---
title: Stellar Splash Engine
kind: entity
topics: [anti-cheat, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/Stellar-Splash__stellar-splash-engine.md
updated: 2026-11-11
confidence: medium
---

# Stellar Splash Engine

**Stellar Splash Engine** is a **TypeScript** backend for a **Web3 splash-game** platform that runs **competitive tournaments** and **authoritatively verifies** client-reported gameplay instead of trusting scores on submission alone. Raw match events feed a **deterministic headless simulator**; when the replayed outcome matches **server-side physics**, the stack issues **cryptographic attestations** suitable for auditable esports and payout workflows. (source: wiki/sources/descriptions/Stellar-Splash__stellar-splash-engine.md)

Anti-cheat enforcement layers include **session tokens**, **click-timing** checks, **tick anomaly** detection, and **entropy heuristics** on submitted telemetry. **Stellar Horizon** indexing and **Soroban** smart contracts handle **entry-fee validation**, **prize-pool escrow**, **settlements**, and **channel-account transaction pooling**; operations add **rate limiting**, **OWASP-oriented** hardening, **Prometheus** metrics, and **webhook** notifications for tournament operators.

Compared with browser HMAC leaderboard references such as [[pew-game]] or GHST input-replay stacks such as [[ghostline]], Stellar Splash couples **replay attestation** with **on-chain settlement** and **tournament orchestration** for Web3 esports operators.

## Links

- Repo: https://github.com/Stellar-Splash/stellar-splash-engine

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[ghostline]] · [[nimjump]] · [[blastscale]] · [[leaderboard]]
