---
title: AstroX AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Eangly99__AstroX-AntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-08-26
confidence: medium
---

# AstroX AntiCheat

High-performance **GeyserMC extension** anti-cheat for Minecraft Bedrock Edition players. Written in **Java** (Maven); intercepts raw Bedrock **UDP/RakNet** packets at the **Netty channel layer** before Geyser translates them to Java, enabling sub-millisecond detection without main-thread server tick overhead. Heuristic modules cover movement, combat, inventory, and packet validation—reach, hitbox backtracking, flight, autoclicker, device spoofing, and crash-packet firewalling—with Bedrock-native kinematics, input-mode-aware reach limits, latency backtracking, and a leaky-bucket timer to reduce false positives from translation artifacts. Targets GeyserMC server operators needing enterprise-grade Bedrock AC with Discord webhook alerts, admin commands, and configurable violation actions. (source: wiki/sources/descriptions/Eangly99__AstroX-AntiCheat.md)

## Links

- Repo: https://github.com/Eangly99/AstroX-AntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[oomph]] · [[ghost-anticheat]] · [[paradox-anticheat]] · [[minecraft-anticheat-list]]
