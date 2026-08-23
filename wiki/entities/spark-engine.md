---
title: SparkEngine
kind: entity
topics: [game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/Krilliac__SparkEngine.md
updated: 2026-08-23
confidence: medium
---

# SparkEngine

**SparkEngine** (Krilliac/SparkEngine) is a cross-platform **C++23 3D game engine** with a full runtime, editor, build tools, and sample game modules for ARPG, MMO, and MMOFPS genres. Rendering uses modern backends (DirectX 12, Vulkan, Metal) with HLSL/GLSL shader pipelines, PBR, and ray-tracing paths. Core systems include Jolt Physics, ECS, AI navigation, and AngelScript plus visual scripting. (source: wiki/sources/descriptions/Krilliac__SparkEngine.md)

Networking covers dedicated servers, replication, client prediction, lag compensation, encryption, and packet validation, with security-oriented pieces such as **memory integrity checks**. Aimed at game developers building networked titles and researchers studying engine-level multiplayer and client-integrity design — in the Game Engine / source lane, not a cheat or standalone anti-cheat product. (source: wiki/sources/descriptions/Krilliac__SparkEngine.md)

Sits beside other full-stack OSS engines with integrated netcode such as [[lightyear]] (Bevy netcode library) and [[game-networking-resources]] (curated netcode knowledge base), and multi-API C++ engine sources such as [[methanekit]] and [[l-spiro-engine-2022]].

## Links

- Repo: https://github.com/Krilliac/SparkEngine (README: Open-source C++23 3D engine with DirectX 12/Vulkan RHI, ECS, Jolt Physics, and ImGui editor)

## Related

[[overviews/game-engine]] · [[overviews/anti-cheat]] · [[lightyear]] · [[game-networking-resources]] · [[methanekit]] · [[l-spiro-engine-2022]] · [[hazel]]
