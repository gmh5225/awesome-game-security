---
title: LarpingAntiCheat (Hyphon)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/realkyx29-design__LarpingAntiCheat.md
updated: 2026-09-03
confidence: medium
---

# LarpingAntiCheat (Hyphon)

Production-ready **Paper 1.21+** Minecraft anti-cheat plugin (**Hyphon**) for custom SMP servers that need reliable cheat detection with very low false positives. Written in **Java 21**, it runs entirely server-side with no client components. Modular **movement**, **combat**, and **world** checks cover fly, speed, reach, kill aura, scaffold, and fast break, using server-authoritative physics snapshots and per-player violation tracking with decay. Includes **honeypot** and **ESP** detection via decoy entities and optional packet-layer fake bases, plus a **capability analyzer** that adapts checks to custom modifiers and enchantments common on modded SMP servers. Intended for server operators and developers who want Paper-native game security without client-side anti-cheat tooling. (source: wiki/sources/descriptions/realkyx29-design__LarpingAntiCheat.md)

## Detection stack

Movement, combat, and world checks (fly, speed, reach, kill aura, scaffold, fast break); server-authoritative physics snapshots; per-player violation tracking with decay; honeypot/ESP decoy entities with optional packet-layer fake bases; capability analyzer for custom enchantments and modifiers on modded SMP.

## Links

- Repo: https://github.com/realkyx29-design/LarpingAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[grim]] · [[bs-anticheat]] · [[inertia]] · [[minecraft-anticheat-list]] · [[uagc]] · [[shard]]
