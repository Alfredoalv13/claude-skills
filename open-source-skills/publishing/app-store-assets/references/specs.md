# App Store asset specs (fetched 2026-10-20 from developer.apple.com)

Re-verify against the live pages before final export; Apple adds devices yearly.
The validator hardcodes these tables; keep it in sync.

## App icon
- 1024 x 1024 px, no alpha/transparency. Layered via Icon Composer (Liquid Glass). HIG: /design/human-interface-guidelines/app-icons

## Screenshots (.jpg/.jpeg/.png, no alpha, 1-10 per device size, at least 1 required)
If UI is consistent you may upload only the largest required size; ASC scales down.

### iPhone (portrait W x H; landscape is swapped)
| Class | Accepted portrait sizes | Required? |
|---|---|---|
| iPhone Duo outer | 1398x2034 | Required from Apr 2027 for iOS 27.1 SDK+ apps |
| iPhone Duo inner | 2007x2853 | same |
| Dynamic Island large (6.9") | 1260x2736, 1290x2796, 1320x2868 | fallback Face ID large |
| Face ID large (6.5") | 1284x2778, 1242x2688 | required if no Dynamic Island large |
| Dynamic Island medium (6.3"/6.1") | 1179x2556, 1206x2622 | **Required** |
| Face ID medium | 1170x2532, 1125x2436, 1080x2340 | optional |
| Home Button large | 1242x2208 | optional |
| Home Button medium | 750x1334 | optional |
| 4" | 640x1096 / 640x1136 | optional |
| 3.5" | 640x920 / 640x960 | optional |

### iPad
| Class | Portrait sizes | Required? |
|---|---|---|
| 13" | 2064x2752, 2048x2732 | **Required if app runs on iPad** |
| 12.9" | 2048x2732 | optional |
| 11" | 1488x2266, 1668x2420, 1668x2388, 1640x2360 | optional |
| 10.5" | 1668x2224 | optional |
| 9.7" | 1536x2008, 1536x2048, 768x1004, 768x1024 | optional |

### Mac (16:10): 1280x800, 1440x900, 2560x1600, 2880x1800. Required for Mac apps.
### Apple TV: 1920x1080 or 3840x2160. Required.
### Vision Pro: 3840x2160. Required.
### Apple Watch (pick one size, use for all locales; required for Watch apps)
Ultra 3/4 422x514; Ultra/Ultra 2 410x502; S10-12 416x496; S7-9 396x484; S4-6/SE 368x448; S1-3 312x390.

## App previews
- Optional; up to 3 per device size and language. Shown before screenshots; if aspect ratio differs from screenshots they appear in "A Closer Look".
- 15-30 s, max 500 MB, .mov/.m4v/.mp4 (H.264) or .mov (ProRes 422 HQ). Max 30 fps. Processing up to 24 h.
- H.264: 10-12 Mbps target, Progressive, up to High Profile Level 4.0. Audio stereo 256 kbps AAC, 44.1/48 kHz, all tracks enabled.
- Poster frame default 5 s; selectable.
- macOS/tvOS/visionOS landscape only. iMessage-only apps: not available.

| Class | Accepted portrait / landscape |
|---|---|
| iPhone Duo, 6.9", 6.5", 6.1", 5.8" | 886x1920 / 1920x886 |
| 5.5", 4" | 1080x1920 / 1920x1080 |
| 4.7" | 750x1334 / 1334x750 |
| 3.5" | not supported |
| iPad 13", 11", 10.5", 12.9" | 1200x1600 / 1600x1200 (12.9" also 900x1200) |
| iPad 9.7" | 900x1200 / 1200x900 |
| Mac, Apple TV | 1920x1080 |
| Vision Pro | 3840x2160 |

## Creative assets (no alpha)
| Placement | Aspect | Size | Formats | Video |
|---|---|---|---|---|
| Product page header | 21:9 | 3840x1646 | jpg/png | 5-30 s, 30 or 60 fps |
| Product page header alt | 16:9 | 5244x2950 | png only | same |
| Search results | 3:2 | 1920x1280 to 3840x2560 | jpg/png | 5-30 s, 30/60 fps |
| Search results alt | 16:9 | 5244x2950 | png only | same |
| In-App Event card | 16:9 | 1920x1080 to 3840x2160 | jpg/png | 15-30 s |
| In-App Event details | 9:16 | 1080x1920 to 2160x3840 | jpg/png | 15-30 s |
Video formats .mov/.m4v/.mp4; loops continuously; muted in search; muted by default on product page. IAE images max 500 MB. No safe-area numbers on the spec page: use Apple's downloadable templates.

## Copy limits (product page)
| Field | Limit |
|---|---|
| App name | 30 chars |
| Subtitle | 30 chars |
| Promotional text | 170 chars |
| Keywords | 100 chars, comma-separated, no spaces after commas |
| Description / What's New | no limit stated on that page (ASC enforces its own) |

## Review guidelines quick map (section 2.3)
2.3.2 IAP disclosure; 2.3.3 screenshots show app in use; 2.3.4 previews = app screen captures only; 2.3.7 metadata no prices/trademarks/unverifiable claims, name 30 chars; 2.3.8 4+ appropriate, icons consistent; 2.3.9 rights + fictional data; 2.3.10 no other platforms/marketplaces; 2.3.12 What's New; 2.3.14 creative assets: on-brand/app-relevant, no other-app references to mislead, no unverifiable claims, no specific or discounted pricing.
