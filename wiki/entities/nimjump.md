---
title: NimJump
kind: entity
topics: [anti-cheat, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/nimjump__game.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# NimJump

**NimJump** (nimjump/game) is a browser-based casual platformer that distributes **cryptocurrency rewards** through a documented **minimal client-authority** design. The **Godot 4** client exports to **WebAssembly**; a **Go** backend validates gameplay with **deterministic map generation** and **server-side replay verification** via a native **replay-verifier** build. (source: wiki/sources/descriptions/nimjump__game.md)

Distinct from pure leaderboard HMAC patterns such as [[pew-game]] or GHST input-replay arenas such as [[ghostline]]: NimJump couples **Web3 payout abuse guards** (signed offline seed batches, IP reward checks) with **native replay attestation** for WASM clients.

## Architecture

| Component | Role |
|-----------|------|
| **Godot 4 client (WASM)** | Runs in-browser; submits signed API requests; offline play consumes server-signed seed batches |
| **Go backend** | Deterministic map generation; ingests sessions; drives replay verification |
| **Replay verifier** | Native build re-simulates runs for server-side attestation |
| **Next.js admin** | Monitors players, sessions, leaderboards, failed replays, and analytics |

## Anti-cheat mechanics

- Offline sessions: batches of **server-signed seeds** plus **signed client API requests**
- Supporting guards: **rate limits**, **IP reward checks**, admin tooling for failed replays
- Ops surface for replay integrity review alongside reward analytics (source: wiki/sources/descriptions/nimjump__game.md)

## Audience

**Game-security practitioners** who want a **production-style reference** for anti-cheat, **replay attestation**, and **reward abuse prevention** in browser/Web3 titles—listed under **Anti Cheat** and **Game Develop** in the README map.

## Links

- Repo: https://github.com/nimjump/game

## Related

[[ghostline]] · [[pew-game]] · [[aimguard]] · [[godot]] · [[overviews/anti-cheat]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[input-provenance]] · [[detector-operations]]
