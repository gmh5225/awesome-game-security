---
title: kiero2
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/kirchesz__kiero2.md
updated: 2026-08-21
confidence: medium
---

# kiero2

**kiero v2** — C++ runtime locator for DirectX 9–12, OpenGL, and Vulkan graphics API method addresses. Bring-your-own hooking: resolves vtable/function pointers at runtime but does not install hooks itself. CMake `FetchContent` integration; OpenGL and Vulkan paths are cross-platform (Windows, Linux, macOS). Aimed at graphics programmers and Windows game tooling developers bootstrapping multi-API Present/swap hooks in the DirectX / hook lane. (source: wiki/sources/descriptions/kirchesz__kiero2.md)

Successor to the original Windows-only [[kiero]] (Rebzzel/kiero; universal D3D9–12/GL/Vulkan hooking with MinHook method-table detours and sample ImGui overlays; x86/x64). README Vulkan lane lists kiero2 beside Pascal/OOP Vulkan wrappers as a cross-platform runtime API locator.

## Links

- Repo: https://github.com/kirchesz/kiero2

## Related

[[present-hook]] · [[kiero]] · [[d3dhook-imgui]] · [[hydrahook]] · [[imgui]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
