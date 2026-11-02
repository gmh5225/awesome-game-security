---
title: Treb3rAntiCheater
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Treb3r__Treb3rAntiCheater.md
updated: 2026-11-02
confidence: medium
---

# Treb3rAntiCheater

**Treb3rAntiCheater** (Treb3r/Treb3rAntiCheater) is a high-performance **Paper 1.21.x** Minecraft server plugin that bundles server-side mitigation for **wallhack (anti-ESP)**, **x-ray**, and **freecam** in one Java package for survival multiplayer operators. (source: wiki/sources/descriptions/Treb3r__Treb3rAntiCheater.md)

## Anti-ESP (occlusion)

Uses **voxel ray marching** and multi-tier perimeter sampling to hide entities behind walls from clients that should not see them, while preserving vanilla nametags through **TextDisplay** when appropriate.

## Anti-xray

Packet-level engine injects into Paper’s chunk packet controller via **reflection** to obfuscate or mask underground ores in outgoing chunk packets **without** editing `paper-world.yml`. Supports in-memory **Engine Modes 1–2** per the README entry.

## Anti-freecam

Periodically forces client camera sync with **NMS packets** and blocks interactions through walls beyond configured reach.

## Links

- Repo: https://github.com/Treb3r/Treb3rAntiCheater

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[shieldguard-anticheat]] · [[petal-anti-freecam]] · [[xray-anticheat]] · [[minecraft-anticheat-list]]
