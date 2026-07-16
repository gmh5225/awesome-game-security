---
title: DMA Attack
kind: overview
topics: [dma-attack]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/README-categories.md
updated: 2026-07-16
confidence: high
---

# DMA Attack

PCIe Direct Memory Access threat modeling for game security: FPGA endpoints (often M.2), host tools like pcileech/MemProcFS, and defenses that software anti-cheat alone cannot fully cover once a hostile bus-master can read RAM. (source: wiki/sources/skills/dma-attack.md)

## Threat model

Typical external DMA cheat: **cheat PC** + **DMA card** (Memory Read TLPs) + optional **HID actuator**. No attacker code need run on the gaming OS—the machine sees a PCIe device performing ordinary-looking DMA.

## Key sub-areas

- **PCIe stack:** TLPs, Config Space, BAR probing, MSI/MSI-X, AER, link/ASPM behavior
- **Firmware tiers:** stock pcileech fingerprints → donor shadow config → BAR/MSI behavioral emulation
- **[[iommu]]:** VT-d / AMD-Vi domains, ACS, ATS trust, fault-rate monitoring, containment (sandbox domain, BME clear, DPC)
- **Hypervisor / attestation:** EPT protections, VBS/[[hvci]], TPM Quote + measured-boot PCRs
- **Thunderbolt/USB4:** hot-plug PCIe tunneling vs Kernel DMA Protection

## Defense layers

1. PCIe-layer fingerprinting (identity vs real silicon)
2. IOMMU enforcement (out-of-domain DMA)
3. External attestation (IOMMU/kernel/boot chain integrity)

## Related concepts

[[dma]] · [[iommu]] · [[hvci]] · [[byovd]] · [[overviews/anti-cheat]]

## README map

`Cheat > DMA`, `Anti Cheat > Detection:DMA`, hypervisor/virtualization/HWID detection, `Windows Security Features`. (source: wiki/sources/README-categories.md)
