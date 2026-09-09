---
title: ShinobiX
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/Timehue__ShinobiX.md
  - wiki/sources/README-categories.md
updated: 2026-09-09
confidence: medium
---

# ShinobiX

Live-service **browser ninja MMORPG** (Timehue) with a React/Vite single-page client, TypeScript API server, and Supabase-backed persistence. Combat, PvE, economy, and player-save flows are **server-authoritative**, defended with settlement receipts, currency ledgers, save locks, and authentication policies against client-side tampering and duplication. Ships extensive security-oriented documentation and audit material (HTTP hardening, auth/anti-cheat patterns, reward-integrity contracts, combat authority boundaries) plus broad automated tests across parity and settlement paths. Reference for practical online-RPG backend integrity—not a commercial AC product. (source: wiki/sources/descriptions/Timehue__ShinobiX.md)

## Architecture

React/Vite SPA client; TypeScript API layer; Supabase persistence; live-service MMORPG deployment.

## Integrity mechanisms

Server-authoritative combat, PvE, economy, and player-save flows; settlement receipts; currency ledgers; save locks; authentication policies resisting duplication and stat/reward spoofing.

## Documentation & testing

Published security audit material covering HTTP hardening, auth and anti-cheat patterns, reward-integrity contracts, and combat authority boundaries; automated parity and settlement-path test coverage.

## Links

- Repo: https://github.com/Timehue/ShinobiX

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[engine-trust-boundaries]] · [[gatewarden-public]] · [[adaptive-boss-arena]] · [[certael]] · [[research-rigor]]
