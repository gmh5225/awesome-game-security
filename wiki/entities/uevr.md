---
title: UEVR
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/praydog__UEVR.md
updated: 2026-07-25
confidence: medium
---

# UEVR

Universal Unreal Engine VR injection mod (praydog) that adds 6DOF VR to virtually any UE4/UE5 title (README: 4.8–5.4). Hooks the engine render pipeline for stereoscopic rendering, OpenXR/OpenVR head tracking, motion-controller input, and roomscale movement without per-game patches. C++ injector locates engine internals at runtime via UE reflection and pattern scanning—useful for UE researchers studying inject / render-hook / reflection surfaces on flat-screen games. (source: wiki/sources/descriptions/praydog__UEVR.md)

Complements Unreal explorer/SDK tooling ([[unrealengine4-swissknife]], [[patternsleuth]], [[luagenny]]) and stereo/DX tooling such as [[3d9]] on the graphics side; Unity VR samples ([[the-seed-link-future]]) are the parallel managed-engine lane.

## Links

- Repo: https://github.com/praydog/UEVR (README: Universal Unreal Engine VR Mod (4.8 - 5.4))

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[present-hook]] · [[3d9]] · [[luagenny]] · [[patternsleuth]] · [[unrealengine4-swissknife]] · [[ue5-with-dear-imgui]] · [[the-seed-link-future]]
