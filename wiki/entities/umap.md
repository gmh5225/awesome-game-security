---
title: umap
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/btbd__umap.md
updated: 2026-08-17
confidence: medium
---

# umap

**umap** (btbd/umap) is a minimalist **Windows kernel driver mapper** in C that manually maps an unsigned driver into kernel memory from user mode. It uses a **vulnerable signed driver** for physical memory access to allocate kernel pool space, copy PE sections, process relocations, resolve imports, and invoke the mapped driver's entry point — all without creating registry traces or loading through standard driver-loading paths. Aimed at kernel researchers studying stealthy driver mapping techniques and their detection vectors. (source: wiki/sources/descriptions/btbd__umap.md)

Sits in the kdmapper-family manual-map lane beside [[kdmapper]], [[known-driver-mappers]], and other BTBD research such as [[wpp]] and [[driver-hwid-btbd-modified]].

## Links

- Repo: https://github.com/btbd/umap

## Related

[[kdmapper]] · [[known-driver-mappers]] · [[byovd]] · [[wpp]] · [[driver-hwid-btbd-modified]] · [[revert-mapper]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[kernel-pool-scanning]]
