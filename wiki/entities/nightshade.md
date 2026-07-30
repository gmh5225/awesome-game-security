---
title: Nightshade
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/matthewjberger__nightshade.md
updated: 2026-07-30
confidence: medium
---

# Nightshade

Rust game engine for 3D and 2D titles built around a plugin-composed App model and staged system schedules. Ships a custom dynamic ECS, a wgpu-based PBR renderer, and a high-level `nightshade-api` facade with lower-level crates for rendering, audio, physics, navmesh, UI, OpenXR, and Steam. Games assemble from capability plugins, load glTF scenes, and target desktop or the web via WASM tooling such as Trunk. An included editor and Rhai scripting support interactive scene authoring and prototyping. (source: wiki/sources/descriptions/matthewjberger__nightshade.md)

Primary use case is game development and engine experimentation—not anti-cheat or reverse engineering. Sits beside other Rust engine libraries ([[macroquad]], [[raylib]]) as a data-oriented ECS + wgpu study surface.

## Links

- Repo: https://github.com/matthewjberger/nightshade (README tag: [Rust data-oriented game engine with custom ECS and wgpu PBR renderer (native/web/VR)])

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[macroquad]] · [[zig-gamedev]] · [[raylib]] · [[wickedengine]]
