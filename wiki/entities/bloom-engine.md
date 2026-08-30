---
title: Bloom Engine
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/Bloom-Engine__engine.md
updated: 2026-08-30
confidence: medium
---

# Bloom Engine

**Bloom** (Bloom-Engine/engine) is a TypeScript game engine that compiles games to native binaries and the web through **Perry**, an LLVM-based ahead-of-time TypeScript compiler. It exposes a simple, raylib-inspired function-based API for 2D and 3D games, with the engine core implemented in Rust and rendered through **wgpu** across Metal, DirectX 12, Vulkan, OpenGL, and WebGPU. The stack bundles Jolt Physics, GPU skeletal animation for glTF/GLB models, WGSL shaders, and an npm-packaged TypeScript surface so developers can write one codebase and ship across desktop, mobile, and WASM targets. Aimed at game developers who want native performance and cross-platform deployment while authoring gameplay in TypeScript rather than C++ or a heavyweight editor-centric engine—not a cheat or anti-cheat artifact. (source: wiki/sources/descriptions/Bloom-Engine__engine.md)

Sits in the Game Engine / source lane beside other Rust+wgpu and TypeScript-native stacks such as [[bevy]], [[nightshade]], [[raylib]], and browser engines like [[engine]] (PlayCanvas).

## Links

- Repo: https://github.com/Bloom-Engine/engine [Native TypeScript game engine compiling to Metal, DirectX 12, Vulkan, OpenGL, and WebGPU]

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[bevy]] · [[nightshade]] · [[raylib]] · [[engine]] · [[bgfx]] · [[pilot]] · [[esoterica]]
