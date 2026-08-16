---
title: IW4MAdmin SebzAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/crazythecoder__IW4MAdmin-SebzAntiCheat.md
updated: 2026-08-16
confidence: medium
---

# IW4MAdmin SebzAntiCheat

**Server-side suspicion telemetry and staff review system** for **IW4X** (Call of Duty: Modern Warfare 2 community client) that collects cheat indicators and presents cases through an **IW4MAdmin** dashboard **without automatically banning players**. Targets IW4X server administrators who need structured cheat investigation and human moderation rather than unattended enforcement. (source: wiki/sources/descriptions/crazythecoder__IW4MAdmin-SebzAntiCheat.md)

## Detection stack

- **GSC scripts** on the game server — aim anomalies, visibility issues, radar context, and repeated suspicious patterns
- **Native IW4MAdmin detections** — snap, strain, recoil, bone, button, and offset evidence
- **JavaScript plugins** — aggregate evidence; score **risk** and **confidence** separately
- **Node.js Discord watcher** — notify staff of new cases via Discord
- Optional **Python flag worker** for downstream processing

## Moderation workflow

Supports **watch**, **clear**, **purge**, and **recover** moderation workflows so staff can triage, dismiss, or escalate cases from the dashboard rather than relying on auto-ban logic.

## Operations tooling

Python release tooling provides signed updates with validation, backups, and rollback. Performance-aware sampling helps busy servers limit telemetry overhead.

Sits in the server-authoritative community-host lane beside [[cs2-calladmin]], [[7dtd-anticheatmod]], and [[cs2ac]] — human-in-the-loop review over automated kernel AC.

## Links

- Repo: https://github.com/crazythecoder/IW4MAdmin-SebzAntiCheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[cs2-calladmin]] · [[7dtd-anticheatmod]] · [[aimbot-detection-prototype]]
