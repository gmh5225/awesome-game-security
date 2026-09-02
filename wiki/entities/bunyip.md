---
title: Bunyip
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/matjam__bunyip.md
updated: 2026-09-02
confidence: medium
---

# Bunyip

Complete **game engine written in Go** (matjam/bunyip) for building real-time and turn-based **2D and 3D games**. Implemented in **pure Go without cgo**, using generated **Vulkan bindings** and native platform layers for windowing, input, and audio on **macOS, Windows, and Linux**. Bundles an entity component system, 2D/3D physics, skeletal animation, physically based rendering, an immediate-mode UI toolkit, spatial audio with tracker module playback, and TCP/TLS and UDP networking. Aimed at simulation-heavy titles such as roguelikes, strategy games, and space games, with headless screenshot testing and extensive developer guides—not a cheat or anti-cheat artifact. (source: wiki/sources/descriptions/matjam__bunyip.md)

Sits in the Game Engine / source lane beside other ECS-centric cross-platform engines such as [[bevy]], [[bloom-engine]], [[nightshade]], and [[raylib]]; cgo-free Vulkan rendering makes it a useful reference for studying portable graphics and engine internals in Go.

## Links

- Repo: https://github.com/matjam/bunyip [Pure Go game engine with Vulkan rendering, ECS, physics, and headless screenshot tests]

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[bevy]] · [[bloom-engine]] · [[nightshade]] · [[raylib]] · [[custom-game-engines]] · [[pilot]]
