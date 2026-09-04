---
title: Corner Culling
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/87andrewh__CornerCulling.md
updated: 2026-09-04
confidence: medium
---

# Corner Culling

**Server-side occlusion-culling system** (87andrewh) designed to **reduce wallhack visibility** in multiplayer shooters. Written primarily in **C++** with **Unreal Engine** project files, it uses **analytical ray casts** rather than coarse visibility approximations. Combines **recent-occluder caching**, **BVH acceleration**, and **latency-aware lookahead checks** to keep culling fast while reducing popping artifacts. Intended for **anti-cheat and game security research** on scalable line-of-sight enforcement. (source: wiki/sources/descriptions/87andrewh__CornerCulling.md)

Complements the author's Source-engine variant [[corner-culling-source-engine]] and behavioral detectors such as [[osanticheat]] by enforcing visibility at the occlusion layer instead of inferring wallhacks from aim or movement statistics alone.

## Links

- Repo: https://github.com/87andrewh/CornerCulling

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[corner-culling-source-engine]] · [[deepaimdetector]] · [[osanticheat]]
