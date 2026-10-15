---
title: OpenLeaderboard
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/kodeni-am__leaderboard.md
updated: 2026-10-15
confidence: medium
---

# OpenLeaderboard

Open-source **multi-tenant leaderboard backend** for game developers who need fast rank queries and high write throughput on very large boards. The server is written in **Go** and uses a **Redis sorted-set** ranking engine fed by a **durable ingest log** for idempotent writes, replay, and cache rebuilds. Supports time windows, segments, friend-relative ranks, and approximate deep-tail ranking. (source: wiki/sources/descriptions/kodeni-am__leaderboard.md)

## Score submission hardening

Optional per-app **anti-cheat** validates **HMAC-signed score submissions** with a replay window. **Publishable vs secret API keys** and **player tokens** limit what client-exposed credentials can do—reducing moderation abuse and player impersonation when only publishable keys ship in game clients.

## Operations and clients

Web dashboard, reference **Go** and **TypeScript** SDKs, a **Unity** client, and **Docker**, **Terraform**, and AWS-oriented deployment with **Prometheus** and **Grafana** monitoring. Useful for self-hosting production leaderboards while hardening score submission and tenant isolation for live games.

## Links

- Repo: https://github.com/kodeni-am/leaderboard

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[pew-game]] · [[cobra-snake]] · [[blastscale]] · [[guard-game]]
