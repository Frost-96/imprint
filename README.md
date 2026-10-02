# Imprint

**English** | [简体中文](README.zh-CN.md)

A skill for shaping product brand identities, from the first brief to names, logos, app icons, and editable assets.

Imprint connects what a product does, who it serves, and how it should feel to a coherent name and visual identity. Use it to build a brand from scratch or work on a specific piece of an existing one.

[![24 fictional brand identities created with Imprint](examples/gallery/logo-wall.png)](examples/README.md)

24 fictional briefs, actual design outputs. Explore the [full gallery and editable assets](examples/README.md), or see [four selected studies](#selected-studies) below.

## Install

Install directly:

```bash
npx skills add Frost-96/imprint
```

For manual installation, copy the [`skills/imprint/`](skills/imprint/) folder into your agent's skills directory. It contains `SKILL.md`, `agents/`, and `references/`.

## Get started

Tell your agent to use Imprint. Share what you are building, who it is for, how it should feel, and what you want to receive. Include any names, assets, or decisions you want to keep.

**Complete identity**

> Use Imprint to create a brand identity for a rehearsal-planning app for amateur bands. It should feel warm, energetic, and dependable. I need an English name, a logo, and an app icon. Let me choose the name and concept before you refine them.

**Naming only**

> Use Imprint to name a shared cooking journal for families. Explore Chinese and English names that feel familiar and playful. Give me a shortlist with pronunciation, rationale, trade-offs, and any naming conflicts you find.

**App icon from an existing logo**

> Use Imprint to turn the attached logo into an app icon. Keep the name and identity intact. Refine the composition for the icon canvas and check small sizes on light and dark backgrounds.

Imprint works in your conversation language; naming languages and target markets come from your brief. You can set a time or candidate budget, choose between directions yourself, or ask the agent to select and explain its recommendation.

## Selected studies

These four studies were made by running Imprint on fictional briefs, from naming and concept exploration to vector artwork and size checks. The products and scenarios are invented; application images are illustrative mockups.

### Puddlefolk — a curious outdoor companion

![Puddlefolk wordmark, frog character, and small icon](examples/puddlefolk/previews/identity.png)

A shared nature journal for families called for a friendly character that could live on observation cards, stickers, and a phone screen. A frog direction won over a snail and a wordmark-only approach; rounded DynaPuff lettering gives the name its playful voice.

The full character lost detail at small sizes, so the identity includes a simpler face with uneven eyes and a separate 16 px variant. The study shows how a character changes across placements while keeping recognizable features.

[Read the case](examples/puddlefolk/README.md) · [Compare concepts](examples/puddlefolk/exploration/concepts.png) · [Inspect size checks](examples/puddlefolk/verification/sizes.png)

### Fault Lantern — a light on the failing event

![Fault Lantern pixel identity in a debugging interface mockup](examples/fault-lantern/previews/application.png)

A fictional event-capture and debugging tool needed an identity tied to investigation. The selected lantern has a single illuminated point, paired with hand-drawn 5×7 pixel lettering and an amber-on-dark palette.

An earlier cassette direction looked too much like a game controller. Rebuilding the symbol around a lantern gave the name and image a clearer connection; the interface mockup carries that idea into a selected-event view. The trace data is illustrative, with no working replay engine implied.

[Read the case](examples/fault-lantern/README.md) · [Compare concepts](examples/fault-lantern/exploration/concepts.png) · [Explore SVG sources](examples/fault-lantern/sources/)

### Swerve Assembly — an identity that turns with the beat

![Swerve Assembly electronic music identity on an event poster](examples/swerve-assembly/previews/application.png)

For an electronic music event and independent release concept, the brief called for restless, collective energy. Wide, slanted lettering, a turning S mark, and acid yellow-green against blue carry that character into an event poster.

The wordmark adapts Manrope through spacing, proportion, and slant. The smaller “Assembly” line sets a practical limit: the full logo is recommended at 320 px wide or above, with the separate mark available for smaller placements.

[Read the case](examples/swerve-assembly/README.md) · [Compare concepts](examples/swerve-assembly/exploration/concepts.png) · [View the poster](examples/swerve-assembly/previews/application.png)

### Palm Silt — leaving the hand in the work

![Palm Silt pottery identity with an AI-generated ceramic still life](examples/palm-silt/previews/identity.png)

A handbuilt pottery and workshop concept called for warmth and visible human touch. Hand-drawn monoline lettering and an irregular impression mark translate the making process into an identity, supported by terracotta and cream.

Removing the inner impression at small sizes made the symbol feel like a generic ring. Restoring a shorter, thicker curve preserved its character. The accompanying ceramic still life is AI-generated; the logo itself is editable vector artwork.

[Read the case](examples/palm-silt/README.md) · [Inspect the refinement](examples/palm-silt/exploration/refinement.png) · [Explore SVG sources](examples/palm-silt/sources/)

The [complete collection](examples/README.md) includes all 24 studies, with their design decisions, source files, exports, and limitations. Each case is available in English and Simplified Chinese.

## How it approaches the work

For a new identity, the workflow moves from product understanding and strategy through naming, visual concepts, monochrome construction, color, icon adaptation, and delivery. Focused tasks use the relevant stages and build on decisions already made.

- **Strategy before aesthetics.** Define the brand's character and its connection to the product before choosing a visual direction.
- **Concept before polish.** Explore distinct ideas, then refine the strongest direction within your brief.
- **Monochrome before effects.** Resolve shape, spacing, and balance before adding color or surface treatments.
- **Design for the placement.** Adapt the identity for app icons, navigation, and other intended uses; inspect the actual artwork at relevant sizes.
- **Verify the handoff.** Check editable sources and exports, and make incomplete work or unresolved findings explicit.

Existing names, assets, and accepted choices stay fixed unless you authorize changes. The full workflow lives in [SKILL.md](skills/imprint/SKILL.md), with detailed guidance in [references/](skills/imprint/references/).

## What you receive

Deliverables match the scope you request. A complete identity can include:

- Brand positioning, personality, and naming rationale.
- Editable logo sources, applicable wordmarks and lockups, and monochrome and reversed versions.
- App icons, small-size variants, exports, and previews in context.
- Color and typography guidance, spacing and minimum-size rules, and usage examples.
- A record of design decisions, screening findings, and remaining limitations.

Naming-only work ends with verbal deliverables. Visual work requires actual artwork and usable files; an image embedded in an SVG does not qualify as an editable vector logo.

## Tools and scope

Imprint provides the design workflow. Your agent supplies the tools: image generation for raster concepts, vector editing and rendering for editable artwork, image inspection and file access for verification, and browsing for external research. Available tools determine which parts of a task can be completed.

Name and visual-conflict searches are preliminary screening, not trademark clearance or proof of originality. Design assessments remain judgments; audience recognition and market success require evidence beyond the design process.

## License

[MIT](LICENSE) © 2026 Imprint contributors. Third-party fonts, images, and other materials used in a design task retain their own licenses.
