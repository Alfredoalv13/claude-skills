---
name: app-store-assets
description: Create, review, or validate Apple App Store assets (app icon, screenshots, app preview videos, product page header, search results creative, In-App Event media, and the text copy on them) so they comply with Apple's official asset best practices and App Review Guidelines 2.3. Use whenever producing or auditing store listing visuals/metadata for any iOS, iPadOS, macOS, tvOS, visionOS, or watchOS app, before TestFlight/App Store submission, or when the user mentions screenshots, app previews, store assets, product page, or icon exports.
---

# App Store Assets

Rules distilled from Apple's own pages (fetched 2026-10-20). Sources, in priority order:

1. Asset best practices: https://developer.apple.com/app-store/asset-best-practices/
2. Screenshot specs: https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/
3. App preview specs: https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications/
4. Creative asset specs: https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications
5. Product page copy limits: https://developer.apple.com/app-store/product-page/
6. App Review Guidelines 2.3 (2.3.3, 2.3.4, 2.3.7-2.3.10, 2.3.14): https://developer.apple.com/app-store/review/guidelines/#metadata

Apple changes pixel specs often (new devices each year). **Before final export, re-fetch the spec pages (2-4) and compare with `references/specs.md`; update that file if they differ.** The validator reads its tables from that same data in `scripts/validate_assets.py`.

## Workflow

1. **Plan** the set: pick the story order (see Screenshot rules), decide which platforms/devices are required (`references/specs.md`).
2. **Produce** assets from real app UI (simulator/device captures), then add overlays/captions.
3. **Validate** files: `python3 ~/.claude/skills/app-store-assets/scripts/validate_assets.py <file-or-dir> [...]`
4. **Run the content checklist** in `references/checklist.md` manually (the script can't judge content).
5. **Preview** in App Store Connect's Preview tool before submitting.

## Non-negotiable rules (rejection or featuring risks)

- Screenshots show the **app in use**. More than half of the set per device must be real in-use UI; never only title art, login, or splash (2.3.3).
- Previews use **video screen captures of the app only**; narration and text/video overlays are allowed (2.3.4).
- **No** prices, discounts, URLs, copyright symbols, unverifiable claims (awards not received), other platforms'/marketplaces' logos or references, or Apple recognitions (Editor's Choice, App of the Day, Apple Design Award) in any asset.
- Everything must be suitable for a **4+ age rating**, even if the app is rated higher.
- No alpha channel/transparency in any image (icon, screenshots, creative assets).
- Use fictional account data, never real people's data; you must hold rights to all material (2.3.9).
- Keep assets current with the shipped UI; update each release.
- Don't use "For Kids/Children" wording outside the Kids Category.
- Disclose IAP requirements where featured items need purchase (2.3.2).

## Design rules

- **Screenshots:** up to 10 per device size; first 1-3 appear in search (orientation dependent), so they must carry the core value. One main benefit per screenshot, strongest first, a cohesive story. Show Dark Mode in at least one if supported. Text overlays: a short phrase that enhances the visual, not describes it; localize for every supported language. Don't spend a whole screenshot on accolades or calls to action.
- **App previews:** 15-30 s, up to 3 per device size/language. Start strong with the value proposition. Few cuts, no rapid motion. **Must work muted** (autoplay, muted by default); audio is brand texture only (short music loop, no sudden loud moments). Must loop seamlessly. Pick a compelling poster frame (default is 5 s). Tell a beginning-middle-end story with real UI/gameplay.
- **Icon:** unique, memorable, legible at every size (App Store, Spotlight, Home Screen). Simple, no needless detail. 1024x1024 PNG, no alpha. Build layered with Icon Composer (Liquid Glass). Keep icon family consistent (small, large, Watch, alternates) to avoid confusion (2.3.8).
- **Product page header / search results creative:** one clear idea, designed for a first-time visitor, key content inside the template safe area and centered (assets crop differently by device/orientation). Search asset: purpose obvious at a glance, show real interface/content/gameplay. Use Apple's templates (Figma/Photoshop/Pixelmator/Sketch) from the best-practices page.
- **In-App Events:** need 16:9 card media and 9:16 details media; visually continuous; complement (don't duplicate) the event badge.
- **Set cohesion:** consistent palette, fonts, iconography, tone across icon, screenshots, previews, header.
- **Legibility:** key elements and text readable at thumbnail size; focal point in center to avoid clipping.
- **Localization:** localize text overlays and media per locale; choose inclusive, globally appropriate imagery.
- **Violence (games):** action OK; no gore, graphic imagery, or weapons pointed at a person/audience.

## Copy limits (text that accompanies assets)

App name 30 chars; subtitle 30 chars (no generic claims like "world's best", no other-app refs); promotional text 170 chars (changeable anytime, no ranking effect); keywords 100 chars, comma-separated, no spaces after commas, no repeats/plurals/category names/"app"/trademarks; description: first sentence counts, no prices, accolades at the end. Details in `references/specs.md`.

## Files

- `references/specs.md`: all pixel/format/length tables and copy limits, with source URLs and the date fetched.
- `references/checklist.md`: pre-submission checklist (content + technical).
- `scripts/validate_assets.py`: validates dimensions, format, alpha, count, video length/codec/fps/size using `ffprobe` (stdlib only).

When reporting an audit, cite the specific rule and source URL for each failure.
