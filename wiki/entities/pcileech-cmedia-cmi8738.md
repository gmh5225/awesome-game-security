---
title: PCILeech C-Media CMI8738
kind: entity
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/12i192i1043__pcileech-cmedia-cmi8738.md
updated: 2026-09-05
confidence: medium
---

# PCILeech C-Media CMI8738

**[[pcileech-fpga]]** firmware that emulates a **C-Media CMI8738/PCI-SX** legacy sound card so **Artix-7** DMA boards enumerate as a familiar PCI audio endpoint. Implemented in **SystemVerilog/Verilog** for **Xilinx Vivado**, it presents **authentic config space** and a **full BAR0 register map** captured from real hardware. A **null audio endpoint** advances position counters and fires interrupts without issuing audio memory-read TLPs; an optional **fake DMA generator** can emit periodic MRd traffic that mirrors real audio bus activity while keeping the **PCILeech DMA path isolated**. Targets hardware emulation research, OS driver analysis, PCIe protocol study, and related **DMA/anti-cheat** threat modeling on boards such as **Captain DMA**, **Enigma x1**, **Squirrel**, **Screamer M.2**, and **TBX4**. (source: wiki/sources/descriptions/12i192i1043__pcileech-cmedia-cmi8738.md)

## Emulation model

| Component | Behavior |
|-----------|----------|
| Config space | Donor-accurate CMI8738/PCI-SX identity and capability chain |
| BAR0 | Full register map from captured hardware |
| Audio path | Null endpoint—position counters + interrupts without audio MRd TLPs |
| Bus activity | Optional periodic MRd generator mimics real audio DMA patterns |
| PCILeech DMA | Isolated from the emulated audio traffic generator |

Fits the **class-emulation** firmware tier on [[overviews/dma-attack]]—BAR MMIO fidelity, interrupt timing, and optional bus-activity mimicry beyond VID/DID swap—alongside NIC, bridge, and storage-controller personas such as [[dma-pcileech]], [[pcileech-isabridge]], and [[pcileech-intel-i226-v-fullemu]]. Manual donor-emulation workflows are documented in [[pcileech-dma-firmware-guide]] and [[dma-cfw-guide]].

## Links

- Repo: https://github.com/12i192i1043/pcileech-cmedia-cmi8738

## Related

[[pcileech]] · [[pcileech-fpga]] · [[pcileech-dma-firmware-guide]] · [[pcileech-isabridge]] · [[dma-pcileech]] · [[pcileechgen]] · [[concepts/dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
