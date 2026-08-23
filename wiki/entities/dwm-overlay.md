---
title: dwm-overlay
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/Yukin02__Dwm-Overlay.md
  - wiki/sources/descriptions/LoxTus__dwm-overlay.md
updated: 2026-08-23
confidence: medium
---

# dwm-overlay

Two related Desktop Window Manager overlay projects share this name in the curated list. Both hook DWM composition rendering to draw overlays on top of desktop windows—useful for studying DWM-based overlay rendering beside [[dwm-hook]], [[dwmhook]], and [[present-hook]] paths.

## Yukin02/Dwm-Overlay

Windows **C++ overlay framework** that combines **DWM/DirectX rendering** with an **ImGui** interface. Low-level hook components include assembly stubs for dispatch interception and present-path handling; the codebase provides a minimal base for external overlay drawing, UI widgets, and runtime hook integration. Primary use case is graphics-hooking research and prototyping overlay tooling in game-security contexts. (source: wiki/sources/descriptions/Yukin02__Dwm-Overlay.md)

README category tag: **`[DWM Overlay without modify .text]`** — situates the project in the DWM composition overlay lane, emphasizing hook integration without patching the `.text` section.

## LoxTus/dwm-overlay

Windows **DLL-based DWM overlay proof of concept** that hooks desktop composition rendering. Implemented in **C++** with **MinHook**, **DirectX 11**, and **ImGui**; uses **pattern scanning** to locate the target present routine in **dwmcore**. After hooking, initializes a **D3D11 render path** and draws custom UI content through the swap chain. Mainly useful for graphics hook research, overlay experimentation, and understanding desktop-level rendering interception. (source: wiki/sources/descriptions/LoxTus__dwm-overlay.md)

README category tag: **`[DWM]`** — lighter PoC focus than the Yukin02 assembly-stub framework; pattern-scan + MinHook present-path hook in dwmcore.

## Links

- Repo (Yukin02): https://github.com/Yukin02/Dwm-Overlay
- Repo (LoxTus): https://github.com/LoxTus/dwm-overlay

## Related

[[dwm-hook]] · [[dwmhook]] · [[dwm-dwmdraw]] · [[present-hook]] · [[directxhook]] · [[anti-screenshot-capture]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
