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

**Godot 4 dedicated-server security addon** that hardens multiplayer hosts through a unified, **configuration-driven rule engine** rather than hard-coded anti-abuse logic. Written in **GDScript**, it targets operators who want configurable guardrails across chat, connections, authentication, the remote console, and server-side anti-cheat detections. (source: wiki/sources/descriptions/modcommunity__dot-server-security.md)

The engine applies **sliding-window rate limits** and escalation ladders (**warn → gag → mute → kick → ban**) per surface. Server-side anti-cheat separates **mathematically impossible** claims from merely **suspicious** behavior, supports **movement re-simulation** hooks and **shot validation**, and can merge **external ban feeds** with multiple authentication modes. Ships in **dry-run mode by default** for rule auditing before enforcement. Optional companion **dot-*** addons extend moderation and chat integration. Listed under README **Anti Cheat > Open Source Anti Cheat System**.

## Rule engine surfaces

| Surface | Role |
|---------|------|
| Chat | Rate limits + gag/mute escalation |
| Connections | Join/flood throttling |
| Authentication | Multi-mode auth + ban-feed merge |
| Remote console | Abuse throttling on admin paths |
| Server-side AC | Movement re-sim, shot validation, impossible vs suspicious tiers |

## Anti-cheat surfaces

- **Movement re-simulation** — server-side validation hooks for impossible motion
- **Shot validation** — distinguish impossible vs suspicious combat claims
- **Rule-engine escalation** — configurable ladders instead of hard-coded punishments
- **Ban feeds** — merge external ban lists with local auth modes
- **Dry-run auditing** — default non-punitive mode for tuning rules before rollout (see [[detector-operations]])

## Links

- Repo: https://github.com/modcommunity/dot-server-security

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[void-engine]] · [[godot]] · [[better-godot-mcp]] · [[detector-operations]] · [[research-rigor]]
