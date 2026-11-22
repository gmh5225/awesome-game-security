---
title: NavroProxy
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/nioney1277-lab__NavroProxy.md
  - wiki/sources/README-categories.md
updated: 2026-11-22
confidence: medium
---

# NavroProxy

**NavroProxy** (nioney1277-lab/NavroProxy) is a **MIT-licensed** anti-cheat **proxy** for **Minecraft Bedrock Edition** that terminates player connections in front of a backend server, mirrors world and player state, and validates movement and gameplay packets before they reach the real host. Operators keep the backend on a private listen address while the proxy enforces cheats at the **RakNet** or **NetherNet** protocol layer on **Windows** or **Linux**. (source: wiki/sources/descriptions/nioney1277-lab__NavroProxy.md)

## Implementation

Core stack is **Java 21** with **Gradle**, plus an optional **Go** NetherNet frontend. Bridge plugins integrate with **BDS**, **Geyser/Floodgate**, **Nukkit**, and **PocketMine-MP**.

## Detection

Ships **22+** packet and prediction checks across movement, sprint, timer, placement, elytra, and bad-packet families, with configurable tolerances and **violation-based punishments** via YAML. Operating modes include live **detect** enforcement or passive **inspect** protocol analysis.

## Links

- Repo: https://github.com/nioney1277-lab/NavroProxy

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[oomph]] · [[astrox-anticheat]] · [[bedrockguard]] · [[ghost-anticheat]] · [[endstone-paradox]] · [[minecraft-anticheat-list]]