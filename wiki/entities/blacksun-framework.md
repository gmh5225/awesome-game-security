---
title: BlackSun Framework
kind: entity
topics: [game-hacking, windows-kernel, dma-attack, graphics-api]
sources:
  - wiki/sources/descriptions/cs1ime__blacksun-framework.md
updated: 2026-08-16
confidence: medium
---

# BlackSun Framework

Modular **C++ game cheat framework** (cs1ime) that separates **access backends** from cheat logic so researchers can swap how memory is reached without rewriting feature code. Backends cover **user-mode**, **kernel**, and **DMA** paths; shared infrastructure includes memory read/write abstractions, **pattern scanning**, **hooking** utilities, **overlay rendering**, and **communication layers**. Aimed at game-security researchers studying cheat-framework architecture and multi-backend memory-access patterns. (source: wiki/sources/descriptions/cs1ime__blacksun-framework.md)

Sits in the general-purpose cheat-framework lane beside [[lilypublic]] and [[cs2-ext]]; DMA-capable backends align with transport-agnostic memory libraries such as [[vm]] in [[overviews/dma-attack]].

## Links

- Repo: https://github.com/cs1ime/blacksun-framework

## Related

[[lilypublic]] · [[cs2-ext]] · [[vm]] · [[libmem]] · [[dobby]] · [[overviews/game-hacking]] · [[overviews/dma-attack]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
