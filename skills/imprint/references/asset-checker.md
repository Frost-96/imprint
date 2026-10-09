# Running the asset checker

Read when preparing a delivery manifest or running file verification. The checker writes evidence and study previews; it never edits source assets or produces platform packages. Design and visual review remain in [asset production](asset-production.md#verify-actual-files).

## Dependencies and invocation

Use Python 3.10+ with Pillow. SVG previews additionally need `rsvg-convert` (librsvg) on `PATH`. Use an existing environment when available; otherwise install these dependencies through the environment's normal package workflow. The checker does not install anything. Missing capabilities yield `incomplete`, not a pass. Hash verification uses only Python's standard library.

Create a JSON manifest in the delivery directory. Include every required deliverable, including sources, variants, usage notes, and font notices when applicable. Paths are relative to the manifest (absolute paths also work). This example describes a logo package; adapt requirements to the actual task:

```json
{
  "assets": [
    {"path": "source/master.svg", "kind": "logo", "outlined": true},
    {"path": "source/text-editable.svg", "kind": "logo"},
    {"path": "exports/logo-color.png", "kind": "logo", "dimensions": [2048, 522], "alpha": "transparent"},
    {"path": "usage.txt", "kind": "file"}
  ]
}
```

From the installed skill directory, run:

```bash
python3 scripts/verify_assets.py check /absolute/delivery/manifest.json --output /absolute/delivery/checks
python3 scripts/verify_assets.py verify /absolute/delivery/checks/run-EXAMPLE/report.json
```

Use the actual report path printed by `check`. Each run gets a new directory so earlier evidence is retained and stale previews cannot mix with a new run. Inspect its PNGs using the image viewer. The report records input and preview hashes, renderer version, dimensions, alpha extrema, and visible alpha bounds. Bounds describe nontransparent pixels, not semantic subject bounds on an opaque icon background.

Run `check --help` for the default study sizes. View transparent previews against suitable light/dark backgrounds; the PNGs retain their original background/alpha treatment.

## Manifest fields

| Field | Meaning |
| --- | --- |
| `path`, `kind` | Required. `logo` checks SVG/PNG and rejects image elements in SVG; `icon` allows raster artwork. `file` checks existence, nonempty content and hash only, for other deliverables; it does not validate native packages or ZIP contents. |
| `outlined` | Optional boolean, SVG only. Rejects live text when true; it does not prove that the correct letters were outlined. |
| `dimensions` | Optional `[width, height]`. Exact PNG pixel dimensions or SVG viewport dimensions; not inferred platform specifications. |
| `alpha` | `any` (default), `opaque`, or `transparent`. Transparent requires some fully transparent pixels and some visible artwork; it does not detect a painted checkerboard or validate the intended cutout. |
| `sizes` | Optional nonempty list of study long-edge sizes in raster pixels, replacing the logo/icon defaults. Use this for assigned optical variants. Integer dimensions round proportionally; add separate previews for actual placements and platform masks. |
| `resampling` | `lanczos` (default) or `nearest` for raster study previews. For native pixel art, select nearest where appropriate and separately inspect target-platform resampling. |

All entries are required. `file` entries accept only `path` and `kind`; other unknown or misspelled fields are rejected. Reconcile the manifest with the brief: the script cannot discover an omitted requirement. SVGs must be self-contained static artwork; external resources and unsupported dynamic content leave rendering incomplete. SVG IDs and local `href`/`url()` references are checked structurally; rendering and manual inspection still determine their visible effect.

## Results and freshness

Exit `0` means the declared mechanical checks passed; `1` means a file or requirement failed; `2` means checks could not be completed or the invocation/manifest is invalid. In a mixed report, failures take precedence over incomplete checks. Inspect per-asset errors, incomplete checks and notes. Fix required failures and rerun; report unavailable checks honestly.

`verify` checks that the manifest, inputs and generated previews still match the report hashes and preserves the original result status. It detects stale evidence, not tampering with the report itself. Run it before handing off the inspected package. If files moved or changed, rerun `check` and inspect affected previews. Successful parsing/rendering does not verify fonts, spelling, clipping, source/export visual correspondence, color fidelity, aesthetics, actual-size display, native integration, or user selection.
