---
title: Pyramid Engine
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/RuqoomTech__Pyramid-Engine.md
updated: 2026-08-21
confidence: medium
---

# Pyramid Engine

Pre-alpha C++17 game engine for Windows prototyping. Provides a Win32/OpenGL application loop, graphics device, scene system, and modular support libraries. Targets OpenGL 3.3 core with GLSL 3.30 shaders; includes forward and deferred render passes, shadow mapping, frustum culling with an octree, entity-component scenes with serialization, and resource caches for meshes, shaders, textures, and materials. Standalone packages cover SIMD math, input actions, PNG/JPEG loading, OBJ/MTL import, TrueType/font tooling, text layout, and UI. Built with CMake via MSYS2 MinGW-w64 (Clang also validated); near-term focus is an RTS-style vertical slice. Includes tests and CI. (source: wiki/sources/descriptions/RuqoomTech__Pyramid-Engine.md)

Sits in the Game Engine / OpenGL source lane—an educational engine codebase for studying render pipelines and ECS architecture, not a cheat or anti-cheat artifact.

## Links

- Repo: https://github.com/RuqoomTech/Pyramid-Engine

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[cpp-game-engine-book]] · [[exengine]] · [[joshoengine-native]] · [[gltut]] · [[game-engine-from-scratch]]
