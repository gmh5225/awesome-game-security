---
title: Anti-Screenshot Capture
kind: concept
topics: [graphics-api, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/graphics-api.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/lainswork__dwm-screen-shot.md
  - wiki/sources/descriptions/j-hc__FlagSecurePatcher.md
  - wiki/sources/descriptions/gmh5225__ScreenShot.md
updated: 2026-08-10
confidence: medium
---

# Anti-Screenshot Capture

How anti-cheat and platform code **captures visible frames** for overlay/ESP detection—and how cheat-side projects attempt to **evade or survive** those captures. Techniques differ by compositor, API, and AC module; verify the active capture path before claiming evasion or detection. (source: wiki/sources/skills/graphics-api.md)

## AC capture paths

| Method | What it sees | Notes |
|--------|--------------|-------|
| `BitBlt` / GDI from game DC | Window client area including many overlays | Common; may miss some DWM-composited layers |
| DXGI Desktop Duplication | Composited desktop/monitor output | Broad; protected content and some hardware planes excepted |
| Present / swap-chain hook | Backbuffer before flip | In-process; pairs with integrity checks on Present |
| `PrintWindow` | Specific HWND subtree | Occlusion and layered-window behavior vary |
| GPU readback | Copy render target → CPU buffer | Staging texture / Map patterns at frame rate |

Scheduled or random-interval captures aim to catch intermittent overlays. README lanes: **Anti Cheat → Screenshot**, **Detection:Overlay**, **Cheat → Anti Screenshot**.

Comparative Windows capture samples such as [[screenshot]] (gmh5225; BitBlt, DXGI Desktop Duplication, PrintWindow, DWM thumbnail; README `[BitBlt]`) help researchers validate which path an AC module uses and what each method reveals about overlays and hardware-accelerated windows. (source: wiki/sources/descriptions/gmh5225__ScreenShot.md)

## Cheat-side evasion (collection patterns)

- **Frame suppression** — detect AC `BitBlt`/`PrintWindow` hooks and skip ImGui draw for the captured frame.
- **Display affinity** — `SetWindowDisplayAffinity(WDA_EXCLUDEFROMCAPTURE)` on external overlay HWND so some capture APIs omit it.
- **DWM composition** — separate surfaces that survive `PrintWindow` but not all BitBlt paths; kernel DC blocking in extreme cases.
- **Hardware overlay planes** — content on dedicated scan-out planes may be absent from software duplication.
- **Off-screen render** — secondary display, capture card, or virtual camera feed outside the game window.
- **Android `FLAG_SECURE`** — apps set `WindowManager.LayoutParams.FLAG_SECURE` to block screenshots/recents; Magisk-lane references such as [[flagsecurepatcher]] document disabling the flag and screenshot listeners for capture research. (source: wiki/sources/descriptions/j-hc__FlagSecurePatcher.md)

Evasion samples in the corpus include [[disablenvidiascreenshot]] (DWM / NVIDIA capture lane), [[dwm-screen-shot]] (DWM; AC/screenshot research for defensive engineers) (source: wiki/sources/descriptions/lainswork__dwm-screen-shot.md), [[wda-monitor-trick]] (monitor-level capture research), and [[eac-overlay]] (alternate surfaces vs overlay monitoring).

## Detection pairing

Screenshot evidence is rarely sufficient alone—correlate with [[present-hook]] integrity, foreign GDI DCs ([[winbo]]), module list (`obs-graphics-hook64.dll` is legitimate OBS, not proof of cheat), and gameplay telemetry ([[ai-aimbot-detection]]).

## Related

[[obs-game-capture]] · [[present-hook]] · [[flagsecurepatcher]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/mobile-security]]
