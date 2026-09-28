---
title: Yojimbo
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/mas-bandwidth__yojimbo.md
updated: 2026-09-28
confidence: medium
---

# Yojimbo

**C++ client/server networking library** for real-time multiplayer games (mas-bandwidth). Built for competitive titles such as first-person shooters, it sits on vendored **netcode**, **reliable**, and **serialize** components to provide encrypted and signed UDP transport, connect-token authentication, connection management, packet fragmentation and reassembly, and both reliable-ordered and unreliable-unordered message channels. Includes a bitpacker serialization system, large data block support, per-connection latency and packet-loss statistics, and per-client TLSF heap isolation on the server. Written primarily in C++ with CMake-based builds and extensive fuzz testing of untrusted wire parsers; targets game developers who need a production-ready, security-conscious netcode layer for client/server games with up to roughly 100 players. (source: wiki/sources/descriptions/mas-bandwidth__yojimbo.md)

Sits in the README **Game Network** lane beside transport libraries such as [[game-networking-sockets]] and [[kcp]], server-authoritative Bevy netcode such as [[lightyear]], and rollback P2P SDKs such as [[ggpo]]. Security-relevant surfaces include connect-token authentication, encrypted/signed wire formats, and fuzz-hardened deserialization—relevant when studying packet injection, replay, or server-side memory isolation under hostile clients.

## Links

- Repo: https://github.com/mas-bandwidth/yojimbo (README: C++ network library for client/server games)

## Related

[[game-networking-sockets]] · [[lightyear]] · [[ggpo]] · [[game-networking-resources]] · [[bevy-personal-test]] · [[overviews/game-engine]]
