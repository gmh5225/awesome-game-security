---
title: NTMemory
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/zer0condition__NTMemory.md
updated: 2026-07-17
confidence: medium
---

# NTMemory

Windows kernel memory manipulation library in C: cross-process read/write/allocate from kernel mode via **MDL mapping**, physical-memory translation, and **CR3-based page-table walking**, bypassing API-level protections. Research aid for studying kernel-mode cheat memory access and AC-evasion techniques. (source: wiki/sources/descriptions/zer0condition__NTMemory.md)

README framing also covers a usermode NT explorer surface (query kernel addresses, VA→PA, PFN database inspection) alongside the kernel R/W primitives.

## Links

- Repo: https://github.com/zer0condition/NTMemory

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[byovd]] · [[hvci]] · [[demystifying-patchguard]]
