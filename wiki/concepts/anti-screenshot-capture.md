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
  - wiki/sources/descriptions/g8tsz__deadlock-anti-cheat.md
  - wiki/sources/descriptions/bmharper__WindowsDesktopDuplicationSample.md
  - wiki/sources/descriptions/bavulapati__DXGICaptureApplication.md
  - wiki/sources/descriptions/Rick-laboratory__Windows-Screenshotcapture-DirectX.md
  - wiki/sources/descriptions/Mes2d__Screenshot-Detection-Bypass.md
  - wiki/sources/descriptions/KANKOSHEV__NoScreen.md
  - wiki/sources/descriptions/GuidoBartoli__sherloq.md
updated: 2026-08-25
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

Comparative Windows capture samples such as [[screenshot]] (gmh5225; BitBlt, DXGI Desktop Duplication, PrintWindow, DWM thumbnail; README `[BitBlt]`) help researchers validate which path an AC module uses and what each method reveals about overlays and hardware-accelerated windows. (source: wiki/sources/descriptions/gmh5225__ScreenShot.md) Educational DXGI Output Duplication samples such as [[windows-desktop-duplication-sample]] (bmharper; C++; frame acquire, cursor overlay, dirty/moved regions; README `[DXGI]`) document compositor-side DDA capture for screenshot and remote-desktop tooling developers. (source: wiki/sources/descriptions/bmharper__WindowsDesktopDuplicationSample.md) Desktop capture tooling such as [[dxgicaptureapplication]] (bavulapati; C/C++; shader-centric desktop capture; README `[Capture Desktop]`; anti-cheat / screenshot lane) complements DDA samples for defensive capture pipeline study. (source: wiki/sources/descriptions/bavulapati__DXGICaptureApplication.md) Minimal DX9 front-buffer readback examples such as [[windows-screenshotcapture-directx]] (Rick-laboratory; D3D9 `GetFrontBufferData` → system-memory copy + WIC PNG encode; README `[DX9]`) illustrate in-process GPU readback beside compositor-side DDA paths. (source: wiki/sources/descriptions/Rick-laboratory__Windows-Screenshotcapture-DirectX.md) Title-specific session AC such as [[deadlock-anti-cheat]] (UrnIt; periodic PNG captures of the game window bundled with process/key/hardware telemetry for staff review; Anti Cheat → Screenshot) illustrates scheduled client-side evidence collection rather than hook-based Present interception. (source: wiki/sources/descriptions/g8tsz__deadlock-anti-cheat.md)

## Cheat-side evasion (collection patterns)

- **Frame suppression** — detect AC `BitBlt`/`PrintWindow` hooks and skip ImGui draw for the captured frame.
- **GDI capture hook** — hook `BitBlt` in gdi32 so AC screenshot pipelines receive a pre-stored clean frame instead of the live overlay-modified client area; educational PoC [[screenshot-detection-bypass]] (Mes2d; C++; class-based hook + settings; README `[BitBlt]`). (source: wiki/sources/descriptions/Mes2d__Screenshot-Detection-Bypass.md)
- **Display affinity** — `SetWindowDisplayAffinity(WDA_EXCLUDEFROMCAPTURE)` on external overlay HWND so some capture APIs omit it. Kernel-assisted window protection such as [[noscreen]] (KANKOSHEV; custom driver + device interface; display-affinity-like anti-capture without direct target process memory modification; reduced user-mode detection surface; README Hide Window) extends that lane below user-mode WDA calls. (source: wiki/sources/descriptions/KANKOSHEV__NoScreen.md)
- **DWM composition** — separate surfaces that survive `PrintWindow` but not all BitBlt paths; kernel DC blocking in extreme cases.
- **Hardware overlay planes** — content on dedicated scan-out planes may be absent from software duplication.
- **Off-screen render** — secondary display, capture card, or virtual camera feed outside the game window.
- **Android `FLAG_SECURE`** — apps set `WindowManager.LayoutParams.FLAG_SECURE` to block screenshots/recents; Magisk-lane references such as [[flagsecurepatcher]] document disabling the flag and screenshot listeners for capture research. (source: wiki/sources/descriptions/j-hc__FlagSecurePatcher.md)

Evasion samples in the corpus include [[disablenvidiascreenshot]] (DWM / NVIDIA capture lane), [[dwm-screen-shot]] (DWM; AC/screenshot research for defensive engineers) (source: wiki/sources/descriptions/lainswork__dwm-screen-shot.md), [[wda-monitor-trick]] (monitor-level capture research), and [[eac-overlay]] (alternate surfaces vs overlay monitoring).

## Detection pairing

Screenshot evidence is rarely sufficient alone—correlate with [[present-hook]] integrity, foreign GDI DCs ([[winbo]]), module list (`obs-graphics-hook64.dll` is legitimate OBS, not proof of cheat), and gameplay telemetry ([[ai-aimbot-detection]]). When reviewing player-submitted or AC-captured PNG/JPEG frames, digital image forensics tooling such as [[sherloq]] (GuidoBartoli; Python GUI; ELA, EXIF metadata, frequency/gradient/histogram analysis, cloning detection, TruFor neural detector; screenshot tampering detection for AC analysts) helps assess authenticity before treating pixels as proof. (source: wiki/sources/descriptions/GuidoBartoli__sherloq.md)

## Related

[[obs-game-capture]] · [[present-hook]] · [[flagsecurepatcher]] · [[sherloq]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/mobile-security]]
