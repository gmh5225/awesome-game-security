---
title: Unispect DMA Plugin
kind: entity
topics: [dma-attack, game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__unispectDMAPlugin.md
updated: 2026-08-07
confidence: medium
---

# Unispect DMA Plugin

**gmh5225** fork of Razchek's Unispect that combines **Unity Mono runtime dump** with **external DMA memory access**. Targets game-security researchers and reverse engineers working in the cheat / game engine explorer:Unity lane who need Unispect-style Mono metadata extraction without conventional in-process reads on the gaming OS. (source: wiki/sources/descriptions/gmh5225__unispectDMAPlugin.md)

This fork fixes a bug in the original Unispect branch where **Memory Plugins are not disposed after dumping**, which can leave stale plugin state across dump cycles. (source: wiki/sources/descriptions/gmh5225__unispectDMAPlugin.md)

## Links

- Repo: https://github.com/gmh5225/unispectDMAPlugin

## Related

[[dma]] · [[pcileech]] · [[cheat-engine-dma-plugin]] · [[unityexplorer]] · [[mono]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
