# Asset production, verification, and brand handoff

Read before final production, and earlier when source feasibility or rendering defects affect a design. These checks establish production readiness; inspection of the actual artwork supports visual and brand judgments. Use the main skill's scope and selection rules.

## Sources and exports

For fonts used in identity artwork, including icon letters or monograms, record the typeface and source and verify its terms for the intended use. Permission to use a font does not establish permission to redistribute its files.

- **Core logo:** Produce actual editable vector geometry for the selected symbol, wordmark, or combination. Export true SVG and transparent PNG from the master, with monochrome, reversed, and applicable color/light/dark variants. The approved monochrome structure is the foundation; preserve any approved later treatment in separate appropriate versions. A vector-looking bitmap or raster embedded in SVG is not a vector deliverable.
- **Wordmark:** Preserve the exact selected name as editable outlines. For font-based lettering, also include a text-editable source. Identify custom lettering as outline artwork rather than claiming it is text-editable. Do not invent a wordmark for a symbol-only request.
- **Lockup:** When included, compose symbol and wordmark with documented spacing and intended placement. A wordmark-only identity does not require a separate symbol.
- **Product icon:** Retain the complete treatment, high-resolution master, actual vector/raster/layer sources, resolution, editability, and requested platform executions. A symbol SVG does not replace the icon. If material/lighting cannot be faithfully reconstructed, preserve the inspected raster and disclose raster-only delivery. Explicit vector-icon requirements need actual vector work or partial-delivery status. Use [platform execution](icons/platforms.md) from design onward; export native packages only when requested and validate their resources/tool compatibility. Distinguish static artwork, constructed packages, and tested native integration. Track final-version selection under the [icon workflow](icons/workflow.md#final-choice-and-handoff); production readiness alone does not establish user acceptance.
- **Variants and previews:** Keep canonical logo, product-icon executions, and any small-size simplifications distinct and linked to their applicable uses. Store real rendered previews and test dimensions. An application mockup is not an export package.

## Clean up faithfully

Preserve the selected silhouette, defining relationships, and approved appearance. Set exact colors, opacity, openings, and bounds in the editable master rather than relying on repeated raster prompting for exact pixels. Incidental shading, low-alpha residue, and presentation margins are not automatically design invariants. Compare cleanup/reconstruction with the selected design; material changes require appropriate design review and selection authority.

Count intentional color families separately from antialiasing and incidental shading. A high unique-color count does not establish a gradient. Check alpha and composite on known backgrounds before interpreting a halo or backdrop. Distinguish opaque interior fills, transparent canvas, and partial-alpha residue. Viewer checkerboards or black backgrounds are not necessarily painted into the artwork.

## Verify actual files

1. Render every delivered SVG. Confirm real vector geometry, no embedded/linked raster artwork in core-logo vector masters, correct viewBox/bounds, and no clipping. Check that IDs are unique within each file and internal `url()`/`href` targets exist and resolve to the intended elements; successful rendering alone can hide ambiguous references. Outline masters work without installed fonts; documented text sources may depend on their font.
2. Check spelling and consistency across the package. For font-based wordmarks, render text source and outline master at matching dimensions and compare glyphs/positions. Verify that the renderer loaded the documented font. Diagnose persistent differences at larger scale before attributing them to antialiasing.
3. Render the applicable mark/icon at 1024, 256, 64, 32, and 16 px with preserved aspect ratio; product icons additionally use 128 px and their target environment tests. Record canvas dimensions and visible-art bounds. For non-square marks, define the study dimension and additionally test the actual intended width/height. Inspect at actual display size as well as enlarged diagnostic views. If the available viewer resizes everything, obtain a reliable actual-size view or mark that check incomplete.
4. Inspect recognition, negative spaces, detail merging, optical center, edges, and weight. Test small-size variants independently; record which variant supports each size. Diagnose excessive canvas margins separately from the mark itself; normalized previews do not authorize changing approved clear space. Document unsupported uses/minimum size rather than claiming every rendering passes.
5. For logos, inspect monochrome, reversed, and applicable light/dark variants on intended backgrounds. For product icons, inspect the requested platform appearances and any monochrome resource required by that platform; do not impose a separate monochrome-logo deliverable. Verify openings and boundaries, including overlaps and edited edges. Provide the appropriate variant and usage rule for each supported background.
6. Verify PNG alpha, dimensions, color treatment, source correspondence, and that files open correctly. A painted checkerboard is not transparency. Retain intentional icon backgrounds; transparency requirements depend on the asset and target.
7. Ensure the artifacts reviewed in final validation match the delivered versions. If production changes identity or appearance materially, repeat affected size/design checks on the changed files; do not rely on approval of an earlier image.

Record actual results and failed/unperformed checks. Creating a file or passing a format check does not prove visual usability.

## Brand Identity Package

For a complete identity, provide the following compact package. For focused tasks, include relevant components and explicitly mark unrelated components outside scope. Do not create speculative extra assets to fill headings.

| Component | Handoff content |
| --- | --- |
| Name | Final name, canonical spelling/case/spacing, pronunciation, meaning or origin, territory and naming rationale; distinguish verified origin from designed meaning |
| Brand | Product positioning, personality, traits, anti-traits and consequential assumptions |
| Logo | Primary mark, wordmark/lockup when applicable, monochrome and reversed forms, core visual concept, geometry/construction logic and editable sources |
| Product Icon | Concept/metaphor and product relationship; high-resolution master and actual sources; composition/color/material logic; requested platform and optical variants; environment evidence; usage and native-validation status; favicon only when in scope |
| Color | Primary/supporting/neutral/background roles, exact values, and guidance on applicable logo variants or platform appearances |
| Visual system, for a complete identity | Applicable display/body typography roles and usage terms; one representative application in an intended medium showing how the type, color, composition, or recurring form works beyond the standalone logo. Reuse a planned usage preview where it demonstrates this; do not invent collateral or production templates outside scope |
| Usage | Clear space with a usable reference unit, measured minimum sizes by variant, recommended backgrounds, common misuse and small-size rules |
| Rationale | Why the name and visual concepts were selected, how requested components share brand DNA without requiring identical shapes, fit the audience, and support plausible future development |
| Validation | Actual screening scope/evidence; visual and production checks linked to the exact delivered artifacts; resolved and remaining concerns; tested sizes/formats and unperformed checks |

Provide clear links to files in a durable workspace or user-selected folder. Include concise usage guidance, not only a presentation image. Keep working histories and rejected alternatives separate from approved production assets.

A suitable structure is editable sources, exports, previews, and one usage/brand note; adapt names and organization to the task. Give the user the files they can actually use and state exact limitations. Check the exact delivered versions against the requested scope and intended uses. Missing required formats, unresolved material defects, or incomplete required file/use checks mean a partial/provisional handoff. Preliminary external screening remains preliminary even when design and production are complete.
