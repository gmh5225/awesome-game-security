---
title: Direct3DHook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/justinstenning__Direct3DHook.md
updated: 2026-08-02
confidence: medium
---

# Direct3DHook

C#/.NET library that injects into a target Windows process and hooks its Direct3D rendering path for **screenshot capture** and **in-game overlays**. Uses EasyHook for remote DLL injection and IPC; SharpDX bindings cover Direct3D 9, 10, 10.1, and 11 with optional auto-detection of which API the process has loaded. Host applications communicate with the injected Capture assembly through a remoting `CaptureInterface` to request frames, display text or image overlays, and receive capture results. Includes a `TestScreenshot` sample for end-to-end injection and capture against a live Direct3D window—aimed at game security researchers, reverse engineers, and tool authors needing in-process graphics capture or overlay hooks. (source: wiki/sources/descriptions/justinstenning__Direct3DHook.md)

## Links

- Repo: https://github.com/justinstenning/Direct3DHook

## Related

[[present-hook]] · [[directxhook]] · [[hydrahook]] · [[screencapture]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
