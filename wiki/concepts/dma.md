---
title: DMA (Direct Memory Access)
kind: concept
topics: [dma-attack, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/skills/anti-cheat.md
updated: 2026-07-16
confidence: high
---

# DMA (Direct Memory Access)

Hardware-level memory access where a PCIe device issues Memory Read/Write TLPs against host RAM via Bus Master, without executing attacker code in the gaming OS. In game security this usually means an FPGA card (often M.2) linked to a separate cheat PC. (source: wiki/sources/skills/dma-attack.md)

## Why it matters

Software anti-cheat sees a “normal” PCIe endpoint. Classic process/handle/injection signals may be absent. Defense shifts to PCIe fingerprinting, [[iommu]] policy, hypervisor containment, and TPM/measured-boot attestation.

## Typical stack

Cheat app → LeechCore/pcileech/MemProcFS → FPGA firmware → Memory Read TLPs → walk CR3/page tables → game state; optional HID actuator for input.

## Related

[[iommu]] · [[hvci]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
