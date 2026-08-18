---
title: Yuri
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/unleg1t__Yuri.md
updated: 2026-08-18
confidence: medium
---

# Yuri

Open-source **Minecraft 1.8.9** **MCP**-based hacked client built with **Java** and **Gradle**. Ships a bundled **Java 8** launch environment, complete **1.8** game assets (resource index, blockstates, models, shaders, textures, object storage), and a cached player-skins directory under its launch folder—typical of MCP mod client layouts. Includes bypass modules targeting **Watchdog**, **Polar**, and **Grim** server anti-cheats on legacy **1.8.x** multiplayer networks. Aimed at game security researchers studying pure-Java cheat client architecture, MCP modification patterns, and how server-side Java AC plugins detect combat/movement cheats. (source: wiki/sources/descriptions/unleg1t__Yuri.md)

## Architecture

- **MCP client** — Gradle-built Java mod with standard wrapper tooling and full bundled runtime layout.
- **Assets** — complete 1.8 resource tree plus launch-folder skin cache for offline-ready client study.
- **Bypass modules** — Watchdog / Polar / Grim evasion hooks for Hypixel-era and modern Java-server AC comparison.

Complements native JVM-injection clients such as [[phantom-client]], passive Forge monitors such as [[local-anticheat-1-8-9]], Fabric clients such as [[lenrete-mod]], and server-side plugins such as [[windfall-anticheat]], [[dakotaac]], and [[minecraft-anticheatai]] in the Minecraft game-security lane.

## Links

- Repo: https://github.com/unleg1t/Yuri

## Related

[[phantom-client]] · [[local-anticheat-1-8-9]] · [[lenrete-mod]] · [[windfall-anticheat]] · [[dakotaac]] · [[minecraft-anticheatai]] · [[jaranalyzer]] · [[minecpp]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
