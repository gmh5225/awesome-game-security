---
title: CS2-DMA-Cheat
kind: entity
topics: [dma-attack, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/eden13378__CS2-DMA-Cheat.md
updated: 2026-08-16
confidence: medium
---

# CS2-DMA-Cheat

**Counter-Strike 2** DMA-based cheat research sample written in **C/C++** that reads game memory through **PCIe DMA hardware** rather than injecting into the target process. The project centers on **shader work, rendering, and audio systems** for below-OS visual and feedback features on a separate host machine. Useful for game security researchers and reverse engineers studying offensive DMA techniques in the cheat / game:cs2 lane. (source: wiki/sources/descriptions/eden13378__CS2-DMA-Cheat.md)

Complements CS2 DMA radar samples such as [[cs2-dma-radar]] by illustrating a fuller cheat stack (rendering/audio) beside radar-only overlays; contrasts with in-process CS2 samples such as [[cs2-cheat-cpp]] and external overlays such as [[proext]] by keeping attacker logic off the gaming OS.

## Links

- Repo: https://github.com/eden13378/CS2-DMA-Cheat

## Related

[[cs2-dma-radar]] · [[cs2-cheat-cpp]] · [[proext]] · [[cs2-webradar]] · [[gta5-dma-cheat]] · [[fn-dma-cheat]] · [[csgo-dma-overlay]] · [[dma]] · [[pcileech]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
