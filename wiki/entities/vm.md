---
title: vm (ekknod)
kind: entity
topics: [game-hacking, dma-attack, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/ekknod__vm.md
updated: 2026-08-15
confidence: medium
---

# vm (ekknod)

Cross-platform **C/C++ memory access library** with a unified `vm.h` API for remote process read/write and module enumeration across multiple transports. Game-facing cheat or analysis code can swap backends without rewriting lookup, translation, or scan logic. (source: wiki/sources/descriptions/ekknod__vm.md)

## Backends

Each backend implements the same interface:

- **Windows kernel-mode** — EPROCESS / ActiveProcessLinks process walks
- **Windows user-mode** — `ReadProcessMemory` / `WriteProcessMemory`
- **Linux** — `/proc/pid/mem`
- **DMA** — [[pcileech]] via VMMDLL / LeechCore
- **KVM** — QEMU guest introspection
- **Proton** — Linux-hosted Windows games
- **EFI variables** — kernel communication through UEFI runtime

## Capabilities

- Process lookup, CR3-based page-table translation, PEB/LDR module walking, pattern scanning

Targets game-security researchers and cheat developers studying cross-platform remote memory access and DMA/KVM read-write primitives. (source: wiki/sources/descriptions/ekknod__vm.md)

## Links

- Repo: https://github.com/ekknod/vm

## Related

[[pcileech]] · [[volk-dma]] · [[ntmemory]] · [[dma]] · [[overviews/game-hacking]] · [[overviews/dma-attack]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
