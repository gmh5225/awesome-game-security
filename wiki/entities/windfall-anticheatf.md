---
title: Windfall AntiCheat F
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/enis1enis2__WindfallAntiCheatF.md
updated: 2026-08-15
confidence: medium
---

# Windfall AntiCheat F

Server-side Fabric mod for Minecraft **1.21.5+** that detects cheating on Fabric multiplayer servers. Written in Java with Fabric Loader, Fabric API, Mixins, and Brigadier commands; intercepts packets and runs dozens of combat, movement, packet, and inventory checks. Ported one-to-one from the Spigot/Paper [Windfall Anti-Cheat](https://github.com/enis1enis2/Windfall-AntiCheat). (source: wiki/sources/descriptions/enis1enis2__WindfallAntiCheatF.md)

## Detection stack

Vanilla-accurate physics prediction engine with latency compensation and simulation, adaptive per-player thresholds, and a severity-based punishment system. Targets common hacks such as KillAura, reach, flight, speed, scaffold, and malformed packets while aiming for low false positives on modern Fabric hosts. Optional Discord webhook alerts and Prometheus metrics; Geyser/Bedrock compatibility.

## Links

- Repo: https://github.com/enis1enis2/WindfallAntiCheatF
- Spigot/Paper upstream: https://github.com/enis1enis2/Windfall-AntiCheat

## Related

[[dakotaac]] · [[avaanticheat]] · [[minecraft-anticheatai]] · [[lenrete-mod]] · [[phantom-client]] · [[local-anticheat-1-8-9]] · [[oomph]] · [[minecpp]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
