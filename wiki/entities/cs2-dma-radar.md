---
title: CS2-Dma-Radar
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__CS2-Dma-Radar.md
  - wiki/sources/descriptions/MoZiHao__CS2_DMA_Radar.md
updated: 2026-08-23
confidence: medium
---

# CS2-Dma-Radar

**Counter-Strike 2** DMA-based radar cheats share this name in the curated list—below-OS stacks that read game memory through **PCIe DMA hardware** (VMM/LeechCore) without running software on the target machine, then render player positions and game state on a separate host. Aimed at game security researchers studying DMA radar architectures for Source 2 titles.

## gmh5225/CS2-Dma-Radar

Counter-Strike 2 DMA-based radar cheat that reads game memory through **PCIe DMA hardware**. Extracts player positions and game state via direct memory access, then displays a **real-time radar overlay** on a separate host. The below-OS path avoids VAC process-level detection on the gaming PC. (source: wiki/sources/descriptions/gmh5225__CS2-Dma-Radar.md)

## MoZiHao/CS2_DMA_Radar

Counter-Strike 2 DMA radar that streams game state into a **browser-based tactical map** via a Java **Spring Boot** backend with **WebSocket** and a **Leaflet/JavaScript** frontend for live rendering. The backend reads memory through VMM and LeechCore interfaces; map assets and icons support multiple competitive maps and player markers. Primarily used for external situational-awareness experiments in game security and anti-cheat research contexts. (source: wiki/sources/descriptions/MoZiHao__CS2_DMA_Radar.md)

Complements external CS2 radar samples such as [[cs2-webradar]] (browser-streamed entity map without DMA) and native overlays such as [[proext]] / [[titled-gui-cs2]] by illustrating below-OS PCIe DMA stacks beside EFT DMA radars such as [[eft-dma-radar-1]].

## Links

- Repo (gmh5225): https://github.com/gmh5225/CS2-Dma-Radar
- Repo (MoZiHao): https://github.com/MoZiHao/CS2_DMA_Radar

## Related

[[cs2-dma]] · [[cs2-dma-cheat]] · [[cs2-webradar]] · [[proext]] · [[titled-gui-cs2]] · [[cs2-offsets]] · [[cs2-external-1]] · [[eft-dma-radar-1]] · [[csgo-dma-overlay]] · [[dma]] · [[pcileech]] · [[memprocfs-analyzer]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]
