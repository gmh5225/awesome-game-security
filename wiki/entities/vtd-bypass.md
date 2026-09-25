---
title: VTD-Bypass
kind: entity
topics: [dma-attack, windows-kernel, anti-cheat]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/kEv1nZ0__VTD-Bypass.md
updated: 2026-09-25
confidence: medium
---

# VTD-Bypass

Python tool (kEv1nZ0/VTD-Bypass) that automates bypassing VT-d and IOMMU-related detection by reading and modifying ACPI tables in host physical memory via LeechCore over FPGA DMA hardware. Listed in README **Cheat → VT-d/IOMMU**. (source: wiki/sources/descriptions/kEv1nZ0__VTD-Bypass.md)

## Workflow

1. Dump host physical memory over **LeechCore** on FPGA DMA hardware
2. Locate the **XSDT** ACPI table via signature search
3. Fabricate a checksum-valid **DMAR** table (DRHD base in high MMIO; 4KB-aligned hole selection)
4. Patch XSDT so the OS reports **VT-d enabled** when firmware has it disabled
5. Apply **repeated timed writes during boot** so patches persist through early firmware/OS table reads

## Techniques

- Signature-based ACPI table discovery in physical memory
- 4KB-aligned hole selection for injected table placement
- DRHD base address placement in high MMIO space
- Encrypted configuration files for operator-controlled parameters
- Boot-window timed physical-memory writes (physical DMA, not driver-mediated IOMMU edits)

## Positioning

Offensive **IOMMU/ACPI spoofing** lane beside kernel remapping PoCs such as [[diedmaprotection]] and defensive samples such as [[dmaprotect]]—fabricates firmware-visible VT-d state rather than reprogramming remapping tables from ring 0. Targets hardware security research, ACPI/IOMMU analysis, and anti-cheat testing where VT-d enforcement is checked. (source: wiki/sources/descriptions/kEv1nZ0__VTD-Bypass.md)

## Requirements

Windows host, Python 3.9–3.11, leechcorepyc, and external DMA libraries. (source: wiki/sources/descriptions/kEv1nZ0__VTD-Bypass.md)

## Links

- Repo: https://github.com/kEv1nZ0/VTD-Bypass

## Related

[[pcileech]] · [[pcileech-fpga]] · [[iommu]] · [[diedmaprotection]] · [[dmaprotect]] · [[sewindows]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
