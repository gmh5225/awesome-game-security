---
title: Aurix Net
kind: entity
topics: [game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/aurix-voice__aurix-net.md
updated: 2026-11-12
confidence: medium
---

# Aurix Net

**Self-hostable, game-agnostic multiplayer backend** (aurix-voice) that unifies relay, server-authoritative state sync, and deterministic lockstep rooms on a single node. Implemented mainly in **Rust** with **QUIC** and **WebTransport** datagram transport, a **Postgres** and **Redis** multi-node control plane, and client SDKs for the web, Unity, C++, and Godot, plus a React operator console. Lockstep sessions can use an optional **WASM referee** that simulates room logic on the server as the source of truth, alongside predict-and-rollback, lag-compensation history, **desync detection**, and matchmaking with operator-facing quotas, API keys, grants, and audit logging. The bundled deterministic simulation stack uses fixed-point math and WASM so native and browser builds stay hash-aligned for physics, navigation, and bot logic. Targets developers who need production-grade netcode and server-side authority to limit cheating and keep competitive multiplayer state consistent. (source: wiki/sources/descriptions/aurix-voice__aurix-net.md)

Sits in the README **Game Network** lane beside rollback P2P libraries such as [[ggpo]], [[ggrs]], and [[gekkonet]], client/server stacks such as [[yojimbo]] and [[lightyear]], and server-side verification references such as [[ghostline]] and [[magnetite]]. Security-relevant surfaces include WASM server referee authority, deterministic hash-aligned simulation, desync detection, and operator audit controls.

## Links

- Repo: https://github.com/aurix-voice/aurix-net

## Related

[[ggpo]] · [[ggrs]] · [[gekkonet]] · [[yojimbo]] · [[lightyear]] · [[ghostline]] · [[magnetite]] · [[overviews/game-engine]] · [[overviews/anti-cheat]]
