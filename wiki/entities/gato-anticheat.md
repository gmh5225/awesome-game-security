---
title: Gato AntiCheat
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/true-og__Gato-AntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# Gato AntiCheat

**Gato AntiCheat** is a Fabric dedicated-server mod that enforces combat rules on Java Minecraft worlds, originally built for Nexia’s CTS (combat test snapshot) environment. It uses Fabric Loader, Fabric API, and SpongePowered Mixins to intercept attacks, interaction packets, and entity damage on the server only. Reach checks use lag-aware victim bounding-box history; attack angles and line of sight are validated; suspicious critical hits are flagged from common client cheat fall distances. Fabric events expose reach, bad angle, criticals, and related detections so operators can wire kicks, logging, or custom sanctions. (source: wiki/sources/descriptions/true-og__Gato-AntiCheat.md)

Targets PvP administrators and mod authors who want a lightweight, server-side combat reference rather than full client attestation. Sits beside Paper/Folia plugins such as [[h-ac]] and Fabric suites such as [[bastion]] in the Open Source Anti Cheat System lane.

## Detection surfaces

- **Reach** — lag-compensated victim AABB history on the authoritative server.
- **Angles & LOS** — attack direction and visibility validation.
- **Critical hits** — heuristics for implausible fall-distance crit patterns.
- **Fabric events** — hookable signals for staff automation (kick, log, custom rules).

## Links

- Repo: https://github.com/true-og/Gato-AntiCheat

## Related

[[bastion]] · [[h-ac]] · [[tfg-anticheat-serverside]] · [[overviews/anti-cheat]] · [[overviews/game-engine]]
