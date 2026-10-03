# Platform execution and environment checks

Read when selecting a target execution, before platform constraints can invalidate a concept. Read only applicable platform sections. Keep concept and brand DNA stable while allowing target-specific scale, optical detail, layering, background, and finish. Matching executions are valid when verified; difference is not a goal.

## Verify the target

Record target OS/version range, relevant surfaces, artwork-only versus native-package scope, and available tooling. Consult current official documentation before asserting asset dimensions, safe zones, masks, alpha rules, corner treatment, layering, or export requirements. Save source URL, access date, applicable version, and consequential requirements with the case. If unavailable, mark specifications unverified and avoid claiming platform readiness from memory. These links are starting points, not a frozen specification.

In the shared record, map each required surface/appearance/size to its source or export, corresponding preview/check, and result (passed, failed, or unperformed). Use groups when the same evidence applies; do not invent unnecessary combinations. Reconcile this coverage with the requested scope before handoff so a large preview set cannot conceal an omitted required use.

For environment previews, record the intended logical display size and unit (such as pt, dp or CSS px), its raster-pixel dimensions and density/export scale, and any viewer zoom or resampling. If the scale is unknown, leave actual-size verification unconfirmed. Pixel-reduction boards remain useful stress studies; they do not by themselves establish on-device display size.

| Target | Primary sources | Design and evidence focus |
| --- | --- | --- |
| iOS | [Apple app icons](https://developer.apple.com/design/human-interface-guidelines/app-icons), [Icon Composer](https://developer.apple.com/icon-composer/), [Xcode icon workflow](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer) | Instant recognition, dominant color/form, home-screen mass, current masking and appearances; inspect relevant variants against wallpapers and neighbors. |
| macOS | Same Apple sources and the actual target's Xcode asset workflow | Product-object character, Dock/Finder/search presence, controlled depth/material when justified; inspect large and small contexts. Native quality does not require fake 3D or generic gloss. |
| Android | [Adaptive icons](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive), [launcher tooling](https://developer.android.com/studio/write/create-app-icons), [Play artwork](https://developer.android.com/distribute/google-play/resources/icon-design-specifications) | Foreground/background and applicable monochrome resources, safe-zone/mask behavior and launcher theming; test circle and other supported masks. Store artwork and launcher assets have different roles. |
| Windows | [Design](https://learn.microsoft.com/en-us/windows/apps/design/iconography/app-icon-design), [construction](https://learn.microsoft.com/en-us/windows/apps/design/iconography/app-icon-construction) | Start, taskbar, search and shell usage; inspect small-size silhouettes, padding, alpha/background variants and resource/ICO requirements for the chosen application type. |

For cross-platform work, specify invariants (subject, defining relationship, recognizable color/shape rhythm) and allowed execution differences. Test each target separately. Mobile simplicity and desktop material richness are opportunities, not fixed stylistic categories. A resized desktop render still needs mobile validation.

## Sources, previews, and native validation

Keep clean high-resolution masters or editable layers, a platform adaptation record, assigned exports, and preview-only masks/contexts. System masks and presentation shadows must not accidentally become baked master geometry. Native treatments may be applied by system tooling; a static render is not necessarily an exact reproduction.

For layered workflows, preserve independently usable layers at consistent canvas positions and document composition. For Android, inspect foreground/background and monochrome behavior under current documented mask/safe-zone rules. For Windows, determine the actual framework/packaging before choosing resources. Create only requested platform and identity-surface assets.

An artwork package can be complete without an installable project when that is the requested scope. A requested native package needs actual files accepted by relevant tooling and target validation when available. A PNG renamed .icon/.icns/.ico, XML with nonexistent layers, or a mockup alone is not that package. If tooling/runtime validation is unavailable, distinguish constructed assets, static previews, and unperformed native checks.

Use realistic displayed sizes and comparable neighbor visual mass; follow the [icon workflow's environment checks](workflow.md#platform-size-and-environment-evidence) and label schematics and synthetic neighbors. Check the primary device entry surface plus a contrasting background/appearance where relevant. For multiple targets, one context cannot stand in for all. Preserve masters separately from their evaluation scenes.
