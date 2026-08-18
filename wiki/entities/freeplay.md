---
title: Freeplay
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/antaresjay__freeplay.md
updated: 2026-08-18
confidence: medium
---

# Freeplay

Open-source **Windows game trainer** written in **Rust** that discovers installed games, attaches to single-player processes, and modifies memory through pointer scans, value freezing, and instruction patching. Games are configured with **TOML table files** instead of hard-coded logic; the tool imports **Cheat Engine `.CT` tables** and runs **Auto Assembler** scripts via a built-in x86/x64 assembler that allocates code caves and hooks instructions. (source: wiki/sources/descriptions/antaresjay__freeplay.md)

Ships a **Tauri** desktop app with an in-game overlay, a CLI, and access to a community library of converted cheat tables ranked by user feedback. Integrates with **Steam, Epic, and GOG** libraries; supports 32-bit and 64-bit targets. Refuses to attach to processes protected by anti-cheat systems such as [[easy-anti-cheat]], [[battleye]], and [[vanguard]] — aimed at offline and single-player modification as a transparent, self-hosted alternative to commercial trainers.

## Links

- Repo: https://github.com/antaresjay/freeplay

## Related

[[cheat-engine]] · [[mydev-cheat-engine-tables]] · [[intro-to-gamehacking]] · [[chasm]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
