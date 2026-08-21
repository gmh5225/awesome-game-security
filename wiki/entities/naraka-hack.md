---
title: Naraka-Hack
kind: entity
topics: [game-hacking, game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/Rythorndoran__Naraka-Hack.md
updated: 2026-08-21
confidence: medium
---

# Naraka-Hack

**External** cheat-style implementation for **NARAKA: BLADEPOINT** (Unity IL2CPP). C++ code maintains **offset tables**, reads **entity and player state** from process memory, and draws **ESP-style** boxes and names through an **NVIDIA overlay** window. Includes hotkey-driven menu controls and automation-oriented **combat assistance**. Primarily used for cheat-development practice and reverse engineering of game runtime structures. (source: wiki/sources/descriptions/Rythorndoran__Naraka-Hack.md)

Complements version-pinned metadata scaffolding such as [[dummy-dlls-naraka-1-9-21]] with a live external workflow: offset maintenance, RPM entity traversal, and overlay rendering without in-process IL2CPP hooks. Useful for comparing NVIDIA overlay draw paths ([[nvidia-overlay]], [[nvidia-overlay-hijack]]) against Present-hook internals on Unity battle-royale titles.

## Links

- Repo: https://github.com/Rythorndoran/Naraka-Hack

## Related

[[dummy-dlls-naraka-1-9-21]] · [[il2cpp]] · [[world-to-screen]] · [[nvidia-overlay]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
