---
title: Windfall Anti-Cheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/enis1enis2__Windfall-AntiCheat.md
updated: 2026-08-15
confidence: medium
---

# Windfall Anti-Cheat

Enterprise-oriented, packet-based anti-cheat plugin for Minecraft Java servers (Spigot, Paper, Folia, Purpur). Written in Java as a Maven Bukkit plugin; uses **PacketEvents 2** to intercept player traffic and runs dozens of configurable checks spanning combat, movement, packet abuse, and inventory. Includes lag compensation, movement prediction and simulation, adaptive per-player thresholds, Bedrock/Geyser awareness, and a public API for other plugins, plus Discord alerts and Prometheus metrics. A single JAR targets a wide Minecraft version range for server operators needing server-side cheat detection. (source: wiki/sources/descriptions/enis1enis2__Windfall-AntiCheat.md)

## Detection stack

Packet-intercepted combat, movement, packet, and inventory validation with latency-aware movement simulation and adaptive thresholds. Optional Discord webhook alerts and Prometheus metrics; Geyser/Bedrock player awareness. Fabric multiplayer hosts can use the one-to-one port [[windfall-anticheatf]].

## Links

- Repo: https://github.com/enis1enis2/Windfall-AntiCheat
- Fabric port: https://github.com/enis1enis2/WindfallAntiCheatF

## Related

[[windfall-anticheatf]] · [[dakotaac]] · [[avaanticheat]] · [[minecraft-anticheatai]] · [[lenrete-mod]] · [[phantom-client]] · [[local-anticheat-1-8-9]] · [[oomph]] · [[minecpp]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
