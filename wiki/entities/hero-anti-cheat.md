---
title: HeroAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/m3rMAX__HeroAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-18
confidence: medium
---

# hero-anti-cheat

Open-source server-side anti-cheat plugin for Minecraft **Paper** and **Purpur** **1.21.x** (Java 21+). Implemented in Java with the Bukkit/Paper API and Maven; CI publishes build artifacts. Configurable heuristics flag unauthorized flight, fast experience farming, same-tick totem abuse, suspicious aim target switching, and optional client-brand or plugin-channel signals. Staff receive in-game alerts; when **LiteBans** or **AdvancedBan** is present, violators can receive randomized temporary bans; fast-XP suspects are briefly frozen before kick. Targets server operators who want a lightweight cheat deterrent with conservative thresholds and explicit warnings that some cheats cannot be proven from server events alone. (source: wiki/sources/descriptions/m3rMAX__HeroAntiCheat.md)

## Detection stack

Movement/combat/economy heuristics (fly, fast XP, totem timing, aim switching); optional plugin-message brand or plugin-channel probes; in-game staff alerts; optional LiteBans/AdvancedBan integration with randomized temp-ban durations; fast-XP freeze-then-kick path.

## Links

- Repo: https://github.com/m3rMAX/HeroAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[virgola-anticheat]] · [[bs-anticheat]] · [[h-ac]] · [[minecraft-anticheat-list]] · [[detector-operations]]
