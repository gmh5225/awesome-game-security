---
title: Lucid Tarkov DMA
kind: entity
topics: [dma-attack, game-hacking]
sources:
  - wiki/sources/descriptions/Shurtug__LucidTarkovDMA.md
updated: 2026-11-19
confidence: medium
---

# Lucid Tarkov DMA

**Escape From Tarkov** external hardware-assisted stack that runs on a **second PC** and reaches the gaming machine only through a **PCIe DMA** link, so nothing is injected in-process on the game host. It reads **IL2CPP** game memory for player ESP, loot and corpse overlays (with flea-market values), a **LAN web radar and dashboard**, and optional memory writes (recoil, vision, stamina, interaction). An optional **MAKCU USB** device can drive aim input as ordinary HID mouse traffic. The product centers on commercial DMA cards, a second-host launcher with over-the-air updates after patches, and in-house offsets for **BattlEye**-protected builds—aimed at researchers studying hardware DMA cheating and how external tooling evades traditional in-process anti-cheat. (source: wiki/sources/descriptions/Shurtug__LucidTarkovDMA.md)

Contrasts with radar-only DMA samples such as [[eft-dma-radar-1]] and MemProcFS toolboxes such as [[eftleecher]] by bundling ESP, web radar, optional gameplay writes, and HID aim on one second-host stack with zero gaming-OS footprint.

## Links

- Repo: https://github.com/Shurtug/LucidTarkovDMA

## Related

[[dma]] · [[pcileech]] · [[meatyeftrelease]] · [[eft-dma-radar-1]] · [[eftleecher]] · [[nathans-tarkov-radar-public]] · [[hirschgang-ware]] · [[il2cpp]] · [[battleye]] · [[hardware-input-injection]] · [[overviews/dma-attack]] · [[overviews/game-hacking]]