---
title: dwmhook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/mfxiaosheng__dwmhook.md
updated: 2026-07-30
confidence: medium
---

# dwmhook

Desktop Window Manager **overlay rendering framework** that hooks DWM's DirectX 11 vtable to draw ImGui-based overlays on top of all windows. Uses reflective DLL injection, MinHook/PolyHook2 for vtable interception, FW1FontWrapper for DirectWrite text rendering, and PDB symbol resolution (via DIA SDK) to locate internal DWM compositor functions. (source: wiki/sources/descriptions/mfxiaosheng__dwmhook.md)

Sits in the DWM VFTable overlay lane—composition-level draw outside a single game swap-chain Present—alongside simpler DWM hook samples such as [[dwm-hook]] and kernel composition research such as [[double-callback]].

## Links

- Repo: https://github.com/mfxiaosheng/dwmhook

## Related

[[dwm-hook]] · [[present-hook]] · [[directxhook]] · [[disablenvidiascreenshot]] · [[double-callback]] · [[dxgkrnl-hook]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
