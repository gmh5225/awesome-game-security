---
title: PhysPatch
kind: entity
topics: [dma-attack, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/sonodima__physpatch.md
updated: 2026-07-22
confidence: medium
---

# PhysPatch

Tool for **scanning and patching the Windows kernel via physical memory** (DMA lane). Walks page tables to translate virtual → physical addresses, then writes physical pages directly so changes bypass software-level memory protection and kernel API / access-monitoring hooks. Aimed at kernel researchers studying physical-memory manipulation and integrity implications for anti-cheat and security products. (source: wiki/sources/descriptions/sonodima__physpatch.md)

## Links

- Repo: https://github.com/sonodima/physpatch

## Related

[[dma]] · [[pcileech]] · [[overviews/dma-attack]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
