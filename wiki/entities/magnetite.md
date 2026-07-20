---
title: Magnetite
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/vul-os__magnetite.md
updated: 2026-07-20
confidence: medium
---

# Magnetite

Decentralized, self-hostable Rust game platform for authoritative multiplayer: write once, run from a laptop to an owned fleet without a central cloud. Games target a deterministic authoritative-server SDK, compile to `wasm32-wasip1`, and execute in a Wasmtime sandbox with fuel budgets, memory caps, epoch timeouts, and seeded deterministic RNG so the same inputs always produce the same state. (source: wiki/sources/descriptions/vul-os__magnetite.md)

Anti-cheat is built in by construction: clients send inputs only; the server validates and steps simulation; `ReplayLog` plus `verify_replay` re-simulates ticks for tamper evidence; and `magnetite-anticheat` adds composable validators (aimbot snap, teleport, fire-rate flood) with trust-score escalation. The platform also provides content-addressed game distribution, auto-selected topologies (SingleRoom → Dedicated → Sharded), and pluggable seams for identity, discovery, comms, and non-custodial crypto payments. Aimed at developers and hosts who need sandboxed, replay-verified anti-cheat and self-hosted multiplayer infrastructure rather than a proprietary cloud stack—adjacent to server-authoritative OSS AC such as [[certael]], not kernel products like [[easy-anti-cheat]] or [[vanguard]].

## Links

- Repo: https://github.com/vul-os/magnetite

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[certael]] · [[easy-anti-cheat]] · [[vanguard]]
