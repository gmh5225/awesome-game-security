---
title: Serverless Time-Trial Racing Game
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/eric-rolph__serverless-time-trial-racing-game.md
updated: 2026-11-23
confidence: medium
---

# Serverless Time-Trial Racing Game

**Serverless Time-Trial Racing** (eric-rolph/serverless-time-trial-racing-game) is an **edge-authoritative async sim-racing** reference: players drive laps on a **native Rust client**, then submit evidence to a **Cloudflare Worker** that **re-simulates** the run and accepts or rejects the lap time. The design targets **trust-minimized competitive racing**—leaderboard ranks follow **physically valid** replay outcomes, not client-reported finish state. (source: wiki/sources/descriptions/eric-rolph__serverless-time-trial-racing-game.md)

README category: serverless sim racing with shared Box3D WASM physics, Ed25519-signed input replay on Cloudflare Workers for bit-exact lap validation and cheat-resistant leaderboards (Anti Cheat).

## Deterministic physics kernel

A **Box3D** physics core is compiled once to **WebAssembly** and stepped at a fixed **400 Hz** on:

| Runtime | Role |
|---------|------|
| **Rust native client** (`wasmtime`) | Local play and lap capture |
| **TypeScript Worker referee** (V8) | Authoritative re-simulation |

**Bit-exact determinism** across runtimes lets the edge referee verify laps by **replaying signed input logs** instead of trusting client-simulated state or scores.

## Integrity model

- **Ed25519-signed lap logs** — tamper-evident submit payloads.
- **WASM replay + state-hash comparison** — reject runs whose replayed simulation diverges from submitted hashes.
- **Telemetry heuristics** — supplementary signals aimed at **tool-assisted input** patterns.
- **KV-backed leaderboards** on Workers — validated times only.

**Weekly procedural tracks** are generated and deployed via automation (**Python** track generation in the stack).

## Stack

**C** (physics kernel), **Rust** (client + submission pipeline), **TypeScript** (Workers + referee), **Python** (procedural tracks).

Useful for studying **server-side anti-cheat**, **deterministic simulation**, and **edge-hosted replay validation**—adjacent to browser replay platforms such as [[bitgeist]] and tick-aligned log replay such as [[dmn-minigame]].

## Links

- Repo: https://github.com/eric-rolph/serverless-time-trial-racing-game

## Related

[[bitgeist]] · [[dmn-minigame]] · [[leaderboard]] · [[concepts/input-provenance]] · [[overviews/anti-cheat]] · [[overviews/game-engine]]