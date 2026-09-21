---
title: guard-game
kind: entity
topics: [anti-cheat, game-engine, game-server-security]
sources:
  - wiki/sources/descriptions/Parko-Developer__guard-game.md
  - wiki/sources/README-categories.md
updated: 2026-09-21
confidence: medium
---

# guard-game

**Node.js server-side anti-cheat** that validates player movement and gameplay actions against configurable **world profiles** instead of trusting client reports. Zero runtime dependencies; JSON line protocol over **TCP** plus an **HTTP ingest bridge**; client SDKs for **Unity/C#**, **Godot/GDScript**, **Roblox/Luau**, and **JavaScript**. (source: wiki/sources/descriptions/Parko-Developer__guard-game.md)

Physics-based rules target speed hacks, impossible jumps, teleports, flight/hover exploits, packet flooding, timestamp/sequence spoofing, and action abuse (item duplication, quest farming). Strike-based warnings, automatic bans, admin HTTP API/console, optional **HMAC frame signing**, and Docker deployment. Listed under README **Anti Cheat > Open Source Anti Cheat System**.

## Positioning

Lightweight, **zero runtime dependency** Node.js service for indie and custom multiplayer titles that need an external server-side AC layer without embedding engine-specific plugins. Clients report movement and actions; the server applies **world-profile** physics limits rather than trusting client state. (source: wiki/sources/descriptions/Parko-Developer__guard-game.md)

## Validation surfaces

| Surface | Role |
|---------|------|
| Movement | World-profile physics limits (speed, jump, teleport, fly/hover) |
| Actions | Item/quest abuse heuristics |
| Transport | TCP JSON lines + HTTP ingest; optional HMAC signing |
| Enforcement | Strike ladder → warnings → bans; admin API/console |

## Engine SDKs

Unity (C#), Godot (GDScript), Roblox (Luau), JavaScript — engine-agnostic server layer for custom multiplayer hosts.

## Links

- Repo: https://github.com/Parko-Developer/guard-game

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[dot-server-security]] · [[void-engine]] · [[volcano-ac]] · [[detector-operations]] · [[input-provenance]] · [[research-rigor]]
