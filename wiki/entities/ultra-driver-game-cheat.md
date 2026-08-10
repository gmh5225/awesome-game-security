---
title: UltraDriver Game Cheat
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__UltraDriver-Game-Cheat.md
updated: 2026-08-10
confidence: medium
---

# UltraDriver Game Cheat

Kernel **driver-based game cheat framework** using a custom Windows driver for privileged cross-process memory access. Implements read/write via **physical address translation** or **MDL mapping**, bypassing anti-cheat **handle protections**, with a user-mode communication interface for cheat applications. Aimed at kernel researchers studying driver-based cheat architectures and anti-cheat kernel-level detection. (source: wiki/sources/descriptions/gmh5225__UltraDriver-Game-Cheat.md)

Sits in the Cheat Driver lane beside KM R/W samples such as [[ntmemory]], [[readwrite-kernel-stable]], and [[cheat-driver]].

## Links

- Repo: https://github.com/gmh5225/UltraDriver-Game-Cheat

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[ntmemory]] · [[readwrite-kernel-stable]] · [[cheat-driver]]
