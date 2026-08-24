---
title: Pcileech Intel I226-V FullEmu (Herooyyy)
kind: entity
topics: [dma-attack, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Herooyyy__Pcileech-Intel-I226-V-FullEmu.md
updated: 2026-08-24
confidence: medium
---

# Pcileech Intel I226-V FullEmu (Herooyyy)

**Prebuilt [[pcileech]]-class DMA firmware release** that emulates **Intel I225/I226 wired Ethernet adapter** behavior on PCIe. Ships mainly as a **binary payload** with a minimal README rather than full HDL sources. Focuses on **synthetic TCP traffic generation** and maintaining a **persistent active-link state** so the endpoint presents as a live, traffic-bearing NIC—not an inert DMA card. (source: wiki/sources/descriptions/Herooyyy__Pcileech-Intel-I226-V-FullEmu.md)

## Anti-cheat context

Targets **activity-based detection** used by systems such as **[[vanguard]]**, **Faceit**, and **[[easy-anti-cheat]]** that correlate PCIe network-controller identity with **link activity**, **driver-loaded baselines**, and **ongoing traffic patterns**. Contrasts with open-source network-class forks such as [[dma-pcileech]], [[pcileech-wifi]], and [[pcileech-wifi-v2]] that emphasize config-space/BAR/TLP fidelity from source. See the tier ladder and behavioral probes in [[overviews/dma-attack]].

## Links

- Repo: https://github.com/Herooyyy/Pcileech-Intel-I226-V-FullEmu

## Related

[[pcileech]] · [[pcileech-fpga]] · [[pcileech-isabridge]] · [[dma-pcileech]] · [[pcileech-wifi]] · [[pcileech-wifi-v2]] · [[vgk-dma-bypass]] · [[concepts/dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
