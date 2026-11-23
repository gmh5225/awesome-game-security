---
title: Quarterhood Engine
kind: entity
topics: [game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/quarterhood__engine.md
updated: 2026-11-23
confidence: medium
---

# Quarterhood Engine

**Quarterhood Engine** (quarterhood/engine) is the open-source deterministic game logic and run verifier behind **Quarterhood**, a blockchain-hosted skill arcade where scores are never taken from the browser at face value. The server seeds each run and stores only per-frame input events; it replays those inputs through shared **TypeScript** simulations to derive score, frame count, and a cryptographic hash of final state that anyone can reproduce locally. (source: wiki/sources/descriptions/quarterhood__engine.md)

## Integrity model

- **Shared replay core** — xorshift32 RNG and integer-only physics across multiple mini-games; golden fixtures lock expected outcomes across JavaScript engines.
- **Node verifier CLI** — replays recorded inputs from a seed to validate server scores via a public run API.
- **On-chain attestations** — companion Solidity contract commits weekly leaderboard rows to Robinhood Chain as immutable Merkle roots tied to replay hashes.
- **Anti-scripting flags** — public heuristics gate suspicious runs for human review.

Useful for studying **client–server game integrity**, **verifiable scoring**, and transparent anti-cheat for competitive online play—adjacent to deterministic replay references such as [[bitgeist]], [[dmn-minigame]], [[stellar-splash-engine]], and [[ghostline]].

## Links

- Repo: https://github.com/quarterhood/engine

## Related

[[concepts/input-provenance]] · [[bitgeist]] · [[dmn-minigame]] · [[stellar-splash-engine]] · [[overviews/game-engine]] · [[overviews/anti-cheat]]