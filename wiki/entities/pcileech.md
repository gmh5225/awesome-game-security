---
title: PCILeech
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/descriptions/ufrisk__pcileech.md
updated: 2026-07-29
confidence: high
---

# PCILeech

Host-side tool that uses **PCIe hardware devices** to **read and write target system memory** via **DMA over PCIe**. Canonical stack entry for game-security and RE work in the cheat / DMA lane. (source: wiki/sources/descriptions/ufrisk__pcileech.md)

## Project lineage

Five upstream repos form a pipeline: **FPGA firmware** ([[pcileech-fpga]]) → **LeechCore** (device abstraction) → **PCILeech** (attack modules) / **MemProcFS** (target memory as `/proc`-like tree) → **vmm** (analysis API). Typical workflow: broad MemProcFS discovery (modules, VAD, YARA) then narrow periodic reads via vmm.dll/LeechCore in a custom cheat app. (source: wiki/sources/skills/dma-attack.md)

## Links

- Repo: https://github.com/ufrisk/pcileech
- Related: https://github.com/ufrisk/MemProcFS · https://github.com/ufrisk/LeechCore · https://github.com/ufrisk/pcileech-fpga

## Stock firmware fingerprints

Unmodified [[pcileech-fpga]] builds commonly expose Tier-0/1 detection signals: Xilinx placeholder VID/DID `10EE:0666`, zerowrite4k or loopaddr BAR behavior, absent AER/DSN, deterministic config-read latency, no ASPM transitions, and MSI present without driver-consistent interrupts. Donor shadow config and overlay RAM raise the bar to tiers 2–3; see [[overviews/dma-attack]] for the full sophistication ladder. (source: wiki/sources/skills/dma-attack.md)

## Related

[[dma]] · [[iommu]] · [[pcileech-fpga]] · [[pcileech-dma-fullstealth]] · [[pcileech-fpga-dma-vmd]] · [[pcileech-dma-nvme-vmd]] · [[dma-invoker]] · [[dma-cheat-engine-loader]] · [[dma-speedtest-memflow-rs]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
