# Puddlefolk

**English** | [简体中文](README.zh-CN.md)

![Brand identity](previews/identity.png)

**Family / organic character / bright color blocks**

A fictional brand study actually completed with Imprint on 2026-10-02. Products, people, activities, objects, records, articles, traces, interface examples, and UI are invented. They do not represent a real client, running software, or a launched physical product.

## Brief and positioning

Product: a shared nature-observation journal for parents and children, aimed at families with children aged 6–10 on short walks and weekend outings.

Problem: small discoveries from a walk are quickly forgotten, and photos lack the child’s own observations.

Positioning: **Keep small walking discoveries in a child’s own observation book.**

Value boundary: preserve discoveries, drawings, and a family member’s words in a journal to revisit. It does not judge species safety, edibility, or route safety.

Key traits: curious, friendly, at ease. Placements: mobile observation cards, family journals, and activity stickers.

## Naming exploration and trade-offs

Three naming territories produced six candidates, then a shortlist of Puddlefolk / Mosskip / Small Ramble.

- Friends beside a puddle: Puddlefolk / Pebble Parade.
- Jumping into the small world nearby: Mosskip / Small Ramble.
- Taking discoveries along: Pocket Wonder / Found Acorn.

Selected: **Puddlefolk** (PUD-uhl-fohk). Puddles and companions form an image suitable for family conversation. The long name does not suit extremely small placements.

Preliminary screening: searches for Puddlefolk surfaced same-name music content, but the target page could not be opened for further verification. Mosskip appeared as a gaming username; Small Ramble had leads in other product categories. Puddlefolk was selected for semantic fit with the fictional brief, not exclusivity.

These were limited public searches on 2026-10-02. Some evidence came only from search results and was not fully checked on the destination pages. No trademark-availability conclusion was reached. Image searches did not produce enough visual evidence, so external similarity review remains incomplete.

- [Puddlefolk same-name music lead](https://music.amazon.fr/tracks/B0HBWTBV8J)
- [Mosskip username lead](https://shotbow.net/forum/members/mosskip.3986458/)

## Concepts and construction

A: a curious frog companion; B: a snail; C: a rounded stacked wordmark. Selected A’s character direction with a clear single-line wordmark. The snail felt slow, while the wordmark alone lacked a memorable small-icon element. The wordmark is the main logo; the character is a supporting identity element and does not need to accompany it everywhere.

A built-in image-generation tool first created a black-and-white frog, which vtracer converted into real vector paths with holes for eye and belly whitespace. The original image and full prompt are retained. Full-body detail did not survive small sizes, so a simpler face was drawn, keeping uneven eyes and a tilted pose; the 16 px version removes the mouth. DynaPuff uses wght 600 and wdth 100 with adjusted spacing.

See the [three monochrome directions](exploration/concepts.png), [final monochrome refinement](exploration/refinement.png), and [actual-size images](verification/sizes.png). Initial concepts and final sources intentionally retain differences to show the decisions made. In developer-tool cases, files marked retired document abandoned names and symbols and are not final assets.

## Color and typography

Deep berry purple carries outlines and text; bright yellow supports the character; leaf green suggests outdoors; pink marks occasional discoveries; cream leaves room for observations.

| Role | HEX |
| --- | --- |
| Primary | `#492142` |
| Background | `#FFF8E8` |
| Accent | `#F3CE3D` |
| Supporting | `#9CBD66` |
| Detail | `#EF9CB2` |

The wordmark uses **DynaPuff**, with Manrope for information. Existing letterforms and custom spacing are used; no original typeface is claimed. Font sources are pinned to Google Fonts commit `9710da1eacb3be272583c3224dcb70f9da6eadbb`. `fonts/sources.json` records source URLs, original SHA-256 values, instance axes, and modified names. Static instances were renamed to the Range family and include the original SIL Open Font License; the bundled OFL governs their use.

## Usage and deliverables

Use the full wordmark from **180 px** wide and the full-body character from **64 px**. Prefer the face in dense interfaces; use `app-icon-small` at 16 px. Leave at least one quarter of the wordmark’s total height around it and one eighth of the character’s canvas width around the character. These recommendations come from rendering and visual inspection, not audience experiments. Sizes refer to the canvas rather than the visible artwork; small-size support does not establish recall.

- `sources/logo-*.svg`: the main logo in color, black, and white. White artwork requires a dark background.
- `sources/wordmark-*.svg`: separate outlined lettering. `wordmark-text.svg` retains editable text with an embedded font; check spacing again after changing text.
- `sources/mark-*.svg` and `mark-small.svg`: standalone marks and the small-size adaptation.
- `sources/app-icon*.svg`: generic square icons without pre-cut rounded corners, not a complete platform submission package.
- `exports/`: transparent logo PNGs and icons at 1024, 256, 64, 32, and 16 px.
- `previews/`: an identity overview and an application mockup; interfaces are not functional.
- `verification/`: size checks, source hashes, applicable text/outline comparisons, and export consistency reports.
- `exploration/`: three concepts, monochrome refinement, and retained earlier versions. The original generated frog and complete prompt are included.

Keep proportions and internal whitespace. Do not stretch, outline, or add shadows to the logo, force the full wordmark into 16 px, or use low-contrast supporting colors for small body text. Core logos use shapes and letter paths, not embedded bitmaps masquerading as editable vectors. Pixel symbols are more stable when aligned to whole pixels.

## Verification and remaining limitations

Checked SVG structure, actual render bounds, black/white values, transparent backgrounds, icon dimensions, and agreement between text and outlined versions. Every delivered PNG is byte-for-byte identical to its SVG freshly rendered at the same size. See the [check report](verification/report.json), [export comparison](verification/export-consistency.json), and [actual-size images](verification/sizes.png).

The face and full-body versions simplify facial detail differently. A long-term character system would need more consistent expressions and movement rules. No child-comprehension testing was performed.

This demonstrates the skill’s process and deliverables. It is not customer validation, trademark approval, or evidence that every agent has been tested for compatibility.

[← All examples](../README.md) · [Imprint](../../README.md)
