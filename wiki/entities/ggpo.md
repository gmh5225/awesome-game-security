---
title: GGPO
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/pond3r__ggpo.md
updated: 2026-09-28
confidence: medium
---

# GGPO

**C++ rollback networking SDK** for peer-to-peer online multiplayer (pond3r). Replaces traditional input-delay netcode with **input prediction and speculative execution**: player inputs are sent immediately and the simulation rolls back when predictions diverge, preserving offline responsiveness online. Uses **UDP-based P2P** communication with deterministic game-state serialization, save/load callbacks, input synchronization, and time-sync handling. Ships P2P, spectator, and sync-test backends plus the **Vector War** sample for 2–4 players. Built with **CMake** for Windows (Linux support underway); exposes a callback-driven API via `ggponet.h` for integrating rollback networking into new or existing engines. Targets game developers building latency-sensitive competitive titles such as fighting games where low-latency synchronized netcode is essential. (source: wiki/sources/descriptions/pond3r__ggpo.md)

Sits in the README **Game Network** lane beside Rust GGPO-style ports such as ggrs, Bevy netcode such as [[lightyear]], and security-oriented rollback testbeds such as [[bevy-personal-test]]. UE5 fighting frameworks such as [[nightsky-engine]] integrate GGPO-based rollback rather than shipping this SDK directly.

## Links

- Repo: https://github.com/pond3r/ggpo (README: Rollback networking SDK using input prediction and speculative execution; includes the Vector War sample)

## Related

[[lightyear]] · [[bevy-personal-test]] · [[nightsky-engine]] · [[game-networking-resources]] · [[overviews/game-engine]]
