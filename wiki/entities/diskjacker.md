---
title: Diskjacker
kind: entity
topics: [dma-attack, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/LabGuy94__Diskjacker.md
updated: 2026-08-23
confidence: medium
---

# Diskjacker

**Diskjacker** (LabGuy94) is a **proof-of-concept** for **runtime Hyper-V VM-exit hijacking** using a **DMA-based (DDMA-style)** approach. It combines **C++ kernel and usermode** components with **assembly stubs** for low-level mapping and execution transfer. The workflow depends on specific **virtualization and hardware preconditions** and demonstrates adapting **[[ddma]]**-class disk-controller DMA primitives to **hypervisor security research** rather than general application development. (source: wiki/sources/descriptions/LabGuy94__Diskjacker.md)

Contrasts with boot-time Hyper-V loaders such as [[modded-voyager]] and in-guest Hyper-V RE frameworks such as [[voyager]] / [[hyper-rev]] by targeting **live VM-exit dispatch** after the OS is running. Complements btbd **[[ddma]]** Hyper-V runtime modification research on the same DDMA primitive lane.

## Links

- Repo: https://github.com/LabGuy94/Diskjacker

## Related

[[ddma]] · [[ddma-1]] · [[voyager]] · [[modded-voyager]] · [[hyper-rev]] · [[hyperdeceit]] · [[hvci]] · [[overviews/dma-attack]] · [[overviews/windows-kernel]]
