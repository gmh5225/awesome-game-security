---
title: DMA (Direct Memory Access)
kind: concept
topics: [dma-attack, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md
  - wiki/sources/descriptions/un4ckn0wl3z__DMAInvoker.md
  - wiki/sources/descriptions/un4ckn0wl3z__DMACheatEngineLoader.md
  - wiki/sources/descriptions/ufrisk__pcileech.md
  - wiki/sources/descriptions/ufrisk__pcileech-fpga.md
  - wiki/sources/descriptions/sonodima__physpatch.md
  - wiki/sources/descriptions/slack69__csgo-dma-overlay.md
  - wiki/sources/descriptions/sh1ftd__dma-speedtest-memflow-rs.md
  - wiki/sources/descriptions/realquantumstealth-hub__PCILeech-DMA-Fullstealth.md
  - wiki/sources/descriptions/sercanarga__fpga-dma-multi-tool.md
updated: 2026-07-27
confidence: high
---


# DMA (Direct Memory Access)

Hardware-level memory access where a PCIe device issues Memory Read/Write TLPs against host RAM via Bus Master, without executing attacker code in the gaming OS. In game security this usually means an FPGA card (often M.2) linked to a separate cheat PC. (source: wiki/sources/skills/dma-attack.md) Host tooling such as [[pcileech]] drives those PCIe devices for target-memory R/W over DMA. (source: wiki/sources/descriptions/ufrisk__pcileech.md) Device firmware/HDL for those endpoints lives in [[pcileech-fpga]] (Vivado flows, TLP/BAR/config-space shadow across many boards). (source: wiki/sources/descriptions/ufrisk__pcileech-fpga.md) Fullstealth-oriented builds such as [[pcileech-dma-fullstealth]] (Quantumstealth; M2/Squirrel/Captain 75T/Enigma X1) extend that firmware lane for stealth/threat-modeling research. (source: wiki/sources/descriptions/realquantumstealth-hub__PCILeech-DMA-Fullstealth.md)

## Why it matters

Software anti-cheat sees a “normal” PCIe endpoint. Classic process/handle/injection signals may be absent. Defense shifts to PCIe fingerprinting, [[iommu]] policy, hypervisor containment, TPM/measured-boot attestation, and occasionally firmware-level blocks (e.g. BIOS DXE option-ROM attribute stripping in [[x670e-tomahawk-anticheat-update]]). (source: wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md) Physical-page patching tools such as [[physpatch]] (VA→PA walk then direct physical write) illustrate how DMA-class access can alter kernel memory while bypassing software hooks and access monitors. (source: wiki/sources/descriptions/sonodima__physpatch.md)


## Typical stack

Cheat app → LeechCore/pcileech/MemProcFS → FPGA firmware → Memory Read TLPs → walk CR3/page tables → game state; optional HID actuator for input. Host-side DMA RPM wrappers such as [[dma-invoker]] (DMALibrary-backed) sit in the cheat-app layer for Windows process-memory reads. (source: wiki/sources/descriptions/un4ckn0wl3z__DMAInvoker.md) Benchmarks such as [[dma-speedtest-memflow-rs]] (memflow; PCILeech/native; throughput/latency) help characterize that hardware path. (source: wiki/sources/descriptions/sh1ftd__dma-speedtest-memflow-rs.md) Windows board utilities such as [[fpga-dma-multi-tool]] (Artix-7 detect/flash via openFPGALoader + DMA R/W speedtest) sit in the FPGA bring-up layer before host DMA apps. (source: wiki/sources/descriptions/sercanarga__fpga-dma-multi-tool.md) CE-facing DMA loaders such as [[dma-cheat-engine-loader]] (copy CE into `DMACE`; closed-source) bridge classic Cheat Engine installs onto that external DMA path. (source: wiki/sources/descriptions/un4ckn0wl3z__DMACheatEngineLoader.md) Game-facing samples such as [[csgo-dma-overlay]] pair DMA reads with an overlay for CS:GO research. (source: wiki/sources/descriptions/slack69__csgo-dma-overlay.md)

## Related

[[iommu]] · [[hvci]] · [[pcileech]] · [[pcileech-fpga]] · [[pcileech-dma-fullstealth]] · [[fpga-dma-multi-tool]] · [[physpatch]] · [[x670e-tomahawk-anticheat-update]] · [[dma-invoker]] · [[dma-speedtest-memflow-rs]] · [[dma-cheat-engine-loader]] · [[csgo-dma-overlay]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]

