---
title: dwmhook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/mfxiaosheng__dwmhook.md
  - wiki/sources/descriptions/gmh5225__dwmhook.md
updated: 2026-08-09
confidence: medium
---

# dwmhook

Two related Desktop Window Manager overlay projects share this name in the curated list. Both hook DWM's rendering pipeline to draw overlays on top of any window without creating a separate overlay HWND—useful for studying DWM-based overlay rendering beside [[dwm-hook]] and [[present-hook]] paths.

## mfxiaosheng/dwmhook

Desktop Window Manager **overlay rendering framework** that hooks DWM's DirectX 11 vtable to draw ImGui-based overlays on top of all windows. Uses reflective DLL injection, MinHook/PolyHook2 for vtable interception, FW1FontWrapper for DirectWrite text rendering, and PDB symbol resolution (via DIA SDK) to locate internal DWM compositor functions. (source: wiki/sources/descriptions/mfxiaosheng__dwmhook.md)

## gmh5225/dwmhook

Windows DWM hooking **proof of concept** that intercepts DWM composition functions to inject draw calls into the desktop compositor. Renders overlays that appear above any window without a separate overlay window—aimed at game-security researchers studying DWM-based overlay rendering techniques. (source: wiki/sources/descriptions/gmh5225__dwmhook.md)

Lighter PoC focus than the mfxiaosheng vtable/ImGui framework; sits in the same DWM composition overlay lane as [[dwm-hook]] and kernel composition research such as [[double-callback]].

## Links

- Repo (mfxiaosheng): https://github.com/mfxiaosheng/dwmhook
- Repo (gmh5225): https://github.com/gmh5225/dwmhook

## Related

[[dwm-hook]] · [[present-hook]] · [[directxhook]] · [[disablenvidiascreenshot]] · [[double-callback]] · [[dxgkrnl-hook]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
