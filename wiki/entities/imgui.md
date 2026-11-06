---
title: Dear ImGui
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/ocornut__imgui.md
  - wiki/sources/descriptions/ocornut__imgui_test_engine.md
updated: 2026-11-06
confidence: medium
---

# Dear ImGui

Bloat-free immediate-mode C++ GUI library (ocornut/imgui): outputs vertex buffers for any graphics API (DirectX 9/10/11/12, OpenGL, Vulkan, Metal) with windows, widgets, plots, tables, docking, and multi-viewport support. Widely used for in-game debug overlays, tool GUIs, and cheat-menu interfaces; aimed at game developers, tool programmers, and anyone needing fast portable in-app UI. (source: wiki/sources/descriptions/ocornut__imgui.md)

Upstream of Present-hook overlay templates ([[dx11-basehook]], [[directxhook]], [[present-hook]]), official extensions ([[imgui-club]]), remote remoting ([[netimgui]]), engine wiring ([[ue5-with-dear-imgui]]), and the companion **automation / test runner** [[imgui-test-engine]] (input-injection GUI tests; headless CI; screenshot/video capture). (source: wiki/sources/descriptions/ocornut__imgui_test_engine.md)

README notes DX11/12 `ResizeBuffers` commit history relevant to swap-chain resize handling.

## Links

- Repo: https://github.com/ocornut/imgui

## Related

[[overviews/graphics-api]] · [[overviews/game-hacking]] · [[imgui-club]] · [[imgui-test-engine]] · [[netimgui]] · [[ue5-with-dear-imgui]] · [[imgui-standalone]] · [[external-imgui-cheat-menu-example-2023]] · [[external-imgui-android]] · [[present-hook]] · [[directxhook]] · [[dx11-basehook]]
