---
title: StrataDMA
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/chase-irql__StrataDMA.md
updated: 2026-10-16
confidence: medium
---

# StrataDMA

Cross-platform **C++17 static library** (chase-irql) that wraps **MemProcFS** and **VMMDLL** for authorized direct memory access inspection of live Windows targets from a 64-bit Windows or Linux analysis host. Provides a structured, production-oriented facade over FPGA or similar LeechCore DMA setups for forensic, reverse-engineering, and game-security workflows. (source: wiki/sources/descriptions/chase-irql__StrataDMA.md)

## Capabilities

- Configurable device initialization; process attach by name or PID
- Strict typed memory read APIs with scatter batches and frame caching
- Module and symbol tooling; signature scanning; **CR3 recovery**; PE dumping
- Registry and VFS access; rich OS inspection tables; optional input polling
- CMake and Visual Studio builds; vendors LeechCore and MemProcFS headers
- Mock-backed tests that run without DMA hardware

## Links

- Repo: https://github.com/chase-irql/StrataDMA

## Related

[[dma]] · [[pcileech]] · [[volk-dma]] · [[dmalib]] · [[dmalibrary]] · [[vm]] · [[pcileech-memprocfs-mcp]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
