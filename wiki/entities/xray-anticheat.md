---
title: XRay AntiCheat
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/LB45440078L__xray-anticheat.md
updated: 2026-10-09
confidence: medium
---

# XRay AntiCheat

Paper/Spigot plugin that detects ore-vision (X-Ray) mining with **likelihood-ratio statistical models**, explainable evidence, decaying player history, and moderator-driven ban waves. Maven multi-module Java: Minecraft-free analytical core, JDBC persistence, embedded web admin, and a Spigot plugin listening to mining events. (source: wiki/sources/descriptions/LB45440078L__xray-anticheat.md)

## Capabilities

Signals include buried vs exposed ore discoveries, tunnel geometry, targeting patterns, and inter-discovery timing. Staff review via in-game commands, GUI, and optional ban-wave planning; default policy favors human review over automatic bans.

## Links

- Repo: https://github.com/LB45440078L/xray-anticheat

## Related

[[jevcraft-bench]] · [[minecraft-anticheat-list]] · [[detector-operations]] · [[research-rigor]] · [[overviews/anti-cheat]]
