---
title: x670e-tomahawk-anticheat-update
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md
updated: 2026-07-17
confidence: medium
---

# x670e-tomahawk-anticheat-update

Reverse-engineering notes on the MSI MAG X670E TOMAHAWK WIFI BIOS **v1KB** “anti-cheat” update: two DXE-phase changes aimed at DMA cheat hardware and memory NX policy. (source: wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md)

## Documented DXE changes

1. **PCI option-ROM attribute strip** — Bds clears `EFI_PCI_IO_ATTRIBUTE_EMBEDDED_ROM` pre-boot, reducing option-ROM execution paths that DMA/FPGA endpoints can abuse.
2. **DxeCore NX policy retune** — adjusts NX memory-protection policy in the DXE core.

Useful as a firmware-layer companion to [[iommu]] / PCIe fingerprinting defenses in the [[dma]] threat model—not a runtime anti-cheat product.

## Links

- Repo: https://github.com/zer0condition/x670e-tomahawk-anticheat-update

## Related

[[dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
