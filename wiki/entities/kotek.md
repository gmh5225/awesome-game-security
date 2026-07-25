---
title: Kotek
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/wh1t3lord__kotek.md
updated: 2026-07-24
confidence: medium
---

# Kotek

Modular C/C++20 core framework for a three-layer game-engine stack: replaceable services (math, containers, logging, filesystem, windowing, UI, ECS, rendering) behind stable `ktkI*` interfaces registered through a main manager. Backends are CMake-swappable or runtime-overridable via plugins—e.g. GLM/DirectXMath, GLFW, Dear ImGui, RmlUi, CEF, pico_ecs, bgfx, plus no-dependency own implementations. Builds target Windows first with Linux OS abstractions; static, shared, and explicit plugin linkage. (source: wiki/sources/descriptions/wh1t3lord__kotek.md)

Sits in the Game Engine / multi-API source lane (OpenGL ES, Vulkan, DirectX, BGFX)—a customizable C++ runtime core for engine/app development and graphics-pipeline study, not a cheat or anti-cheat artifact.

## Links

- Repo: https://github.com/wh1t3lord/kotek (README tag: [Modular C++20 game/application framework with OpenGL ES, Vulkan, DirectX, and BGFX backends])

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[wind-effects]] · [[wickedengine]] · [[urho3d]] · [[island]]
