---
title: AimGuard
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/Ajitha-2001__aimguard.md
  - wiki/sources/README-categories.md
updated: 2026-10-22
confidence: high
---

# AimGuard

**Server-side anti-cheat prototype** (Python) that ingests match telemetry, scores player behavior, and supports **moderator-driven enforcement** rather than automatic bans. (source: wiki/sources/descriptions/Ajitha-2001__aimguard.md)

Modules cover aim/movement feature extraction, **lag-compensated validation**, grid-based **potential visibility sets** (PVS) to limit client replication, and network integrity (HMAC, anti-replay). The stack adds Play Integrity attestation handling, statistical and ML detectors, hash blocklists with optional local PC scanning, SQLite persistence, and a token-authenticated **HTTP API** with review queues, appeals, and ban waves. Targets engineers experimenting with shadow-mode scoring, evidence trust levels, and operational workflows on **synthetic gameplay data** before production client protection.

Listed under README **Anti Cheat > Open Source Anti Cheat System** beside [[guard-game]] and [[dot-server-security]].

## Links

- Repo: https://github.com/Ajitha-2001/aimguard

## Related

[[detector-operations]] · [[input-provenance]] · [[guard-game]] · [[dot-server-security]] · [[overviews/anti-cheat]]
