---
title: Ultimo
kind: entity
topics: [anti-cheat, game-server-security]
sources:
  - wiki/sources/descriptions/StanislawGolec__Ultimo.md
  - wiki/sources/README-categories.md
updated: 2026-10-17
confidence: medium
---

# Ultimo

**Authoritative multiplayer card-game server** inspired by Uno, implemented in **Java 21** with no external runtime dependencies. Reference for server-side validation, fog-of-war state sync, and lightweight multiplayer networking without Spring or similar frameworks. (source: wiki/sources/descriptions/StanislawGolec__Ultimo.md)

## Architecture

- **Multiplexed transport:** raw TCP, in-house **RFC 6455 WebSocket** stack, and embedded **HTML5** client on one port
- **Concurrency:** Java **virtual threads** per connection; **actor-style per-room event loop** for safe concurrent game state
- **Wire protocol:** line-delimited text protocol; terminal and browser clients

## Server-side anti-cheat patterns

Fully authoritative gameplay—not client-trust card state:

- Validates every **move, shuffle, and penalty** on the backend
- **Fog-of-war filtering** so clients never receive opponents' hidden cards
- Illustrates cheat-resistant **state synchronization** for online card games

## Testing and deployment

Large **JUnit** suite including concurrency and WebSocket fuzz tests. **Docker** and **Cloud Run** deployment paths.

## Links

- Repo: https://github.com/StanislawGolec/Ultimo

## Related

[[overviews/anti-cheat]] · [[blastscale]] · [[shinobix]] · [[guard-game]] · [[input-provenance]]
