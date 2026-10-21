---
title: Obelisk
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Zagrios__Obelisk.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: medium
---

# Obelisk

**Native Apple silicon macOS game launcher** that signs into **Steam, Epic Games, and GOG** and manages download, update, install, and launch from one unified library. (source: wiki/sources/descriptions/Zagrios__Obelisk.md)

A **SwiftUI** front end talks to a **Rust** core implementing each storefront’s protocols (informed by public tools such as SteamKit and Legendary), including transfers, cloud saves, friends, chat, and an in-game overlay without requiring official store clients. Windows builds run through the bundled **Voile Wine** runtime, with per-game profiles choosing Rosetta-based Wine or a **Linux compatibility engine backed by voile-lkd** for titles whose anti-cheat supports Linux, plus Metal graphics paths such as D3DMetal and DXMT.

The project emphasizes **running games legitimately without modifying or bypassing anti-cheat**, while documenting engine choice, runtime contracts, and launch diagnostics for compatibility work on Mac. It suits players consolidating stores on Apple silicon and researchers studying storefront integration, Wine-based translation, and **anti-cheat constraints on non-Windows platforms**.

Listed in the README under **Cheat** (Linux / Proton / macOS compatibility lane).

## Links

- Repo: https://github.com/Zagrios/Obelisk

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[are-we-anti-cheat-yet]] · [[pointblank-linux]] · [[crossover-patcher]] · [[holodori-kernel-bypass]]
