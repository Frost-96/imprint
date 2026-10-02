# Bayward

**English** | [简体中文](README.zh-CN.md)

![Brand identity](previews/identity.png)

**Industrial / compact / high contrast**

A fictional brand study actually completed with Imprint on 2026-10-02. Products, people, activities, objects, records, articles, traces, interface examples, and UI are invented. They do not represent a real client, running software, or a launched physical product.

## Brief and positioning

Product: equipment-maintenance and shift-handoff logs for technicians and shift leads in small manufacturing workshops.

Problem: observations, repair records, and pending work are scattered across whiteboards and messages, making it difficult for the next shift to continue.

Positioning: **Leave the next shift a record they can act on.**

Value boundary: retain evidence of each observation, equipment state, and the next person taking over. No automatic diagnosis or safety certification is promised.

Key traits: dependable, continuous, practical. Placements: workshop tablets, equipment cards, and desktop handoff lists.

## Naming exploration and trade-offs

Three naming territories produced six candidates, then a shortlist of Bayward / Rivet Relay / Torque Ledger.

- A dependable workshop guide: Bayward / Holdfast.
- Passing work to the next pair of hands: Rivet Relay / Second Shift.
- Readable records left by equipment: Torque Ledger / Witness Bay.

Selected: **Bayward** (BAY-werd). “Bay” suggests a workstation and “ward” contributes direction. This is the creative interpretation for this study, not a historical etymology.

Preliminary screening: Rivet Relay was already used for a workflow-automation service. Torque Ledger appeared as a torque checklist and was insufficiently distinctive. Neither was selected. Bayward searches found existing construction-company and Bayward Consulting leads, so the name is retained only for this fictional study and is not cleared for use.

These were limited public searches on 2026-10-02. Some evidence came only from search results and was not fully checked on the destination pages. No trademark-availability conclusion was reached. Image searches did not produce enough visual evidence, so external similarity review remains incomplete.

- [Rivet Relay service](https://rivetrelay.com/services/workflow-automation)
- [Torque Ledger checklist](https://safetyculture.com/library/construction/torque-ledger-pxl14y4dwg2r4iw1)
- [Bayward Builders directory listing](https://www.bbb.org/us/ca/san-francisco/profile/general-contractor/bayward-builders-1116-965027)
- [Bayward Consulting usage lead](https://www.infoguardsecurity.com/cybersecurity-consultants-experts/)

## Concepts and construction

A: opposing components; B: a forward channel; C: a folded-corner record. A was selected because it can express continuity between shifts without a wrench or gear. B’s arrow meaning was too broad; C looked more like a generic document tool. This is a design judgment, without user testing.

The first components merged at their connection. Opening that area produced two clear solid forms, with a wider gap in the dedicated 16 px version. The wordmark uses Barlow Condensed Bold with adjusted AY, YW, and WA spacing.

See the [three monochrome directions](exploration/concepts.png), [final monochrome refinement](exploration/refinement.png), and [actual-size images](verification/sizes.png). Initial concepts and final sources intentionally retain differences to show the decisions made. In developer-tool cases, files marked retired document abandoned names and symbols and are not final assets.

## Color and typography

Graphite carries the primary form and reading text. Signal orange marks entry points and areas needing attention; paper white supports record panels, with gray-green as a secondary color. Orange does not indicate safety certification.

| Role | HEX |
| --- | --- |
| Primary | `#191B1D` |
| Background | `#F1EFE8` |
| Accent | `#F4512A` |
| Supporting | `#BAC3BE` |

The wordmark uses **Barlow Condensed**, with Manrope for information. Existing letterforms and custom spacing are used; no original typeface is claimed. Font sources are pinned to Google Fonts commit `9710da1eacb3be272583c3224dcb70f9da6eadbb`. `fonts/sources.json` records source URLs, original SHA-256 values, instance axes, and modified names. Static instances were renamed to the Range family and include the original SIL Open Font License; the bundled OFL governs their use.

## Usage and deliverables

Use the full lockup from **180 px** wide and the standalone components from **32 px**. At 16 px use the small variant. External clear space should be at least one quarter of the total logo height. These recommendations come from rendering and visual inspection, not audience experiments. Sizes refer to the canvas rather than the visible artwork; small-size support does not establish recall.

- `sources/logo-*.svg`: the main logo in color, black, and white. White artwork requires a dark background.
- `sources/wordmark-*.svg`: separate outlined lettering. `wordmark-text.svg` retains editable text with an embedded font; check spacing again after changing text.
- `sources/mark-*.svg` and `mark-small.svg`: standalone marks and the small-size adaptation.
- `sources/app-icon*.svg`: generic square icons without pre-cut rounded corners, not a complete platform submission package.
- `exports/`: transparent logo PNGs and icons at 1024, 256, 64, 32, and 16 px.
- `previews/`: an identity overview and an application mockup; interfaces are not functional.
- `verification/`: size checks, source hashes, applicable text/outline comparisons, and export consistency reports.
- `exploration/`: three concepts, monochrome refinement, and retained earlier versions.

Keep proportions and internal whitespace. Do not stretch, outline, or add shadows to the logo, force the full wordmark into 16 px, or use low-contrast supporting colors for small body text. Core logos use shapes and letter paths, not embedded bitmaps masquerading as editable vectors. Pixel symbols are more stable when aligned to whole pixels.

## Verification and remaining limitations

Checked SVG structure, actual render bounds, black/white values, transparent backgrounds, icon dimensions, and agreement between text and outlined versions. Every delivered PNG is byte-for-byte identical to its SVG freshly rendered at the same size. See the [check report](verification/report.json), [export comparison](verification/export-consistency.json), and [actual-size images](verification/sizes.png).

The abstract components may resemble other industrial symbols. A sufficient external visual-similarity review remains incomplete.

This demonstrates the skill’s process and deliverables. It is not customer validation, trademark approval, or evidence that every agent has been tested for compatibility.

[← All examples](../README.md) · [Imprint](../../README.md)
