---
title: Corner Culling Source Engine
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/87andrewh__CornerCullingSourceEngine.md
updated: 2026-09-04
confidence: medium
---

# Corner Culling Source Engine

**Source engine anti-wallhack extension** (87andrewh) that enforces **strict server-side visibility culling** for competitive multiplayer. Combines a **C++ extension**, **SourceMod** scripts, and **map-side occluder** definitions to control what players can see without trusting client rendering. Emphasizes **ray-cast correctness**, **low frame-time overhead**, and **latency-safe** behavior to avoid visibility popping at normal ping ranges. Aimed at server operators and researchers hardening Source-based games against wallhack-style information leaks. (source: wiki/sources/descriptions/87andrewh__CornerCullingSourceEngine.md)

Complements behavioral SourceMod plugins such as [[little-anti-cheat]] and [[nocheatz-3]] by enforcing line-of-sight at the visibility layer rather than inferring cheats from aim or movement statistics.

## Links

- Repo: https://github.com/87andrewh/CornerCullingSourceEngine

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[corner-culling]] · [[little-anti-cheat]] · [[nocheatz-3]] · [[source-engine]] · [[deepaimdetector]] · [[osanticheat]]
