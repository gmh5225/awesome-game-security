---
title: Lightyear
kind: entity
topics: [game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/cBournhonesque__lightyear.md
updated: 2026-08-23
confidence: medium
---

# Lightyear

**Rust server-authoritative multiplayer library** for the [[bevy]] game engine (cBournhonesque). Builds production netcode with **client-side prediction and rollback**, snapshot interpolation, deterministic input replication, lag compensation, bandwidth management, and world replication via `bevy_replicon`. Transport-agnostic networking over UDP, WebSocket, Steam, and WebTransport (via aeronet), with message channels, packet fragmentation, and postcard-based serialization; supports client-server, peer-to-peer, and host-client topologies with tick-synchronized input handling. Integrates physics and input crates such as Avian and Leafwing; includes WebAssembly support through WebTransport. Aimed at game developers and security researchers studying authoritative multiplayer architecture, netcode design, and the **client-server trust boundaries** that underpin anti-cheat and exploit analysis. (source: wiki/sources/descriptions/cBournhonesque__lightyear.md)

Sits in the README **Game Network** lane beside private-server stacks such as [[ds3os]] and [[ds2os]]. Complements security-oriented Bevy testbeds such as [[bevy-personal-test]] (shadow-VM replay validation, Rhai sandbox) and OSS server-authoritative AC foundations such as [[certael]]—Lightyear focuses on replication/netcode primitives rather than kernel AC or dedicated validator services.

## Links

- Repo: https://github.com/cBournhonesque/lightyear (README: Rust server-authoritative Bevy multiplayer library with prediction, rollback, and WebTransport/wasm support)

## Related

[[bevy]] · [[bevy-personal-test]] · [[certael]] · [[magnetite]] · [[overviews/game-engine]] · [[overviews/anti-cheat]]
