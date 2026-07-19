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
updated: 2026-07-19
confidence: high
---


# DMA (Direct Memory Access)

Hardware-level memory access where a PCIe device issues Memory Read/Write TLPs against host RAM via Bus Master, without executing attacker code in the gaming OS. In game security this usually means an FPGA card (often M.2) linked to a separate cheat PC. (source: wiki/sources/skills/dma-attack.md) Host tooling such as [[pcileech]] drives those PCIe devices for target-memory R/W over DMA. (source: wiki/sources/descriptions/ufrisk__pcileech.md)

## Why it matters

Software anti-cheat sees a “normal” PCIe endpoint. Classic process/handle/injection signals may be absent. Defense shifts to PCIe fingerprinting, [[iommu]] policy, hypervisor containment, TPM/measured-boot attestation, and occasionally firmware-level blocks (e.g. BIOS DXE option-ROM attribute stripping in [[x670e-tomahawk-anticheat-update]]). (source: wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md)


## Typical stack

Cheat app → LeechCore/pcileech/MemProcFS → FPGA firmware → Memory Read TLPs → walk CR3/page tables → game state; optional HID actuator for input. Host-side DMA RPM wrappers such as [[dma-invoker]] (DMALibrary-backed) sit in the cheat-app layer for Windows process-memory reads. (source: wiki/sources/descriptions/un4ckn0wl3z__DMAInvoker.md) CE-facing DMA loaders such as [[dma-cheat-engine-loader]] (copy CE into `DMACE`; closed-source) bridge classic Cheat Engine installs onto that external DMA path. (source: wiki/sources/descriptions/un4ckn0wl3z__DMACheatEngineLoader.md)

## Related

[[iommu]] · [[hvci]] · [[pcileech]] · [[x670e-tomahawk-anticheat-update]] · [[dma-invoker]] · [[dma-cheat-engine-loader]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]

