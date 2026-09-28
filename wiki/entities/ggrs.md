---
title: GGRS
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/gschup__ggrs.md
updated: 2026-09-28
confidence: medium
---

# GGRS

**Rust rollback networking library** reimplementing GGPO-style peer-to-peer netcode (gschup). Written entirely in safe Rust, it replaces the original callback-driven API with a simpler **request-based control flow**: the library returns save, load, and advance operations for the game to fulfill. Supports **P2P and spectator sessions**, configurable input prediction and lockstep modes, **UDP transport** with optional custom sockets, and built-in **SyncTestSession** plus checksum-based desync detection to validate deterministic simulation. Targets game developers who need low-latency netcode and want to verify that game logic stays synchronized across clients—relevant for fair online play and cheat-resistant networked simulations. (source: wiki/sources/descriptions/gschup__ggrs.md)

Sits in the README **Game Network** lane beside the canonical C++ [[ggpo]] SDK, C++ client/server stacks such as [[yojimbo]], server-authoritative Bevy netcode such as [[lightyear]], and security-oriented rollback testbeds such as [[bevy-personal-test]]. Security-relevant surfaces include deterministic state checksums, sync-test harnesses, and lockstep modes that expose desync when simulation diverges.

## Links

- Repo: https://github.com/gschup/ggrs (README: Safe Rust reimagining of GGPO with a request-based API; includes P2P, spectator, and sync-test examples)

## Related

[[ggpo]] · [[yojimbo]] · [[lightyear]] · [[bevy-personal-test]] · [[nightsky-engine]] · [[game-networking-resources]] · [[overviews/game-engine]]
