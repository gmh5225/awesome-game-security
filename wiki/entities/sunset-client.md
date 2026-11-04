---
title: Sunset Client
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/PointOfPressure__sunset-client.md
  - wiki/sources/README-categories.md
updated: 2026-11-04
confidence: medium
---

# Sunset Client

**Sunset** (PointOfPressure/sunset-client) is a native **Rust** utility client for **Horizon**, a Rust-based **Minecraft 26.3** rewrite, shipped as a horizon-native mod with extensive mixin hooks. It organizes features into combat, movement, player, render, and world modules—including PvP-oriented kill aura, crystal/anchor aura, scaffold, velocity tweaks, ESP, and a configurable click GUI—using a Meteor Client–inspired architecture. Development uses Horizon’s mixin toolchain, install scripts, Python verification/packaging tools, and documented anticheat sweep matrices comparing module behavior against common server anticheats. Targets players and researchers studying how feature-rich client-side modifications interact with multiplayer server enforcement. (source: wiki/sources/descriptions/PointOfPressure__sunset-client.md)

README category: Cheat / game:minecraft (Horizon).

## Architecture

| Component | Role |
|-----------|------|
| Rust + Horizon mixins | In-process hooks on the Horizon/Minecraft 26.3 rewrite |
| Module taxonomy | Combat, movement, player, render, world feature bundles |
| Click GUI | Configurable in-client module toggles and settings |
| Anticheat matrices | Maintainer docs mapping modules vs common server AC behaviors |

## Anti-cheat interaction

Documented sweep matrices position Sunset as a structured reference for how combat/movement/render modules surface to Paper/Folia/Fabric server plugins—contrasts with JVM attach overlays such as [[nocturne-client]] and Fabric Java clients such as [[vortex-client]]. (source: wiki/sources/descriptions/PointOfPressure__sunset-client.md)

## Links

- Repo: https://github.com/PointOfPressure/sunset-client

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[vortex-client]] · [[nocturne-client]] · [[epsilon]] · [[lenrete-mod]]
