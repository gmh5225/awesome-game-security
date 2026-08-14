---
title: ImOverlay-DX11
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/rabbanyhmm__ImOverlay-DX11.md
updated: 2026-08-14
confidence: medium
---

# ImOverlay-DX11

Lightweight **C++20** framework for hardware-accelerated, transparent desktop overlays and multi-window UI on Windows via **Win32**, **DirectX 11**, and **Dear ImGui**. Ships as two drop-in files that manage layered windows, DXGI swapchains, smart click-through hit testing, native drag handling, and parent-child overlay hierarchies with cascading lifecycle events. Supports topmost floating windows, multi-monitor anchoring, dynamic physical window expansion for popups/menus, and optional antivirus-hardening features such as Control Flow Guard and ASLR. (source: wiki/sources/descriptions/rabbanyhmm__ImOverlay-DX11.md)

Targets developers building game overlays and desktop tools, and researchers studying transparent external overlay rendering relevant to game security and anti-cheat analysis. Sits in the **external layered-window** lane beside GDI/D2D externals—no in-process Present hook—using DX11 compositing over transparent HWNDs instead of [[present-hook]] injection.

## Links

- Repo: https://github.com/rabbanyhmm/ImOverlay-DX11

## Related

[[imgui]] · [[present-hook]] · [[egui-d3d11]] · [[external-imgui-cheat-menu-example-2023]] · [[asdf-overlay]] · [[overlay]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
