# Imprint

A skill for shaping product brand identities, from the first brief to names, logos, app icons, and editable assets.

Imprint connects what a product does, who it serves, and how it should feel to a coherent name and visual identity. Use it to build a brand from scratch or work on a specific piece of an existing one.

## Install

Install directly :

```bash
npx skills add Frost-96/imprint
```

Add `-g` to make the skill available across projects.

```bash
npx skills add Frost-96/imprint -g
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
