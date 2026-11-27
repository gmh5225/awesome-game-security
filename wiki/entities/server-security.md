---
title: GameSpice Server Security
kind: entity
topics: [game-engine, anti-cheat, game-server-security]
sources:
  - wiki/sources/descriptions/gamespice-platform__server-security.md
updated: 2026-11-27
confidence: medium
---

# GameSpice Server Security

**Godot 4 dedicated-server security addon** in the GameSpice stack: GDScript modules that harden live multiplayer hosts by watching chat, connections, authentication, remote console traffic, and server-side anti-cheat signals against operator-defined rules. Targets operators running **GameSpice Core** and **GameSpice Server** who want configurable guardrails and enforcement without bolting on a separate punishment stack. (source: wiki/sources/descriptions/gamespice-platform__server-security.md)

A **unified sliding-window rule engine** shares counters, escalation ladders, exemptions, and **dry-run defaults** across detections and game events before actions escalate through **warn → gag → mute → kick → ban**. Server-side anti-cheat distinguishes **provable violations** from **suspicious behaviour** that merits warnings only. **External ban-list feeds** merge into join checks; operator consoles expose commands such as `sec_why` and `sec_status`. Listed under README **Anti Cheat → Open Source Anti Cheat System**.

## Rule engine surfaces

| Surface | Role |
|---------|------|
| Chat | Sliding-window limits + gag/mute escalation |
| Connections | Join/flood monitoring |
| Authentication | Auth paths + ban-feed merge |
| Remote console | Abuse throttling on admin commands |
| Server-side AC | Provable vs suspicious violation tiers |

## Design notes

- **Integrated escalation** — punishments ride the same rule engine as moderation signals (contrast [[gamespice-anticheat]], which emits escalation hooks only)
- **Dry-run by default** — tune ladders and exemptions before enforcement (see [[detector-operations]])
- **GameSpice pairing** — feeds speed/teleport/aim-snap style reports into [[gamespice-anticheat]] DotSuspicionWatch when both addons are present
- **Parallel to [[dot-server-security]]** — similar Godot dedicated-server rule-engine pattern from the modcommunity tree

## Links

- Repo: https://github.com/gamespice-platform/server-security

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[gamespice-anticheat]] · [[dot-server-security]] · [[guard-game]] · [[void-engine]] · [[godot]] · [[detector-operations]]