---
title: dot-server-security
kind: entity
topics: [game-engine, anti-cheat, game-server-security]
sources:
  - wiki/sources/descriptions/modcommunity__dot-server-security.md
  - wiki/sources/README-categories.md
updated: 2026-09-12
confidence: medium
---

# dot-server-security

**Godot 4 dedicated-server security addon** with a unified, configuration-driven rule engine for multiplayer operators. Written in **GDScript**, it applies sliding-window rate limits and escalation ladders (warn, gag, mute, kick, ban) across chat, connections, authentication, the remote console, and server-side anti-cheat detections. (source: wiki/sources/descriptions/modcommunity__dot-server-security.md)

Server-side anti-cheat distinguishes mathematically impossible claims from merely suspicious behavior, supports movement re-simulation hooks, and can merge external ban feeds with multiple authentication modes. Ships in **dry-run mode by default** and integrates optionally with companion dot-* addons for moderation and chat. Listed under README **Anti Cheat > Open Source Anti Cheat System**.

## Anti-cheat surfaces

- **Movement re-simulation** — server-side validation hooks for impossible motion
- **Shot validation** — distinguish impossible vs suspicious combat claims
- **Rule-engine escalation** — configurable ladders instead of hard-coded punishments
- **Ban feeds** — merge external ban lists with local auth modes

## Links

- Repo: https://github.com/modcommunity/dot-server-security

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[void-engine]] · [[godot]] · [[better-godot-mcp]] · [[detector-operations]] · [[research-rigor]]
