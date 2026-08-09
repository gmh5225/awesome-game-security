---
title: cheat-engine-ceserver-pcileech
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__cheat-engine-ceserver-pcileech.md
updated: 2026-08-09
confidence: medium
---

# cheat-engine-ceserver-pcileech

**Cheat Engine ceserver** that implements the **ceserver network protocol** over a **PCILeech/LeechCore** backend for **DMA-based** memory access. A desktop Cheat Engine client connects to the server on a separate machine; scan and edit operations traverse DMA hardware rather than in-process APIs, so the target gaming OS does not observe conventional CE process-memory access—aimed at DMA security researchers who want familiar CE workflows on an external PCIe path. (source: wiki/sources/descriptions/gmh5225__cheat-engine-ceserver-pcileech.md)

Complements in-CE DMA plugins such as [[cheat-engine-dma-plugin]] and closed loaders such as [[dma-cheat-engine-loader]] when the workflow is remote ceserver over [[pcileech]] rather than a local CE plugin swap. Other ceserver backends include Frida attach ([[frida-ceserver]]) and WASM targets ([[wasm-ceserver]]).

## Links

- Repo: https://github.com/gmh5225/cheat-engine-ceserver-pcileech

## Related

[[pcileech]] · [[cheat-engine-dma-plugin]] · [[dma-cheat-engine-loader]] · [[frida-ceserver]] · [[wasm-ceserver]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
