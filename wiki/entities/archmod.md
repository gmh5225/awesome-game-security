---
title: ArchMod
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/BlaMacfly__ArchMod.md
updated: 2026-08-30
confidence: medium
---

# ArchMod

**ArchMod** (BlaMacfly/ArchMod) is a native **Linux cheat panel** for **Steam games running under Proton**, offering a WeMod-like trainer experience without Windows. Built with a **Rust + Tauri 2** backend and **React** frontend, it scans Steam libraries, manages a trainer vault, and injects Windows trainer executables into the correct Proton prefix via **protontricks** and native fallbacks. (source: wiki/sources/descriptions/BlaMacfly__ArchMod.md)

Its in-progress native engine reads and writes game memory directly on Linux through **`process_vm_readv`**, supporting byte-pattern scanning, pointer-chain resolution, value freezing, code hooks, and **Cheat Engine table** parsing. Community profiles let researchers share memory addresses and cheat definitions per game build. Targets Linux gamers and reverse engineers who want single-player trainer support and memory manipulation on Proton, with explicit warnings about anti-cheat and multiplayer use.

## Links

- Repo: https://github.com/BlaMacfly/ArchMod

## Related

[[proton]] · [[cheat-engine]] · [[freeplay]] · [[cttrainer]] · [[elden-ring-ct-tga]] · [[counterstrikesource-linux-trainer]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
