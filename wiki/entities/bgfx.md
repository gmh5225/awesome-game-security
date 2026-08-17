---
title: bgfx
kind: entity
topics: [graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/bkaradzic__bgfx.md
updated: 2026-08-17
confidence: medium
---

# bgfx

Cross-platform C/C++ rendering library providing a thin abstraction over Direct3D 9/11/12, Metal, OpenGL, OpenGL ES, Vulkan, and WebGPU. Offers a unified API for draw-call submission, shader management, texture handling, compute dispatches, and render-state management so applications can target major platforms from one codebase. Includes **shaderc**, a GLSL-based shader cross-compiler. Aimed at game-engine developers and graphics programmers needing portable low-level rendering. (source: wiki/sources/descriptions/bkaradzic__bgfx.md)

Sits in the Renderer / multi-API graphics-library lane—the upstream BGFX abstraction used by engine backends such as [[gplayengine]] and [[kotek]], not a cheat or anti-cheat artifact.

## Links

- Repo: https://github.com/bkaradzic/bgfx (README: [Rendering library])

## Related

[[overviews/graphics-api]] · [[overviews/game-engine]] · [[gplayengine]] · [[kotek]] · [[raylib]] · [[present-hook]]
