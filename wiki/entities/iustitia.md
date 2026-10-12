---
title: Iustitia
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ThoriaDevelopment__Iustitia.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: medium
---

# Iustitia

Fabric **1.21.11** client-side Minecraft Java mod (ThoriaDevelopment/Iustitia; Kotlin/Gradle; Fabric mixins) that passively models other players from inbound server-rebroadcast packets—no server plugin and no outbound reporting. It runs **36** configurable detection checks with violation-level scoring (reach, kill aura, fly, speed, scaffold, and related combat/movement anomalies spanning legacy 1.8-style and modern 1.21-era patterns), preset moderation profiles, in-game commands, HUD/nametag indicators, and **clip replay** that reconstructs recent motion as in-world ghost models for staff review. Intended for moderators and anticheat researchers who need local inspection and evidence rather than automated kicks or bans. (source: wiki/sources/descriptions/ThoriaDevelopment__Iustitia.md)

## Operations

Local-only staff alerts and replay review—no server enforcement path. Treat detections as client-side heuristics on observed packets, not authoritative server verdicts.

## Positioning

Same **passive client observer** lane as [[rain-injectable]] (1.8.9 injectable Rain rebuild) and freezato/LocalAnticheat-1.8.9-style local chat flags; complements server-side Paper/Fabric plugins such as [[virgola-anticheat]] and [[shieldguard-anticheat]].

## Links

- Repo: https://github.com/ThoriaDevelopment/Iustitia

## Related

[[overviews/anti-cheat]] · [[concepts/detector-operations]] · [[rain-injectable]] · [[minecraft-anticheat-list]] · [[anticheat-qa]]
