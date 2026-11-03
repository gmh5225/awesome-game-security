---
title: NimJump
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/nimjump__game.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# NimJump

**NimJump** (nimjump/game) is a browser-based casual platformer that distributes cryptocurrency rewards through a minimal client-authority design. The Godot 4 client exports to WebAssembly while a Go backend validates gameplay with deterministic map generation and server-side replay verification via a native replay-verifier build. (source: wiki/sources/descriptions/nimjump__game.md)

## Anti-cheat mechanics

- Offline sessions use batches of server-signed seeds and signed client API requests
- Rate limits, IP reward checks, and admin tooling for failed replays and analytics
- Next.js admin dashboard for players, sessions, leaderboards, and replay integrity

## Role in the README map

Listed under **Anti Cheat** and **Game Develop** as a production-style reference for replay attestation, signed seed batches, and reward-abuse prevention beside [[ghostline]] and [[aimguard]].

## Links

- Repo: https://github.com/nimjump/game

## Related

[[ghostline]] · [[aimguard]] · [[overviews/anti-cheat]] · [[overviews/game-engine]] · [[detector-operations]] · [[input-provenance]]
