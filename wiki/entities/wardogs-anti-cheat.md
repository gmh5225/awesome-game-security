---
title: Wardogs Anti-Cheat
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/KSroido__wardogs-anti-cheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-28
confidence: medium
---

# Wardogs Anti-Cheat

**Wardogs anti-cheat** (KSroido) is a **server-side** moderation and cheat-detection stack for community Wardogs dedicated hosts. Kill and player events arrive from the **Nightwatch** game-server panel; enforcement (bans, kicks, announcements, whispers, team changes) flows back through the same integration. The implementation is primarily **TypeScript** on **Cloudflare Workers** with a shared **Cloudflare D1** SQLite store, split across four workers: event hook, scheduled cron, admin web tools, and faction-switch guard.

Detection uses a **karma scoring** model with configurable rules over suspicious combat statistics—extreme K/D, headshot rates, long-range kills, frequent renames—and optional **Steam account risk** checks including VAC and game-ban history. Operational extras include auto-balance, clan friend checks, dashboards, and match-economy leaderboards. Targets private-server operators who want automated heuristics and Steam-linked enforcement without a traditional always-on backend. Listed under Anti Cheat / Open Source Anti Cheat System. (source: wiki/sources/descriptions/KSroido__wardogs-anti-cheat.md)

Pairs with defensive mechanics reference [[wardogs-data-docs]] for Wardogs balance and combat ground truth when tuning karma thresholds.

## Architecture

- **Event hook worker** — ingests Nightwatch-forwarded kill and player events for real-time scoring.
- **Cron worker** — scheduled reconciliation and batch maintenance on D1 state.
- **Admin web worker** — operator dashboards and configuration surfaces.
- **Faction-switch guard** — policy checks around team/faction changes.

## Detection model

- **Karma rules** — weighted hits on statistical outliers (K/D, headshots, range, rename churn).
- **Steam risk** — optional VAC/game-ban history signals before kick or ban.
- **Enforcement API** — Nightwatch-backed bans, kicks, messaging, and team controls.

## Links

- Repo: https://github.com/ksroido/wardogs-anti-cheat

## Related

[[overviews/anti-cheat]] · [[detector-operations]] · [[wardogs-data-docs]] · [[detect-fps-hackers]] · [[gamespice-anticheat]] · [[dot-server-security]]