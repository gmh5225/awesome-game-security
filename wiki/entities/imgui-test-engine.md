---
title: Dear ImGui Test Engine
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/ocornut__imgui_test_engine.md
updated: 2026-11-06
confidence: medium
---

# Dear ImGui Test Engine

C++ library plus companion tests/examples ([ocornut/imgui_test_engine](https://github.com/ocornut/imgui_test_engine)) for **automating Dear ImGui** and apps that embed it: the runner injects mouse, keyboard, and gamepad input so tests can drive widgets, menus, and navigation while assertions live in your code. It runs in a normal window or **headless** for automated builds, supports fast runs or slower human-like pacing, and can **capture screenshots and video**; an optional performance helper works with ImPlot-style plotting to compare timing across runs. Primary use cases are regression, integration, and smoke tests—and scripted demos or capture pipelines—for ImGui-heavy **debug panels, editors, and in-engine tooling**. (source: wiki/sources/descriptions/ocornut__imgui_test_engine.md)

## Links

- Repo: https://github.com/ocornut/imgui_test_engine

## Related

[[imgui]] · [[overviews/game-engine]] · [[overviews/graphics-api]] · [[ue5-with-dear-imgui]] · [[unreal-imgui-tools]]
