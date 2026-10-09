# Asset production, verification, and brand handoff

Read before production, or earlier when source feasibility affects concept choice. Apply shared [selection](../SKILL.md#user-choices) and [completion rules](../SKILL.md#final-brand-handoff).

## Sources and exports

For fonts, record typeface/source and verify intended-use terms separately from redistribution rights.

- **Logo:** Produce actual editable vector geometry before final selection. Export true SVG and transparent PNG, with monochrome, reversed, and applicable color/light/dark variants. Preserve the unadorned core separately from later treatments. A raster embedded in SVG is not vector artwork.
- **Wordmark:** Preserve exact selected lettering as outlines; also supply a text-editable source for font-based lettering. Custom outlines are not live text. Document spacing for requested lockups.
- **Product icon:** Preserve the complete high-resolution treatment, actual vector/raster/layer sources, resolution, editability, and requested platform executions. Disclose raster-only sources; explicit vector requirements need vector work. Follow [platform execution](icons/platforms.md) for requested native packages, distinguishing constructed files from tested integration.
- **Variants/previews:** Link optical variants to assigned uses. Keep canonical assets, platform executions, and rendered evaluation scenes separate; mockups are not export packages.

## Clean up faithfully

Preserve the selected silhouette, defining relationships, and appearance. Set exact colors, opacity, openings, and bounds in the editable master rather than repeatedly prompting for exact pixels. Compare reconstructions with the selected artwork; incidental shading, residue, and presentation margins are not automatically invariants.

Distinguish intentional color families from antialiasing: many unique colors do not prove a gradient. Check alpha and composite on known backgrounds to distinguish opaque fills, transparent canvas, and partial-alpha residue; a viewer's checkerboard or black backdrop may not be painted into the file.

## Verify actual files

Run the bundled [asset checker](asset-checker.md) against an explicit manifest of all required files. It checks file structure, SVG IDs/references, vector-logo restrictions, declared dimensions/alpha, and renders study sizes while recording hashes. Fix required failures; missing tools or unsupported checks remain unverified. Use an equivalent verified toolchain if dependencies are unavailable, retaining the same evidence and limitations.

Inspect the actual generated previews for what the script cannot establish:

- **Source fidelity:** Correct spelling, geometry, viewBox/framing, clipping, colors, and correspondence between sources and exports. Compare live-text and outline sources at matching dimensions and confirm the intended font loaded; investigate persistent differences before blaming antialiasing.
- **Reduction:** Recognition, negative spaces, detail merging, optical balance and edges at actual display size, plus enlarged diagnostics. The checker uses long-edge raster pixels; additionally test actual intended width/height and platform contexts. Map optical variants to their assigned sizes, distinguish canvas margins from artwork, and record unsupported stress-test sizes separately from failed required uses. A resizing viewer cannot establish actual-size verification.
- **Backgrounds:** Inspect logo monochrome/reversed versions and requested icon appearances on intended backgrounds. Check openings, overlaps, edited edges and halos; a painted checkerboard is not transparency. Preserve approved clear space and intentional icon backgrounds.

Record visual findings against the exact report/assets and run its hash verification before handoff. Changed artwork requires affected file and visual checks again. A mechanical pass establishes neither visual usability nor user acceptance; unresolved required checks keep delivery provisional. Study sizes are not platform export specifications and do not add deliverables such as favicons.

## Brand Identity Package

Include only requested components. A useful layout is sources, exports, previews, and one usage/brand note; keep rejected alternatives and histories separate from production assets.

| Component | Handoff content |
| --- | --- |
| Name | [Naming record](naming.md#final-choice-and-handoff), including canonical spelling, pronunciation, rationale, and evidence status |
| Brand | Positioning, personality, traits/anti-traits, assumptions, and shared identity relationships |
| Logo | Sources/variants above, concept and construction logic |
| Product icon | Sources/executions above, metaphor, composition/color/material logic, optical assignments, context evidence, and native-validation status |
| Color | Exact values, primary/supporting/neutral/background roles, and applicable variants |
| Visual system, for complete identities | Typography roles/terms and one representative intended-use application showing type, color, and composition beyond the logo; reuse a planned preview where suitable |
| Usage | Clear-space reference unit, measured minimum sizes per variant, backgrounds, common misuse, and reduction rules |
| Validation | Selected versions/authority, exact-file checks, screening evidence, resolved/remaining concerns, and unperformed tests |

Provide durable file links and concise usage guidance, with rationale connecting the requested components to the audience and plausible future development. Apply shared completion criteria; complete design/production does not upgrade preliminary external screening.
