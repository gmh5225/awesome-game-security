---
title: eac_cr3_shuffle
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/SamuelTulach__eac_cr3_shuffle.md
updated: 2026-08-21
confidence: medium
---

# eac_cr3_shuffle

**eac_cr3_shuffle** (SamuelTulach) is a compact C++ research sample focused on **CR3 shuffling behavior** in [[easy-anti-cheat]]-protected environments. The code demonstrates low-level paging primitives—physical memory range walking, directory-base discovery, and virtual-to-physical translation checks—and ships with reference material explaining why CR3 manipulation complicates external memory inspection workflows. Primary use case: reverse engineering and anti-cheat internals research, especially page-table-related protection strategies. README category: cheat / Bypassing CR3 protection. (source: wiki/sources/descriptions/SamuelTulach__eac_cr3_shuffle.md)

Distinct from full UM+KM bypass stacks such as [[eac-cr3-bypass]]—this repo emphasizes **observing and reasoning about CR3 shuffle mechanics** rather than delivering a coordinated driver bypass. Complements cross-process translate libraries such as [[ntmemory]] and protected-process access PoCs such as [[meme-rw]] from the same author.

## Links

- Repo: https://github.com/SamuelTulach/eac_cr3_shuffle

## Related

[[easy-anti-cheat]] · [[eac-cr3-bypass]] · [[ntmemory]] · [[meme-rw]] · [[windows-kernel-pagehook]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
