---
title: VolkDMA
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/lyk64__VolkDMA.md
updated: 2026-08-09
confidence: medium
---

# VolkDMA

C++ **DMA library** for FPGA-based out-of-band physical memory access on Windows x64. Wraps **LeechCore** and **MemProcFS** with RAII session management for remote memory analysis, manipulation, reverse engineering, and debugging without running attacker code on the gaming OS. (source: wiki/sources/descriptions/lyk64__VolkDMA.md)

## Capabilities

- Process and module enumeration; typed reads/writes; pointer-chain resolution
- Scatter I/O, signature scanning, virtual-to-physical address translation
- **CR3 fixing** via patched VMM binaries (page-table walk stability on live targets)
- **Kernel-derived input state API** — cursor position and keyboard/mouse button state from kernel structures, avoiding local hooks on the cheat PC

Ships as a static library with bundled runtime DLLs. Targets researchers and developers building game-security tooling, anti-cheat analysis workflows, and low-level debugging over PCIe DMA. (source: wiki/sources/descriptions/lyk64__VolkDMA.md)

## Links

- Repo: https://github.com/lyk64/VolkDMA

## Related

[[dma]] · [[pcileech]] · [[dma-invoker]] · [[cheat-engine-dma-plugin]] · [[meatyeftrelease]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
