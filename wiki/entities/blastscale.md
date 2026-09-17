---
title: BlastScale
kind: entity
topics: [anti-cheat, mobile-security, game-server-security]
sources:
  - wiki/sources/descriptions/AtakanKeser__BlastScale.md
  - wiki/sources/README-categories.md
updated: 2026-09-17
confidence: medium
---

# BlastScale

Production-oriented **server-authoritative mobile puzzle** backend built around a casual Unity client, used to study game security, anti-cheat design, and server-side validation at scale. (source: wiki/sources/descriptions/AtakanKeser__BlastScale.md)

## Stack

- **Server:** Java Spring Boot modular monolith
- **Admin:** React + TypeScript panel
- **Client:** Unity C#
- **Data:** MySQL, Redis, MongoDB, Elasticsearch
- **Ops:** Prometheus + Grafana observability; LiveOps events, remote config, and A/B experiments

## Server-side anti-cheat

Fully authoritative gameplay loop—not client-trust scoring:

- Issues **level seeds**; replays submitted moves through a **deterministic board engine**
- **Chain-of-responsibility** pipeline validates sessions, timing, score bounds, and move sequences before rewards
- **Exactly-once economy** updates via idempotency keys and an append-only ledger
- Redis-backed leaderboards beside the validation path

Reference for mobile puzzle backends combining move-replay integrity with reward/economy hardening. Compare [[shinobix]] (browser MMORPG auth/reward-integrity) and [[cobra-snake]] (web Snake HMAC sessions + score plausibility). (source: wiki/sources/descriptions/AtakanKeser__BlastScale.md)

## Links

- Repo: https://github.com/AtakanKeser/BlastScale

## Related

[[overviews/anti-cheat]] · [[input-provenance]] · [[detector-operations]] · [[mobile-trust-boundaries]] · [[cobra-snake]] · [[shinobix]]
