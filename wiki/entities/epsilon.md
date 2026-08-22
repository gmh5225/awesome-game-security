---
title: Epsilon
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/NekoyaHouse__Epsilon.md
updated: 2026-08-22
confidence: medium
---

# Epsilon

Modern **multi-loader** Minecraft utility client for **NeoForge** and **Fabric** that exposes configurable gameplay modules through a modular architecture. Written primarily in **Java** with **Gradle Kotlin** build scripts, it hooks the client via **Mixins** and a custom **event bus** to intercept ticks, packets, rendering, and player actions. The codebase ships combat, movement, player automation, and render modules, an extensible **addon system**, **Lua scripting** support, and a **Lumin** / **PrismRHI**-based graphics stack for custom HUD and UI rendering. Aimed at game security researchers and anti-cheat developers studying how advanced Minecraft clients implement packet manipulation, rotation systems, and client-side bypass techniques. (source: wiki/sources/descriptions/NekoyaHouse__Epsilon.md)

## Architecture

| Component | Role |
|-----------|------|
| NeoForge + Fabric loaders | Dual-target multi-loader deployment |
| Mixins + event bus | Bytecode hooks for ticks, packets, rendering, player actions |
| Module system | Combat, movement, player automation, render categories |
| Addon + Lua | Extensible third-party modules and scripting |
| Lumin / PrismRHI | Custom HUD and UI rendering stack |

## Links

- Repo: https://github.com/nekoyahouse/epsilon

## Related

[[lenrete-mod]] · [[phantom-client]] · [[yuri]] · [[seiun-ac]] · [[windfall-anticheatf]] · [[minecraft-anti-cheat]] · [[dakotaac]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
