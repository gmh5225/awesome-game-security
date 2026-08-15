---
title: DxWrapper
kind: entity
topics: [graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/elishacloud__dxwrapper.md
updated: 2026-08-15
confidence: medium
---

# DxWrapper

C++ DirectX compatibility wrapper DLL that helps older Windows games run on modern Win10/11 by intercepting and remapping graphics and input APIs. Proxy wrappers cover DirectDraw, Direct3D 8/9, DirectInput, DirectSound, and related system libraries with INI-driven configuration. Integrates DDrawCompat, d3d8to9 translation, and Dd7to9 conversion; uses API hooking (Detours and pattern-based hooks) plus GDI and window-procedure fixes for fullscreen and rendering quirks. Optional logging, debug overlays, and resource dumping support diagnosis of legacy rendering issues—aimed at game compatibility, reverse engineering of legacy DirectX titles, and old-game graphics fixes. Catalogued under DirectX Compatibility. (source: wiki/sources/descriptions/elishacloud__dxwrapper.md)

## Links

- Repo: https://github.com/elishacloud/dxwrapper

## Related

[[detours]] · [[directxhook]] · [[d3d9on12]] · [[free-direct]] · [[xidi]] · [[gta4-rtx]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]]
