---
title: Hyperion Engine
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/HyperionGameTech__HyperionEngine.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: medium
---

# Hyperion Engine

Open-source **C++/C# game engine** distribution (HyperionGameTech) with bundled editor and runtime content. (source: wiki/sources/descriptions/HyperionGameTech__HyperionEngine.md)

## Capabilities

- Cross-platform build scripts; JSON engine and global settings for desktop and mobile; shader and device-tier configuration.
- C++-oriented tree with Clang format and tidy configs. (source: wiki/sources/descriptions/HyperionGameTech__HyperionEngine.md)
- Editor gizmos, scene-entity icons (lighting, cameras, probes, fog, lightmaps, particles), and custom `.hmf` assets (materials, prefabs, mesh data with index/vertex buffers and BVH blobs).
- DirectX 12 and Vulkan rendering, editor tooling, multiplayer samples, and **Glimmer GI** with clustered deferred rendering (per README entry).

## Runtime samples

Bundled runtime content emphasizes **skeletal animation**: named clips and per-bone keyframe tracks for locomotion, combat, and weapon handling—useful when studying how shipped clients structure animation data beside mesh/material prefabs. (source: wiki/sources/descriptions/HyperionGameTech__HyperionEngine.md)

## Use cases

Game developers and engine programmers building or inspecting a full client stack—asset formats, animation tracks, and rendering architecture—in the README **Game Engine → Source** lane beside [[spark-engine]] and [[bevy]], not anti-cheat or cheat artifacts. (source: wiki/sources/descriptions/HyperionGameTech__HyperionEngine.md)

## Links

- Repo: https://github.com/HyperionGameTech/HyperionEngine

## Related

[[spark-engine]] · [[bevy]] · [[doriax]] · [[kotek]] · [[overviews/game-engine]] · [[overviews/graphics-api]]
