---
title: DMALib
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Spuckwaffel__DMALib.md
updated: 2026-08-20
confidence: medium
---

# DMALib

Lightweight **C++ DMA helper library** (Spuckwaffel) for game memory access workflows. Wraps common operations—process lookup, base address retrieval, memory read/write, pattern scanning, and scatter reads—over externally supplied **LeechCore** and **MemProcFS** libraries. Primary use case: building DMA-based game security research tools with cleaner reusable code instead of raw VMMDLL/LeechCore calls. Listed under cheat / DMA library. (source: wiki/sources/descriptions/Spuckwaffel__DMALib.md)

## Capabilities

- Process and module resolution; typed memory read/write
- Pattern (signature) scanning; scatter read batching
- Integrates with LeechCore/MemProcFS backends supplied at link/runtime

## Links

- Repo: https://github.com/Spuckwaffel/DMALib

## Related

[[dma]] · [[volk-dma]] · [[dma-invoker]] · [[pcileech]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
