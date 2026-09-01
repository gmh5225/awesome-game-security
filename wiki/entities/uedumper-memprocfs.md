---
title: UEDumper-MemProcFS
kind: entity
topics: [game-engine, game-hacking, reverse-engineering, dma-attack]
sources:
  - wiki/sources/descriptions/BadBrojo__UEDumper-MemProcFS.md
updated: 2026-09-01
confidence: medium
---

# UEDumper-MemProcFS

**All-in-one Unreal Engine dumper and live editor** (BadBrojo; C++) for runtime SDK extraction and memory inspection. ImGui UI with configurable offsets and engine definitions across UE **4.19–5.2**. Modules cover SDK generation, class browsing, and live read/write, backed by **MemProcFS / LeechCore-style** memory backends for external physical-memory access—useful when in-process injection is blocked or when operating from a DMA cheat PC. Primary use case: Unreal game reverse engineering and game-security analysis. Listed under cheat / SDK Dump. (source: wiki/sources/descriptions/BadBrojo__UEDumper-MemProcFS.md)

Sits beside the upstream [[uedumper]] (Spuckwaffel; local process memory) and DMA-assisted RE tooling such as [[pcileech-memprocfs-mcp]] by pairing the same UE dumper/editor workflow with the canonical [[pcileech]] / MemProcFS stack rather than standard process-handle reads.

## Links

- Repo: https://github.com/BadBrojo/UEDumper-MemProcFS

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/dma-attack]] · [[unreal-object-model]] · [[uedumper]] · [[ezfndev-uedumper]] · [[shh0yauedumper]] · [[dumper-7]] · [[pcileech]] · [[pcileech-memprocfs-mcp]] · [[memprocfs-analyzer]] · [[volk-dma]]
