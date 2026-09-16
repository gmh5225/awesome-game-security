---
title: Thorium Minecraft Plugin
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ThoriumAC__Thorium-Minecraft-Plugin.md
  - wiki/sources/README-categories.md
updated: 2026-09-16
confidence: medium
---

# Thorium Minecraft Plugin

Open-source server-side client for the Thorium Minecraft anti-cheat engine. Written in Java for Bukkit, Spigot, Paper, and Folia, it captures movement, combat, block interaction, transaction markers, and nearby world geometry from packets the server already receives—no client mod, memory inspection, or player-machine access. Uses PacketEvents, Java-WebSocket, and Protocol Buffers to authenticate and stream telemetry to the remote Thorium detection engine, then optionally enforces returned verdicts (staff alerts, warnings, kicks, bans). Detection logic runs in the closed-source Thorium engine; the open plugin lets operators audit outbound data and punishment wiring. Targets Minecraft server administrators needing server-side AC across versions 1.8 through current releases. (source: wiki/sources/descriptions/ThoriumAC__Thorium-Minecraft-Plugin.md)

## Detection stack

Server-side packet telemetry (movement, combat, block interaction, transactions, nearby geometry); WebSocket + protobuf engine channel; optional verdict enforcement (alerts, warnings, kicks, bans); closed-source remote inference engine with auditable open plugin transport.

## Links

- Repo: https://github.com/ThoriumAC/Thorium-Minecraft-Plugin

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[bs-anticheat]] · [[guardac]] · [[shard]] · [[grim]] · [[sentinel-anticheat-neoforge]] · [[minecraft-anticheat-list]] · [[detector-operations]]
