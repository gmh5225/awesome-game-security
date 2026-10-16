---
title: FoxAddition
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/IDCTeam-Group__FoxAddition.md
updated: 2026-10-16
confidence: medium
---

# FoxAddition

**FoxAddition** (IDCTeam-Group/FoxAddition) is an open-source **Spigot**, **Paper**, and **Folia** Minecraft server anti-cheat plugin written in **Java** and built with **Gradle**. It uses **PacketEvents** for low-level packet inspection alongside configurable checks for invalid packets, movement and abilities, block placement, keep-alives, and world exploits such as break aura and nuker. The project targets multiplayer administrators and anti-cheat developers who want lightweight protection spanning roughly **1.7.2** through current releases. (source: wiki/sources/descriptions/IDCTeam-Group__FoxAddition.md)

## Detection

Packet-driven and event-style checks cover common client-side hacks—movement/ability abuse, suspicious block interaction, keep-alive anomalies, and fast-break/nuker patterns—with tunable per-check behavior. (source: wiki/sources/descriptions/IDCTeam-Group__FoxAddition.md)

## Operations

Server operators get **per-world toggles**, a **violation-level** escalation model, and **file-based alert logging** for staff review. Optional integrations include **GeyserMC** and **Floodgate** for Bedrock players, plus hooks for **DiscordSRV**, **ProtocolLib**, and related plugins when present. (source: wiki/sources/descriptions/IDCTeam-Group__FoxAddition.md)

## Positioning

Version-spanning Paper/Folia PacketEvents AC beside modular heuristics such as [[bs-anticheat]] and [[h-ac]], fly-focused [[nofly]], remote-engine telemetry such as [[thorium-minecraft-plugin]], and Bedrock-aware plugins such as [[vanticheat]]. Operational patterns: [[detector-operations]]. Catalog: [[minecraft-anticheat-list]].

## Links

- Repo: https://github.com/IDCTeam-Group/FoxAddition

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[bs-anticheat]] · [[h-ac]] · [[nofly]] · [[thorium-minecraft-plugin]] · [[vanticheat]] · [[detector-operations]] · [[minecraft-anticheat-list]]
