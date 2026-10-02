# Palm Silt

**English** | [简体中文](README.zh-CN.md)

![Brand identity](previews/identity.png)

**Pottery studio / hand-drawn lettering / earth tones and material**

A fictional brand study actually completed with Imprint on 2026-10-02. Products, people, activities, objects, records, articles, traces, interface examples, and UI are invented. They do not represent a real client, running software, or a launched physical product.

## Brief and positioning

Product: handbuilt pottery and small studio classes for everyday-object users who enjoy traces of making, and adult craft beginners.

Positioning: **Leave the movement of the hand in everyday objects.**

The brief assumes English naming and communication; multilingual brand localization was not completed. These are strategic choices, not market facts established through audience research.

Personality and visible decisions: tactile → uneven contour and simple handwriting; warm → clay and oat surfaces; unhurried → low density and material photography.

Avoid: luxury serif seals, cute mascots, and invented ancient craft heritage.

## Naming exploration and trade-offs

- Earth meets gesture: Palm Silt / Loamfold.
- Softness meets firing: Tender Kiln / Warm Vessel.
- A trace of the maker: Thumbwell / Palm Note.

| Candidate | Specific strengths | Main cost | Decision |
| --- | --- | --- | --- |
| Palm Silt | Two short words clearly connect hand and material. | Needs a category introduction; must not be described as an actual ingredient recipe. | Adopted as a fictional name. |
| Tender Kiln | A contrast between softness and firing. | “Tender” already has adjacent-category usage leads. | Not selected. |
| Thumbwell | Close to the impression of a thumb. | Strong technical-term association; pronunciation is untested with an audience. | Not selected. |

Selected spelling: **Palm Silt**; suggested pronunciation: PAHM silt, with “palm” spoken in the target accent. Palm and Silt combine tactile images of a hand and earth; they do not state that the product recipe consists of silt.

Conflicting or weak candidates were not presented as final recommendations merely to fill a shortlist. The table retains the selection and rejection reasons.

Preliminary screening: Loamfold was already a clothing brand. Tender Kiln searches returned kiln/glass-art meanings, and Tender appeared in pottery. Thumbwell is an existing technical term. Palm Silt and Palmsilt searches mostly matched the two words semantically, with adjacent-word leads for Palm Élan / Silt Design Studio. Availability remains unverified.

Search date: 2026-10-02. Queries: `"Loamfold"`; `"Palm Silt"`; `"Tender Kiln"`; `"Thumbwell" ceramics`; `"Palmsilt"`; `"Palm Silt" ceramics`; `"Palm Silt" pottery studio`. General search and some Exa follow-ups were used. Some destination pages were represented only by search snippets and were not reviewed individually. Domain, social-handle, trademark-registration, and audience spoken-spelling checks were not performed.

- [Loamfold brand statement](https://loamfold.com/pages/statement-of-faith)
- [Tender glass-work search result](https://www.vitreus-art.co.uk/tender-fused-vitreus-art.html)
- [Thumbwell technical term](https://www.globalpointofcare.abbott/content/dam/ardx/globalpointofcare/apoc/support/i-stat-1/technical-bulletins/english/istat-large-thumbwell/738598-00B.pdf)
- [Adjacent word-use lead](https://www.palmelan.com/)

## Concepts and construction

A: an irregular open form with an inner impression; B: hands holding an object; C: maker’s handwriting alone. Selected A with a hand-drawn wordmark to retain touch and a usable standalone stamp. B could read as a heart; C lacked a compact entry point.

Each letter of palm silt was drawn with round-ended monoline strokes and modest height differences. The first small version removed the inner impression, but visual inspection found only a generic ring left. A shorter, thicker inner curve restored it. The pre-refinement size board is retained for comparison.

See the [three monochrome directions](exploration/concepts.png), [final monochrome refinement](exploration/refinement.png), and [actual-size images](verification/sizes.png). Initial concepts and final sources intentionally retain differences to show the decisions made. In developer-tool cases, files marked retired document abandoned names and symbols and are not final assets.

## Color and typography

Earth brown carries text and the mark; oat forms the background; terracotta covers larger areas and labels; stone gray is secondary. Material character primarily comes from the still life, without baking texture into the core logo.

| Role | HEX |
| --- | --- |
| Primary text / outline | `#573C30` |
| Background | `#F2E6D5` |
| Accent | `#B76E50` |
| Supporting | `#B4B1A0` |

Palm Silt’s wordmark is hand-drawn monoline vector artwork, with no corresponding typeable font. Manrope supplies ordinary information text; JetBrains Mono supplies code, state, and event text in the two developer-tool studies. Bundled fonts retain their respective SIL Open Font Licenses. Instances are renamed RangeBody, RangeBodyBold, and RangeTerminal as applicable. Source URLs, hashes, and axes are in `fonts/sources.json`, with licenses alongside them. Static instances come from a pinned Google Fonts commit; modifying a font does not mean designing it from scratch.

## Usage and deliverables

Leave at least one quarter of the full composition’s canvas height around it, and at least 32/256 of canvas width around the standalone impression. The minimum recommended full-logo width is **240 px**. These recommendations come from rendering and visual inspection, not audience experiments. Sizes refer to the canvas rather than the visible artwork; small-size support does not establish recall.

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

Use 16 px only for an entry point after recognition has been established; the inner impression is easier to read at 32 px and above. The still life is generated imagery, not a product that was physically made, fired, or photographed.

The built-in imagegen tool generated the still life. Its original is `previews/still-life-original.png`; the full prompt is `exploration/imagegen-prompt.txt`. The core logo was constructed independently, not extracted from a photograph or built by embedding a photo in its SVG.

External visual screening produced only a few category references and search leads, without a complete visual-similarity review. No claim is made of absolute originality, name clearance, or demonstrated market recognition. These limits do not prevent the delivered files from showing the design process.

[← All examples](../README.md) · [Imprint](../../README.md)
