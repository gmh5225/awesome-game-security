---
title: DMALibrary
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Metick__DMALibrary.md
updated: 2026-08-23
confidence: medium
---

# DMALibrary

**C++ DMA toolkit** (Metick) for external memory access and system inspection over hardware DMA paths. Wraps common LeechCore/MemProcFS workflows with signature scanning, normal and scatter read/write, memory dumping, CR3-fix helpers, PID and module-base lookup, and import/export parsing utilities. Primary use case: advanced game-security research and cheat tooling that reads game state from a separate host without target-OS process APIs. Listed under cheat / DMA library. (source: wiki/sources/descriptions/Metick__DMALibrary.md)

## Capabilities

- Signature (pattern) scanning; normal and scatter memory read/write
- Memory dumps; CR3/DTB fix helpers for page-table walks
- Process ID and image-base resolution; PE import/export parsing helpers
- Designed to integrate with LeechCore and MemProcFS dependencies supplied at link/runtime

## Links

- Repo: https://github.com/Metick/DMALibrary

## Related

[[dma]] · [[dmalib]] · [[volk-dma]] · [[dma-invoker]] · [[pcileech]] · [[cheat-engine-dma-plugin]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
