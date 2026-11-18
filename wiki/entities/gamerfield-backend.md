---
title: gamerfield-backend (Fairplay Arena)
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/ArghadeepMisra__gamerfield-backend.md
updated: 2026-11-18
confidence: medium
---

# gamerfield-backend (Fairplay Arena)

**Fairplay Arena** (`gamerfield-backend`, ArghadeepMisra) is a **stateless Spring Boot REST API** that acts as the source of truth for an anti-cheat gaming platform: player accounts, recorded matches, global rankings, moderator enforcement, and ban appeals. **Java 21** services expose **JWT-protected** endpoints for players, moderators, and trusted clients—including automated judges that must exceed confidence thresholds before bans apply. **PostgreSQL** stores durable state and an **append-only audit trail** enforced at the database layer for moderation actions; **Redis sorted sets** back fast leaderboard and rank lookups at scales where pure SQL counting is costly. The stack includes Docker Compose, Flyway migrations, OpenAPI, Prometheus metrics, and **k6** load benchmarks—useful for engineers studying production patterns for account state machines, idempotent match ingestion, refresh-token security, and human-in-the-loop cheat enforcement. (source: wiki/sources/descriptions/ArghadeepMisra__gamerfield-backend.md)

README category: Spring Boot REST backend for Fairplay anti-cheat (JWT auth, matches, Redis leaderboard, moderation queue, append-only audit log, ban appeals on PostgreSQL).

## Stack

| Layer | Role |
|-------|------|
| API | Stateless Spring Boot; role-scoped JWT (players, moderators, services) |
| Data | PostgreSQL accounts/matches/moderation; DB-enforced audit log |
| Ranks | Redis sorted sets for leaderboard/rank queries |
| Ops | Flyway, OpenAPI, Prometheus, Docker Compose, k6 benchmarks |

## Links

- Repo: https://github.com/ArghadeepMisra/gamerfield-backend

## Related

[[ghostline]] · [[blastscale]] · [[leaderboard]] · [[detector-operations]] · [[overviews/anti-cheat]]