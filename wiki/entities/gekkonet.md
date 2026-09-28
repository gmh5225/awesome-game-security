---
title: GekkoNet
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/HeatXD__GekkoNet.md
updated: 2026-09-28
confidence: medium
---

# GekkoNet

**C/C++ rollback and lockstep netcode library** for deterministic, frame-synchronized multiplayer games (HeatXD). Inspired by [[ggpo]] and [[ggrs]], it exposes a **C API** for session management, player-input exchange, and save/load callbacks used during rollback, with configurable **input prediction**, **runahead**, **local input delay**, and optional **lockstep-only** play. Ships a built-in **UDP adapter** powered by ASIO, plus **spectator support**, compressed **replay recording and playback**, **checksum-based desync detection**, and network statistics (ping, jitter). **SDL3-based examples** cover local, online, spectator, and stress-test sessions; builds as static or shared libraries with **CMake** and **Visual Studio**. Targets game developers and researchers who need reliable peer-to-peer netcode and practical tooling to detect, reproduce, and debug client state divergence. (source: wiki/sources/descriptions/HeatXD__GekkoNet.md)

Sits in the README **Game Network** lane beside the canonical C++ [[ggpo]] SDK, Rust GGPO-style ports such as [[ggrs]], C++ client/server stacks such as [[yojimbo]], server-authoritative Bevy netcode such as [[lightyear]], and security-oriented rollback testbeds such as [[bevy-personal-test]]. Security-relevant surfaces include deterministic checksum desync detection, replay capture for divergence reproduction, and lockstep modes that expose simulation drift across peers.

## Links

- Repo: https://github.com/HeatXD/GekkoNet (README: C/C++ P2P rollback networking SDK inspired by GGPO and GGRS, with input prediction and speculative execution)

## Related

[[ggpo]] · [[ggrs]] · [[yojimbo]] · [[lightyear]] · [[bevy-personal-test]] · [[game-networking-resources]] · [[overviews/game-engine]]
