---
title: ddma
kind: entity
topics: [dma-attack, windows-kernel]
sources:
  - wiki/sources/descriptions/btbd__ddma.md
updated: 2026-08-17
confidence: medium
---

# ddma

**ddma** (btbd/ddma) is a **proof-of-concept** for **disk-based DMA** on Windows using **HBA (host bus adapter) controllers** — ATA/SCSI storage-class devices that issue bus-master DMA against host RAM. Unlike FPGA [[pcileech]] cheat endpoints, this lane studies how **legitimate disk controllers** with unvirtualized passthrough can reach physical memory and bypass **hypervisor-level protections** such as **SLAT** (Second Level Address Translation / EPT). A kernel driver was demonstrated **modifying Hyper-V at runtime on bare metal** when the native hypervisor exposes unvirtualized device access. (source: wiki/sources/descriptions/btbd__ddma.md)

## Scope and limits

- **ATA only** in the published PoC; README also lists SCSI as a category label.
- **HBA 64-bit addressing** may cap reachable physical ranges.
- Aimed at **kernel and hypervisor security researchers** studying disk-based DMA attacks and SLAT bypass — distinct from game-cheat disk-class firmware such as [[ddma-1]] (gmh5225; external PCIe cheat with zero target-OS footprint).

## Links

- Repo: https://github.com/btbd/ddma

## Related

[[dma]] · [[ddma-1]] · [[pcileech]] · [[iommu]] · [[hvci]] · [[overviews/dma-attack]] · [[overviews/windows-kernel]]
