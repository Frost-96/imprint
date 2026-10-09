#!/usr/bin/env python3
"""Check an explicit identity delivery manifest; generate evidence, never edit sources."""

import argparse
import hashlib
import io
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

try:
    from PIL import Image, __version__ as PILLOW_VERSION
except ImportError:
    Image = None
    PILLOW_VERSION = None


SIZES = {"logo": [1024, 256, 64, 32, 16], "icon": [1024, 256, 128, 64, 32, 16]}
SVG_NS = "http://www.w3.org/2000/svg"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_manifest(path):
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict) or set(manifest) != {"assets"}:
        raise ValueError("Manifest must contain only an assets array")
    assets = manifest["assets"]
    if not isinstance(assets, list) or not assets:
        raise ValueError("assets must be a nonempty array")
    seen = set()
    allowed = {"path", "kind", "outlined", "alpha", "dimensions", "sizes", "resampling"}
    for item in assets:
        if not isinstance(item, dict) or set(item) - allowed:
            raise ValueError("Unknown asset field or invalid asset object")
        if not isinstance(item.get("path"), str) or not item["path"].strip():
            raise ValueError("Each asset needs a nonempty path")
        resolved = (path.parent / item["path"]).resolve()
        if resolved in seen:
            raise ValueError(f"Duplicate asset: {item['path']}")
        seen.add(resolved)
        if item.get("kind") not in ("logo", "icon", "file"):
            raise ValueError("kind must be logo, icon, or file")
        if "outlined" in item and type(item["outlined"]) is not bool:
            raise ValueError("outlined must be a boolean")
        if item.get("alpha", "any") not in ("any", "opaque", "transparent"):
            raise ValueError("alpha must be any, opaque, or transparent")
        if item.get("resampling", "lanczos") not in ("lanczos", "nearest"):
            raise ValueError("resampling must be lanczos or nearest")
        for field in ("dimensions", "sizes"):
            if field in item:
                values = item[field]
                if (not isinstance(values, list) or not values
                        or any(type(n) is not int or not 1 <= n <= 8192 for n in values)):
                    raise ValueError(f"{field} must contain integers from 1 to 8192")
                if field == "dimensions" and len(values) != 2:
                    raise ValueError("dimensions must be [width, height]")
        if item["kind"] == "file" and set(item) != {"path", "kind"}:
            raise ValueError("file entries support only path and kind (existence/hash only)")
        if item.get("outlined") and resolved.suffix.lower() != ".svg":
            raise ValueError("outlined requires an SVG asset")
    return assets


def svg_info(data, item):
    """Validate local static SVG references before allowing the renderer to read it."""
    errors, incomplete, notes = [], [], []
    # Avoid custom entities, including a UTF-16 encoded declaration.
    if re.search(br"<!\s*(?:DOCTYPE|ENTITY)\b", data.replace(b"\x00", b""), re.I):
        raise ValueError("SVG DTD/entity declarations are unsupported; use a self-contained SVG")
    root = ET.fromstring(data)
    if root.tag != f"{{{SVG_NS}}}svg":
        raise ValueError("Not an SVG document with the SVG namespace")
    elements = list(root.iter())
    tags = [e.tag.rsplit("}", 1)[-1] for e in elements]
    ids = Counter(e.get("id") for e in elements if e.get("id") is not None)
    if any(count > 1 for count in ids.values()):
        errors.append("duplicate_svg_ids")
    if item["kind"] == "logo" and any(t in ("image", "feImage") for t in tags):
        errors.append("raster_or_image_reference_in_vector_logo")
    if item.get("outlined") and any(t in ("text", "tspan", "textPath") for t in tags):
        errors.append("live_text_in_outline_master")
    elif "text" in tags:
        notes.append("Live text: manually confirm loaded fonts and compare with outline master")
    if set(tags) & {"script", "foreignObject", "animate", "animateMotion", "animateTransform", "set"}:
        incomplete.append("non_static_svg_content_not_supported")

    refs = []
    for element in elements:
        for key, value in element.attrib.items():
            if key.rsplit("}", 1)[-1] == "href":
                refs.append(value.strip())
            refs.extend(re.findall(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", value, re.I))
        if element.tag == f"{{{SVG_NS}}}style":
            css = element.text or ""
            refs.extend(re.findall(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", css, re.I))
            if re.search(r"@import|\\", css, re.I):
                incomplete.append("css_import_or_escape_requires_manual_review")
    for ref in refs:
        ref = ref.strip()
        if ref.startswith("#"):
            if ref[1:] not in ids:
                errors.append(f"missing_svg_target: {ref}")
        elif not re.match(r"data:image/(?:png|jpeg|webp);base64,", ref, re.I):
            incomplete.append("external_or_unsupported_svg_resource")

    box = root.get("viewBox")
    viewbox = None
    if box is not None:
        viewbox = [float(n) for n in re.split(r"[\s,]+", box.strip())]
        if len(viewbox) != 4 or not all(math.isfinite(n) for n in viewbox) or min(viewbox[2:]) <= 0:
            raise ValueError("Invalid SVG viewBox")

    def dimension(value):
        match = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)(?:px)?", value or "")
        return float(match[1]) if match else None

    width, height = dimension(root.get("width")), dimension(root.get("height"))
    if width is None or height is None:
        if viewbox is None:
            raise ValueError("SVG needs a positive viewBox or explicit pixel width and height")
        if (root.get("width") and width is None) or (root.get("height") and height is None):
            incomplete.append("non_pixel_svg_dimensions_require_explicit_preview_conversion")
        width, height = viewbox[2:]
    if not all(math.isfinite(n) for n in (width, height)) or min(width, height) <= 0:
        raise ValueError("SVG dimensions must be positive")
    return (width, height), {"viewBox": viewbox, "live_text": "text" in tags}, errors, incomplete, notes


def pixels_info(im):
    alpha = im.convert("RGBA").getchannel("A")
    return {"dimensions": list(im.size), "mode": im.mode,
            "alpha_extrema": list(alpha.getextrema()),
            "visible_alpha_bounds": alpha.getbbox(),
            "has_alpha_channel": "A" in im.getbands() or "transparency" in im.info,
            "has_icc_profile": bool(im.info.get("icc_profile"))}


def alpha_errors(info, expected):
    low, high = info["alpha_extrema"]
    if high == 0:
        return ["empty_transparent_artwork"]
    if expected == "opaque" and low != 255:
        return ["expected_opaque_pixels"]
    if expected == "transparent" and low != 0:
        return ["expected_fully_transparent_background_pixels"]
    return []


def check_asset(item, base, run, index, renderer):
    path = (base / item["path"]).resolve()
    result = {"path": str(path), "requirements": item, "errors": [], "incomplete": [],
              "notes": [], "previews": []}
    errors, incomplete = result["errors"], result["incomplete"]
    try:
        data = path.read_bytes()
        result.update(sha256=digest(data), bytes=len(data))
        if not data:
            raise ValueError("Empty file")
        if item["kind"] == "file":
            result["notes"].append("Existence and hash only; content validity not checked")
        else:
            suffix = path.suffix.lower()
            original = None
            if suffix == ".svg":
                dims, info, err, inc, notes = svg_info(data, item)
                result["source"] = {"dimensions": list(dims), **info}
                errors.extend(err)
                incomplete.extend(inc)
                result["notes"].extend(notes)
                if renderer is None:
                    incomplete.append("SVG rendering needs rsvg-convert on PATH")
            elif suffix == ".png":
                if Image is not None:
                    with Image.open(io.BytesIO(data)) as im:
                        if im.format != "PNG":
                            raise ValueError(".png file is not a PNG")
                        im.verify()
                    with Image.open(io.BytesIO(data)) as im:
                        im.load()
                        result["source"] = pixels_info(im)
                        if getattr(im, "n_frames", 1) != 1:
                            raise ValueError("Animated PNG is not a static identity asset")
                        dims = im.size
                        original = im.convert("RGBA")
                    errors.extend(alpha_errors(result["source"], item.get("alpha", "any")))
                else:
                    dims = None
            else:
                raise ValueError("Visual checks support SVG and PNG; use kind=file for other deliverables")
            if Image is None:
                incomplete.append("Pixel inspection and previews need Pillow in this Python environment")
            if dims and "dimensions" in item and list(dims) != item["dimensions"]:
                errors.append(f"dimensions_mismatch: expected {item['dimensions']}, got {list(dims)}")
            if not errors and not incomplete:
                sizes = sorted(set(item.get("sizes", SIZES[item["kind"]])), reverse=True)
                if suffix == ".png" and max(sizes) > max(dims):
                    result["notes"].append("Some previews upscale the raster; they add no source detail")
                # Render the captured bytes so evidence refers to the recorded hash.
                with tempfile.TemporaryDirectory(prefix="imprint-source-") as tmp:
                    snapshot = Path(tmp) / "source.svg"
                    if suffix == ".svg":
                        snapshot.write_bytes(data)
                    for size in sizes:
                        width, height = [max(1, round(n * size / max(dims))) for n in dims]
                        target = run / f"{index:03d}-{size}.png"
                        if suffix == ".svg":
                            proc = subprocess.run(
                                [renderer, "-w", str(width), "-h", str(height), "-o", str(target), str(snapshot)],
                                capture_output=True, text=True, timeout=60,
                            )
                            if proc.returncode:
                                errors.append(f"svg_render_failed: {proc.stderr.strip()[:500]}")
                                break
                            if proc.stderr.strip():
                                incomplete.append(f"renderer_warning: {proc.stderr.strip()[:500]}")
                            with Image.open(target) as im:
                                im.load()
                                info = pixels_info(im)
                        else:
                            mode = Image.Resampling.NEAREST if item.get("resampling") == "nearest" else Image.Resampling.LANCZOS
                            im = original.resize((width, height), mode)
                            im.save(target)
                            info = pixels_info(im)
                        if info["dimensions"] != [width, height]:
                            errors.append("renderer_output_dimensions_mismatch")
                        if suffix == ".svg" and size == sizes[0]:
                            errors.extend(alpha_errors(info, item.get("alpha", "any")))
                        elif info["visible_alpha_bounds"] is None:
                            result["notes"].append(f"Artwork disappears at study size {size}; inspect required-use impact")
                        result["previews"].append({"path": target.name, "sha256": digest(target.read_bytes()), **info})
        if digest(path.read_bytes()) != result["sha256"]:
            errors.append("source_changed_during_check")
    except (OSError, ValueError, SyntaxError, ET.ParseError, subprocess.SubprocessError) as exc:
        errors.append(str(exc))
    result["status"] = "failed" if errors else "incomplete" if incomplete else "passed"
    return result


def check(manifest_path, output):
    manifest_path = manifest_path.resolve()
    manifest_bytes = manifest_path.read_bytes()
    assets = load_manifest(manifest_path)
    output.mkdir(parents=True, exist_ok=True)
    run = Path(tempfile.mkdtemp(prefix="run-", dir=output.resolve()))
    renderer = shutil.which("rsvg-convert")
    version = None
    if renderer:
        version = subprocess.run([renderer, "--version"], capture_output=True, text=True, timeout=10).stdout.strip()
    results = [check_asset(item, manifest_path.parent, run, i, renderer) for i, item in enumerate(assets, 1)]
    status = "failed" if any(r["errors"] for r in results) else "incomplete" if any(r["incomplete"] for r in results) else "passed"
    report = {"schema_version": 1, "status": status, "created_at": datetime.now(timezone.utc).isoformat(),
              "manifest": {"path": str(manifest_path), "sha256": digest(manifest_bytes)},
              "tools": {"python": sys.version.split()[0], "pillow": PILLOW_VERSION, "svg_renderer": version},
              "preview_convention": "long edge in raster pixels; aspect ratio preserved; no platform masks",
              "manual_checks": ["Inspect clipping, spelling, fonts, color and source/export correspondence",
                                "Inspect recognition, optical balance and negative space at actual display sizes",
                                "Check intended backgrounds, platform contexts and assigned optical variants",
                                "Confirm scope coverage and user selection; format checks do not establish design quality"],
              "assets": results}
    if digest(manifest_path.read_bytes()) != report["manifest"]["sha256"]:
        report["status"] = "failed"
        report["error"] = "manifest_changed_during_check"
    target = run / "report.json"
    target.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{report['status']}: {len(results)} assets; report: {target}")
    return {"passed": 0, "failed": 1, "incomplete": 2}[report["status"]]


def verify(report_path):
    report = json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("schema_version") != 1 or report.get("status") not in ("passed", "failed", "incomplete"):
        raise ValueError("Unsupported report")
    if not isinstance(report.get("assets"), list) or not report["assets"]:
        raise ValueError("Report has no assets")
    changed = []
    entries = [report["manifest"], *report["assets"]]
    entries += [{**preview, "path": str(report_path.parent / preview["path"])}
                for asset in report["assets"] for preview in asset["previews"]]
    for entry in entries:
        path = Path(entry["path"])
        try:
            if digest(path.read_bytes()) != entry.get("sha256"):
                changed.append(str(path))
        except OSError:
            changed.append(str(path))
    if changed:
        print("Stale or missing evidence:\n" + "\n".join(changed))
        return 1
    print(f"Hashes unchanged; original mechanical check status: {report['status']}. Manual review still required.")
    return {"passed": 0, "failed": 1, "incomplete": 2}[report["status"]]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    defaults = "; ".join(f"{kind}: {', '.join(map(str, sizes))}" for kind, sizes in SIZES.items())
    check_parser = sub.add_parser(
        "check", help="Validate manifest assets and write a new report/previews directory",
        epilog=f"Default study sizes (long-edge raster pixels): {defaults}. Not platform export specifications.",
    )
    check_parser.add_argument("manifest", type=Path)
    check_parser.add_argument("--output", type=Path, required=True)
    verify_parser = sub.add_parser("verify", help="Detect changed sources, manifest or previews since a check")
    verify_parser.add_argument("report", type=Path)
    args = parser.parse_args()
    try:
        return check(args.manifest, args.output) if args.command == "check" else verify(args.report)
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(f"Cannot complete check: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
