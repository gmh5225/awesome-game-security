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

Open-source server-side anti-cheat plugin for Minecraft **Paper** and **Purpur** **1.21.x** (Java 21+). Maven/Bukkit API build with configurable heuristics for unauthorized flight, fast experience farming, same-tick totem abuse, suspicious aim target switching, and optional client-brand or plugin-channel signals. Staff receive in-game alerts; LiteBans or AdvancedBan can apply randomized temporary bans; fast-XP suspects may be briefly frozen before kick. Documentation stresses conservative thresholds and that some client-side cheats cannot be proven from server events alone. (source: wiki/sources/descriptions/m3rMAX__HeroAntiCheat.md)

## Detection stack

Movement/combat/economy heuristics (fly, fast XP, totem timing, aim switching); optional plugin-message brand probes; staff alerts plus optional ban-plugin integration.

## Links

- Repo: https://github.com/m3rMAX/HeroAntiCheat

## Related

[[overviews/anti-cheat]] · [[virgola-anticheat]] · [[bs-anticheat]] · [[h-ac]] · [[minecraft-anticheat-list]] · [[detector-operations]]
