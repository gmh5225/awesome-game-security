---
title: Obelisk
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Zagrios__Obelisk.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: high
---

# Obelisk

**Obelisk** ([Zagrios/Obelisk](https://github.com/Zagrios/Obelisk)) is a native **Apple silicon macOS** game launcher that signs into **Steam, Epic Games, and GOG**, then downloads, updates, installs, and launches owned titles from one unified library—without requiring the official store clients. (source: wiki/sources/descriptions/Zagrios__Obelisk.md)

A **SwiftUI** front end talks to a **Rust** core that implements each storefront’s protocols (informed by public tools such as **SteamKit** and **Legendary**), including transfers, cloud saves, friends, chat, and an in-game overlay.

## Windows translation on Mac

Windows builds run through the bundled **Voile Wine** runtime. Per-game profiles choose **Rosetta-based Wine** or a **Linux compatibility engine backed by voile-lkd** for titles whose anti-cheat supports Linux/Proton, plus Metal graphics paths such as **D3DMetal** and **DXMT**.

## Anti-cheat stance

The project emphasizes **running games legitimately without modifying or bypassing anti-cheat**, while documenting engine choice, runtime contracts, and launch diagnostics for compatibility work on Mac.

## Research use

Suits players consolidating stores on Apple silicon and developers or researchers studying **storefront integration**, Wine-based translation, and **anti-cheat constraints on non-Windows platforms**—in the same **compatibility-with-AC-intact** lane as [[pointblank-linux]], [[proton]], and trackers such as [[are-we-anti-cheat-yet]] and [[aclist-github-io]].

## Stack

- **UI:** SwiftUI macOS front end.
- **Core:** Rust storefront protocol implementation (SteamKit/Legendary-informed).
- **Social / library:** Cloud saves, friends, chat, overlay without official clients.
- **Runtime:** Voile Wine; per-title Rosetta Wine vs voile-lkd Linux engine; D3DMetal/DXMT.

## Links

- Repo: https://github.com/Zagrios/Obelisk [Open-source Apple silicon macOS launcher for Steam/Epic/GOG with Voile Wine runtime and voile-lkd for Windows and Linux anti-cheat–supported titles]

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[pointblank-linux]] · [[crossover-patcher]] · [[proton]] · [[are-we-anti-cheat-yet]] · [[aclist-github-io]]
