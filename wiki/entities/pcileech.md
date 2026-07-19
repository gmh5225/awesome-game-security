---
title: PCILeech
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ufrisk__pcileech.md
updated: 2026-07-19
confidence: medium
---

# PCILeech

Host-side tool that uses **PCIe hardware devices** to **read and write target system memory** via **DMA over PCIe**. Canonical stack entry for game-security and RE work in the cheat / DMA lane: FPGA endpoint + host app for physical-memory access without code running in the gaming OS. (source: wiki/sources/descriptions/ufrisk__pcileech.md)

## Links

- Repo: https://github.com/ufrisk/pcileech

## Related

[[dma]] · [[iommu]] · [[pcileech-fpga]] · [[dma-invoker]] · [[dma-cheat-engine-loader]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
