---
title: bevy-personal-test (XX-Batsu)
kind: entity
topics: [game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/XX-Batsu__bevy-personal-test.md
updated: 2026-08-19
confidence: medium
---

# bevy-personal-test (XX-Batsu)

**Rust/Bevy game security testbed** (XX-Batsu) for building and evaluating tamper-resistant multiplayer clients and servers. Centers on **deterministic simulation**, **rollback netcode**, **state hashing**, and **server-side replay validation**, with a **shadow virtual machine** that runs parallel game-logic checks in WebAssembly workers alongside the main client. Adds encrypted assets, ECDH key exchange, a sandboxed bytecode VM with **Rhai** scripting, memory guards, and dedicated anti-cheat and validator services on the server; includes build tools, fuzz targets, and browser integration via JavaScript loaders for researchers prototyping anti-cheat, server authority, and integrity verification. (source: wiki/sources/descriptions/XX-Batsu__bevy-personal-test.md)

Complements OSS AC evaluation harnesses such as [[anti-cheat-testbench]] and [[anti-cheat-testing-framework]], Wasm replay-verified platforms such as [[magnetite]], and cross-engine server-authoritative adapters such as [[certael]]—all on the [[bevy]] ECS stack rather than a proprietary kernel AC product.

## Links

- Repo: https://github.com/XX-Batsu/bevy-personal-test (README: Rust Bevy multiplayer framework with sandboxed Rhai script VM, rollback netcode, and shadow-VM anti-cheat verification)

## Related

[[bevy]] · [[anti-cheat-testbench]] · [[anti-cheat-testing-framework]] · [[magnetite]] · [[certael]] · [[overviews/game-engine]] · [[overviews/anti-cheat]]
