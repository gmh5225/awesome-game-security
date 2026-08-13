---
title: External Imgui Cheat Menu Example 2023
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__External-imgui-Cheat-Menu-Example-2023.md
updated: 2026-08-13
confidence: medium
---

# External Imgui Cheat Menu Example 2023

Template for building **external cheat menus** with **Dear ImGui** using **SDL** and **OpenGL** backends (gmh5225). Hooks **`SDL_GL_SwapWindow`** to draw an overlay in the game's OpenGL swap path, with explicit **GL context save/restore** so ImGui rendering does not corrupt the target context or cause flickering artifacts. README tag: `[External Imgui Menu]`. (source: wiki/sources/descriptions/gmh5225__External-imgui-Cheat-Menu-Example-2023.md)

Useful as a starter for SDL/OpenGL titles where an external process injects or hooks the swap function rather than using a separate layered HWND or a DXGI Present vtable hook.

## Links

- Repo: https://github.com/gmh5225/External-imgui-Cheat-Menu-Example-2023

## Related

[[imgui]] · [[d3dhook-imgui]] · [[present-hook]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
