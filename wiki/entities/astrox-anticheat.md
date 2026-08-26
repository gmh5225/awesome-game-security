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

High-performance **GeyserMC extension** anti-cheat for Minecraft Bedrock Edition players. Written in **Java** (Maven); intercepts raw Bedrock **UDP/RakNet** packets at the **Netty channel layer** before Geyser translates them to Java, enabling sub-millisecond detection without main-thread server tick overhead. Targets GeyserMC server operators who need enterprise-grade Bedrock AC with Discord webhook alerts, admin commands, and configurable violation actions. (source: wiki/sources/descriptions/Eangly99__AstroX-AntiCheat.md)

## Architecture

Pre-translation packet hook on the GeyserMC Netty pipeline; checks run off the main server tick. Uses Bedrock-native kinematics, input-mode-aware reach limits, latency backtracking, and a leaky-bucket timer to reduce false positives from Geyser translation artifacts.

## Detection stack

Movement, combat, inventory, and packet-validation heuristic modules: reach, hitbox backtracking, flight, autoclicker, device spoofing, and crash-packet firewalling.

## Links

- Repo: https://github.com/Eangly99/AstroX-AntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[oomph]] · [[ghost-anticheat]] · [[paradox-anticheat]] · [[windfall-anticheat]] · [[minecraft-anticheat-list]]
