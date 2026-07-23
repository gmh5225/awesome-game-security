---
title: DMA Attack
kind: overview
topics: [dma-attack]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md
  - wiki/sources/descriptions/un4ckn0wl3z__DMAInvoker.md
  - wiki/sources/descriptions/un4ckn0wl3z__DMACheatEngineLoader.md
  - wiki/sources/descriptions/ufrisk__pcileech.md
  - wiki/sources/descriptions/ufrisk__pcileech-fpga.md
  - wiki/sources/descriptions/tandasat__HelloIommuPkg.md
  - wiki/sources/descriptions/sonodima__physpatch.md
  - wiki/sources/descriptions/slack69__csgo-dma-overlay.md
  - wiki/sources/descriptions/sh1ftd__dma-speedtest-memflow-rs.md
updated: 2026-07-23
confidence: high
---


# DMA Attack

PCIe Direct Memory Access threat modeling for game security: FPGA endpoints (often M.2), host tools like [[pcileech]]/MemProcFS, and defenses that software anti-cheat alone cannot fully cover once a hostile bus-master can read RAM. (source: wiki/sources/skills/dma-attack.md)

## Threat model

Typical external DMA cheat: **cheat PC** + **DMA card** (Memory Read TLPs) + optional **HID actuator**. No attacker code need run on the gaming OS—the machine sees a PCIe device performing ordinary-looking DMA. [[pcileech]] is the common host app that drives PCIe hardware for target-memory R/W over DMA. (source: wiki/sources/descriptions/ufrisk__pcileech.md) FPGA HDL/firmware for those devices is [[pcileech-fpga]] (Vivado builds, TLP/BAR/config shadow across CaptainDMA, ScreamerM2, and related boards). (source: wiki/sources/descriptions/ufrisk__pcileech-fpga.md) Host tooling in the cheat / RPM lane includes DMALibrary wrappers such as [[dma-invoker]] (Windows DMA RPM). (source: wiki/sources/descriptions/un4ckn0wl3z__DMAInvoker.md) Hardware/throughput evaluation tools such as [[dma-speedtest-memflow-rs]] (Rust memflow CLI/GUI; PCILeech/native connectors; MiB/s + latency) sit in the same DMA measurement lane. (source: wiki/sources/descriptions/sh1ftd__dma-speedtest-memflow-rs.md) Cheat Engine DMA loaders such as [[dma-cheat-engine-loader]] (drop CE into `DMACE`; not open-source) sit in the same external CE/DMA research lane. (source: wiki/sources/descriptions/un4ckn0wl3z__DMACheatEngineLoader.md) Kernel-scan/patch research such as [[physpatch]] (page-table walk → physical-page write) shows the same physical-memory path used to alter Windows kernel memory while bypassing software hooks. (source: wiki/sources/descriptions/sonodima__physpatch.md) Title-specific DMA+overlay samples such as [[csgo-dma-overlay]] illustrate the cheat-app visualization layer for CS:GO. (source: wiki/sources/descriptions/slack69__csgo-dma-overlay.md)


## Key sub-areas

- **PCIe stack:** TLPs, Config Space, BAR probing, MSI/MSI-X, AER, link/ASPM behavior
- **Firmware tiers:** stock pcileech fingerprints → donor shadow config → BAR/MSI behavioral emulation
- **[[iommu]]:** VT-d / AMD-Vi domains, ACS, ATS trust, fault-rate monitoring, containment (sandbox domain, BME clear, DPC)
- **Hypervisor / attestation:** EPT protections, VBS/[[hvci]], TPM Quote + measured-boot PCRs
- **Thunderbolt/USB4:** hot-plug PCIe tunneling vs Kernel DMA Protection

## Defense layers

1. PCIe-layer fingerprinting (identity vs real silicon)
2. IOMMU enforcement (out-of-domain DMA) — sample DXE remapping programming in [[helloiommupkg]] (learning-only). (source: wiki/sources/descriptions/tandasat__HelloIommuPkg.md)
3. External attestation (IOMMU/kernel/boot chain integrity)
4. Firmware / pre-boot policy — e.g. BIOS DXE stripping PCI embedded option-ROM attributes and retuning NX ([[x670e-tomahawk-anticheat-update]]) (source: wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md)

## Related concepts

[[dma]] · [[iommu]] · [[helloiommupkg]] · [[hvci]] · [[byovd]] · [[pcileech]] · [[pcileech-fpga]] · [[physpatch]] · [[x670e-tomahawk-anticheat-update]] · [[dma-invoker]] · [[dma-speedtest-memflow-rs]] · [[dma-cheat-engine-loader]] · [[csgo-dma-overlay]] · [[overviews/anti-cheat]]


## README map

No top-level DMA section — maps via `Cheat` (~2575) DMA lanes and `Anti Cheat > Detection:DMA` (~607), plus hypervisor/virtualization/HWID detection and `Windows Security Features` (~9; TPM/IOMMU/VBS/HVCI attestation samples). (source: wiki/sources/README-categories.md)
