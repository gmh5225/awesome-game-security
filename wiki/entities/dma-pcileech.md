---
title: DMA-Pcileech (JOKOSAHS)
kind: entity
topics: [dma-attack, anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/JOKOSAHS__DMA-Pcileech.md
updated: 2026-08-24
confidence: medium
---

# DMA-Pcileech (JOKOSAHS)

Open-source **[[pcileech]]-based FPGA firmware** for **PCIe DMA device emulation**, originally oriented toward **network-card-style** hardware (AX200-class presentation in the curated README). Implemented mainly in **SystemVerilog/Verilog** with **Xilinx Vivado** TCL scripts and board constraint files for **Screamer M2**, **Enigma X1**, **Squirrel**, and related **Artix-7** boards. (source: wiki/sources/descriptions/JOKOSAHS__DMA-Pcileech.md)

## Design scope

Covers PCIe **TLP handling**, **configuration-space shadowing**, **BAR control**, **FT601 USB** host communication, and **FIFO/mux** datapaths typical of [[pcileech-fpga]] DMA setups. **TLP interrupt behavior** is noted as tuned for certain motherboards—relevant to MSI/MSI-X and completion-latency probes in the firmware tier ladder on [[overviews/dma-attack]].

## Anti-cheat context

Released as an **educational** reference after **Anti-Cheat Expert (ACE)** began detecting related **network-card firmware** in the wild. Primary audience is researchers studying DMA/PCILeech firmware techniques in game-security and anti-cheat contexts—not a turnkey evasion product. Compare other network-class emulation forks such as [[pcileech-wifi]] and [[pcileech-wifi-v2]].

## Links

- Repo: https://github.com/JOKOSAHS/DMA-Pcileech

## Related

[[pcileech]] · [[pcileech-fpga]] · [[pcileech-wifi]] · [[pcileech-wifi-v2]] · [[pcileechgen]] · [[dma-cfw-guide]] · [[dma-fw-guide-2.0]] · [[concepts/dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
