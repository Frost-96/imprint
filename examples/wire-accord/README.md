# Wire Accord

**English** | [简体中文](README.zh-CN.md)

![Brand identity](previews/identity.png)

**Developer tool / technical diagrams / blue-and-white collaboration**

A fictional brand study actually completed with Imprint on 2026-10-02. Products, people, activities, objects, records, articles, traces, interface examples, and UI are invented. They do not represent a real client, running software, or a launched physical product.

## Brief and positioning

Product: a brand concept for collaborative API-contract review, field changes, and example responses, serving frontend and backend developers who need to align their interfaces.

Positioning: **One agreement, with the same field visible on both sides.**

The brief assumes English naming and communication; multilingual brand localization was not completed. These are strategic choices, not market facts established through audience research.

Personality and visible decisions: explicit → connected schema diagrams; cooperative → paired endpoints; measured → fine grids and calm dense information.

Avoid: generic glowing AI orbs, literal ship illustrations, and security-certification claims.

## Naming exploration and trade-offs

- Shared agreement: Wire Accord / Common Field.
- Transport between teams: Schema Ferry / Draftport.
- Visible change: Delta Sheet / Field Margin.

| Candidate | Specific strengths | Main cost | Decision |
| --- | --- | --- | --- |
| Wire Accord | A clear two-sided agreement, natural to say and write. | Accord has other software uses; the full name still needs checking. | Adopted as a fictional name. |
| Schema Ferry | A technical term connected to delivery. | An existing project in the same field was found. | Dropped for a conflict. |
| Delta Sheet | Easy to understand change information. | Too descriptive to support a standalone name. | Dropped for insufficient quality. |

Selected spelling: **Wire Accord**; suggested pronunciation: WIRE uh-KORD. Wire relates to interface exchange; Accord to a shared agreement. Keep the full name rather than Accord alone.

Conflicting or weak candidates were not presented as final recommendations merely to fill a shortlist. The table retains the selection and rejection reasons.

Preliminary screening: Schema Ferry matched the same-field schema_ferry Ruby gem and was dropped. DraftPort was already a software product. Delta Sheet was too close to technical-documentation terminology. Exact, joined-spelling, and software searches for Wire Accord mostly returned semantic matches. Accord Project is an adjacent software context, leaving a potential confusion risk and no legal-availability conclusion.

Search date: 2026-10-02. Queries: `"Schema Ferry"`; `"Draftport"`; `"Wire Accord"`; `"Schema Ferry" API`; `"Schemaferry"`; `"Delta Sheet" software API`; `"Wire Accord" API`; `"Wire Accord" software`; `"Wireaccord"`. General search and some Exa follow-ups were used. Some destination pages were represented only by search snippets and were not reviewed individually. Domain, social-handle, trademark-registration, and audience spoken-spelling checks were not performed.

- [schema_ferry project documentation](https://rubydoc.info/gems/schema_ferry)
- [Existing DraftPort product](https://draftport.app/)
- [Adjacent Accord Project context](https://docs.accordproject.org/docs/accordproject/)
- [Delta Sheet terminology example](https://www.infineon.com/dgdl/xc164CM-CS_deltasheet_1.0D3.pdf?fileId=db3a304412b407950112b40c11e60a20)

## Concepts and construction

A: two field tracks inside offset frames; B: a document in transit; C: name initials. A was selected because the same fields sit within both sides’ boundaries and can extend directly into a contract-comparison diagram. B looks like a generic file tool; C’s initials give fewer purpose clues.

Deeper screening found schema_ferry software and prompted the rename from Schema Ferry to Wire Accord. The mark’s strategy remained a two-party agreement, so the concept was retained. Widened gaps between frames and field lines to remove initial merging. The 32/16 px versions thicken the strokes; individual field nodes are not expected to remain readable at 16 px.

See the [three monochrome directions](exploration/concepts.png), [final monochrome refinement](exploration/refinement.png), and [actual-size images](verification/sizes.png). Initial concepts and final sources intentionally retain differences to show the decisions made. In developer-tool cases, files marked retired document abandoned names and symbols and are not final assets.

## Color and typography

Deep blue carries text; bright blue indicates interaction and shared agreement; pale blue separates structural groups; small terracotta accents flag changes awaiting confirmation. The grid supports layout, becoming alignment and connection relationships in the application.

| Role | HEX |
| --- | --- |
| Primary text / outline | `#153374` |
| Background | `#F8FAFF` |
| Accent | `#2858DE` |
| Supporting | `#DCE8FC` |
| Change cue | `#DE7968` |

The wordmark uses a static Manrope instance, with both editable text and outlined sources. Manrope supplies ordinary information text; JetBrains Mono supplies code, state, and event text in the two developer-tool studies. Bundled fonts retain their respective SIL Open Font Licenses. Instances are renamed RangeBody, RangeBodyBold, and RangeTerminal as applicable. Source URLs, hashes, and axes are in `fonts/sources.json`, with licenses alongside them. Static instances come from a pinned Google Fonts commit; modifying a font does not mean designing it from scratch.

## Usage and deliverables

Leave at least one quarter of the symbol width around the lockup. Use the full logo from **260 px** wide and prefer the symbol at **32 px** or above. These recommendations come from rendering and visual inspection, not audience experiments. Sizes refer to the canvas rather than the visible artwork; small-size support does not establish recall.

- `sources/logo-*.svg`: the main logo in color, black, and white. White artwork requires a dark background.
- `sources/wordmark-*.svg`: separate outlined lettering. Swerve Assembly and Wire Accord also include `wordmark-text.svg`.
- `sources/mark-*.svg` and `mark-small.svg`: standalone marks and the small-size adaptation.
- `sources/app-icon*.svg`: generic square icons without pre-cut rounded corners, not a complete platform submission package.
- `exports/`: transparent logo PNGs and icons at 1024, 256, 64, 32, and 16 px. Logo PNGs are 1200 px wide, with a separate minimum-size full logo. The 32/16 px icon exports use the small source.
- `previews/`: an identity overview and an application mockup; interfaces are not functional.
- `verification/`: size checks, source hashes, applicable text/outline comparisons, and export consistency reports.
- `exploration/`: three concepts, monochrome refinement, and retained earlier versions.

Keep proportions and internal whitespace. Do not stretch, outline, or add shadows to the logo, force the full wordmark into 16 px, or use low-contrast supporting colors for small body text. Core logos use shapes and letter paths, not embedded bitmaps masquerading as editable vectors. Pixel symbols are more stable when aligned to whole pixels.

## Verification and remaining limitations

All final source SVGs were rendered. Checks covered the absence of embedded bitmaps in core vector artwork, clipping at transparent asset edges, black/white values, icon dimensions, and opaque backgrounds. In this four-case batch, the two font-based wordmarks were compared with their outlined versions at 2400 px width; font-text comparison does not apply to the two hand-drawn wordmarks. Every final PNG is byte-for-byte identical to a fresh render of its SVG at the same size.

Visual inspection covered large artwork, application scenes, black/white and reversed versions, and icons at 256, 64, 32, and 16 px. The 1024 px icons were checked for dimensions and source correspondence; the source symbols were also inspected at large size. Reports: [structure and rendering](verification/report.json), [PNG correspondence](verification/export-consistency.json).

Brackets, tracks, and sans-serif type are common in developer tools, so recognition depends more on the combination. Field-node details are weak at 16 px; 32 px and above is better for standalone use. The interface depicts one fictional review, without executing contract validation or a mock service.

External visual screening produced only a few category references and search leads, without a complete visual-similarity review. No claim is made of absolute originality, name clearance, or demonstrated market recognition. These limits do not prevent the delivered files from showing the design process.

[← All examples](../README.md) · [Imprint](../../README.md)
