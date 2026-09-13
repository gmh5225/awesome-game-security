---
title: Traktor
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/apistol78__traktor.md
  - wiki/sources/README-categories.md
updated: 2026-09-13
confidence: medium
---

# Traktor

Modular cross-platform C++ game engine with integrated editor, runtime, and build toolchain for creating and shipping games. Rendering backends include DirectX 11, Vulkan, and Metal; a node-based HLSL/GLSL shader graph drives materials; Lua scripting includes debugging and profiling; physics uses Bullet and Jolt; animation covers cloth and ragdoll; AI navigation meshes, peer-to-peer networking, and state replication support multiplayer workflows. An Avalanche asset server and Model Context Protocol tooling in the editor extend content and agent-driven workflows. Targets Linux, Windows, macOS, Raspberry Pi, Android, and iOS; README lists shipped commercial titles on Steam, PSN, iOS, and macOS. (source: wiki/sources/descriptions/apistol78__traktor.md)

Fits the README **Game Engine → Source** lane for engine programmers, graphics researchers, and security analysts who need full source access to a modern multi-backend engine with editor MCP integration—complementary to lightweight Vulkan study engines such as [[ursus]] and editor-centric stacks such as [[godot]].

## Security research angles

Full source access supports studying boundaries that fail independently in shipped titles:

- **Multi-backend rendering** — DirectX 11, Vulkan, and Metal backends plus a node-based HLSL/GLSL shader graph expose how the same material compiles and presents per API; pair with [[frame-observation-boundary]] when comparing capture or hook evidence across backends.
- **Scripting and replication** — Lua runtime (with debugger/profiler hooks) and peer-to-peer state replication are separate trust surfaces from native engine modules; map findings to [[engine-trust-boundaries]] before attributing multiplayer behavior.
- **Editor MCP tooling** — Model Context Protocol integration in the editor is an agent-driven workflow surface distinct from shipped player builds; treat editor automation as its own privilege boundary.
- **Shipped-title baseline** — Commercial releases on Steam, PSN, iOS, and macOS provide production references against the open engine tree for diffing replication, asset pipeline (Avalanche server), and platform-specific backends.

(source: wiki/sources/descriptions/apistol78__traktor.md)

## Links

- Repo: https://github.com/apistol78/traktor

## Related

[[ursus]] · [[lina-engine]] · [[godot]] · [[methanekit]] · [[engine-trust-boundaries]] · [[engine-artifact-selection]] · [[overviews/game-engine]] · [[overviews/graphics-api]]
