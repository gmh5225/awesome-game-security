---
title: ceserver-rawmem
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/cs1ime__ceserver-rawmem.md
updated: 2026-08-16
confidence: medium
---

# ceserver-rawmem

**Cheat Engine ceserver** implementation that reads target process memory through **raw physical memory access** (e.g. `/dev/mem` or DMA) instead of standard process memory APIs. It implements the **ceserver network protocol** for remote Cheat Engine connections while bypassing OS-level memory access protections and anti-cheat monitoring—aimed at security researchers studying physical memory-based CE configurations and DMA attack scenarios. (source: wiki/sources/descriptions/cs1ime__ceserver-rawmem.md)

Complements [[cheat-engine-ceserver-pcileech]] when the backend is generic physical RAM rather than a PCILeech/LeechCore stack, and in-CE DMA plugins such as [[cheat-engine-dma-plugin]] when the workflow is remote ceserver over raw memory instead of a local CE plugin swap.

## Links

- Repo: https://github.com/cs1ime/ceserver-rawmem

## Related

[[cheat-engine-ceserver-pcileech]] · [[cheat-engine-dma-plugin]] · [[dma-cheat-engine-loader]] · [[pcileech]] · [[concepts/dma]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
