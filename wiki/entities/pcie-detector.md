---
title: PCIE-Detector
kind: entity
topics: [dma-attack, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__PCIE-Detector.md
updated: 2026-08-11
confidence: medium
---

# PCIE-Detector

Kernel-level **PCIe Config Space** inspection tooling (C++; Windows driver development) for **defensive DMA detection research**. Targets anti-cheat engineers and defensive security researchers validating capability chains, BAR masks, and extended config headers in the `Anti Cheat > Detection:DMA` lane. (source: wiki/sources/descriptions/gmh5225__PCIE-Detector.md)

## Detection relevance

Complements offensive [[pcileech-fpga]] / [[pcileechgen]] firmware tiers by exercising the same **Config Space** probes outlined in [[dma]]—legacy 256-byte headers, extended capabilities (AER, DSN, ATS), BAR mask walks, and R/W consistency checks—from a kernel driver perspective rather than user-mode inventory alone.

## Links

- Repo: https://github.com/gmh5225/PCIE-Detector

## Related

[[dma]] · [[pcileech]] · [[pcileech-fpga]] · [[pcileechgen]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
