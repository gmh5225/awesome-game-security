---
title: LLGL
kind: entity
topics: [graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/LukasBanana__LLGL.md
updated: 2026-10-17
confidence: medium
---

# LLGL

LLGL (Low Level Graphics Library) is a thin C++11 abstraction that exposes one rendering API over Direct3D 11/12, Vulkan, OpenGL, OpenGLES 3, WebGL, and Metal on desktop, mobile, UWP, and WebAssembly. A backend-agnostic frontend loads pluggable renderer modules at runtime; optional OpenXR integration and generated C99, C#, and Go bindings sit on the core C++ interface. CMake builds the tree, and extensive C++ examples cover pipelines, resource binding, compute, tessellation, and shadow mapping. (source: wiki/sources/descriptions/LukasBanana__LLGL.md)

Useful for game developers and security researchers who need a portable reference for how applications structure GPU work, swap chains, and shader pipelines when studying game rendering internals, graphics hooks, or presentation-path behavior. Sits in the Renderer / multi-API graphics-library lane beside [[bgfx]] and [[diligent-engine]]—not a cheat or anti-cheat artifact.

## Links

- Repo: https://github.com/LukasBanana/LLGL (README: thin C++ abstraction over OpenGL, D3D11/12, Vulkan, and Metal with C/C#/Go wrappers)

## Related

[[overviews/graphics-api]] · [[overviews/game-engine]] · [[bgfx]] · [[diligent-engine]] · [[horizon-engine]] · [[present-hook]] · [[draw-call-hook]]
