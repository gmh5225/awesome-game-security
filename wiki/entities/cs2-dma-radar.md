---
title: CS2-Dma-Radar
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__CS2-Dma-Radar.md
updated: 2026-08-14
confidence: medium
---

# CS2-Dma-Radar

**Counter-Strike 2** DMA-based radar cheat that reads game memory through **PCIe DMA hardware**. Extracts player positions and game state via direct memory access without running software on the target machine, then displays a **real-time radar overlay** on a separate host. The below-OS path avoids VAC process-level detection on the gaming PC. Aimed at game security researchers studying DMA radar architectures for Source 2 titles. (source: wiki/sources/descriptions/gmh5225__CS2-Dma-Radar.md)

Complements external CS2 radar samples such as [[cs2-webradar]] (browser-streamed entity map) and native overlays such as [[proext]] / [[titled-gui-cs2]] by illustrating a zero-target-software PCIe DMA stack beside EFT DMA radars such as [[eft-dma-radar-1]].

## Links

- Repo: https://github.com/gmh5225/CS2-Dma-Radar

## Related

[[cs2-webradar]] · [[proext]] · [[titled-gui-cs2]] · [[cs2-offsets]] · [[cs2-external-1]] · [[eft-dma-radar-1]] · [[csgo-dma-overlay]] · [[dma]] · [[pcileech]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
