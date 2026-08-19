---
title: Dwm-Overlay
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/Yukin02__Dwm-Overlay.md
updated: 2026-08-19
confidence: medium
---

# Dwm-Overlay

Windows **C++ overlay framework** that combines **DWM/DirectX rendering** with an **ImGui** interface. Low-level hook components include assembly stubs for dispatch interception and present-path handling; the codebase provides a minimal base for external overlay drawing, UI widgets, and runtime hook integration. Primary use case is graphics-hooking research and prototyping overlay tooling in game-security contexts. (source: wiki/sources/descriptions/Yukin02__Dwm-Overlay.md)

README category tag: **`[DWM Overlay without modify .text]`** — situates the project in the DWM composition overlay lane beside [[dwm-hook]] and [[dwmhook]], emphasizing hook integration without patching the `.text` section.

## Links

- Repo: https://github.com/Yukin02/Dwm-Overlay

## Related

[[dwm-hook]] · [[dwmhook]] · [[dwm-dwmdraw]] · [[present-hook]] · [[directxhook]] · [[anti-screenshot-capture]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
