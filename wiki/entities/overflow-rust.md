---
title: overflow-rust
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat, graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/NMan1__OverflowRust.md
updated: 2026-08-22
confidence: medium
---

# overflow-rust

**overflow-rust** (NMan1/OverflowRust) is an **external Windows game cheat framework** for **Facepunch Rust** built around a **kernel driver** paired with a **user-mode client** for rendering and control. Implemented mainly in **C and C++**, it documents a bypass path based on **hooking a kernel call chain** and exchanging data through **shared memory**. Feature modules include **ESP** entity visuals, **recoil control**, automation options, and other gameplay state manipulations. Intended for reverse-engineering and anti-cheat evasion research around kernel hooks and overlay techniques under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/NMan1__OverflowRust.md)

Sits in the Facepunch Rust kernel-assisted external lane beside [[rust-external-cheat]], [[rust-external-1]], and [[rust-external-source]], and complements NMan1's [[rainbow-six-cheat]], [[apex-legends-cheat]], and [[external-warzone-cheat]] samples with a shared-memory KM↔UM driver + external-client path for Unity titles.

## Architecture

| Component | Role |
|-----------|------|
| Kernel driver | Kernel call-chain hook bypass and cross-process cheat pipeline |
| User-mode client | Rendering, control UI, and feature orchestration |
| Shared memory | KM↔UM communication channel between driver and client |
| Feature modules | ESP entities, recoil control, automation, gameplay state mods |

See [[world-to-screen]] for ESP projection and [[easy-anti-cheat]] for the protected-title context.

## Links

- Repo: https://github.com/NMan1/OverflowRust

## Related

[[rust-external-cheat]] · [[rust-external-1]] · [[rust-external-source]] · [[rainbow-six-cheat]] · [[apex-legends-cheat]] · [[external-warzone-cheat]] · [[easy-anti-cheat]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
