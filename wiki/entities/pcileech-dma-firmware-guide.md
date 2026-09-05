---
title: Pcileech DMA Firmware Guide
kind: entity
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/16SalomonArs__Pcileech-DMA-Firmware-Guide.md
updated: 2026-09-05
confidence: medium
---

# Pcileech DMA Firmware Guide

Hands-on **Guide** for building custom **[[pcileech-fpga]]** DMA firmware that **emulates a real PCIe donor device**—not only swapping VID/DID. Walks through **Windows-first donor capture**, **PCIe core and BAR setup**, **shadow configuration space**, **write-mask protection**, **capability structures**, and **TLP response** work using **Vivado**, **SystemVerilog**, **Python COE generation**, and tools such as **Arbor** and **TeleScan PE**. Covers common **Artix-7** DMA boards (**Squirrel**, **CaptainDMA**, **LeetDMA**, **Enigma**, **ZDMA**, and related platforms), board-specific flashing, **cold-boot validation**, and recovery when firmware fails to enumerate. Advanced topics include **Zero4K BAR** handling, **Vivado ILA** debugging, and optional **Linux capture** paths. Primary audience: researchers and hardware learners doing controlled-lab DMA and PCIe firmware work relevant to game security and reverse-engineering tooling. (source: wiki/sources/descriptions/16SalomonArs__Pcileech-DMA-Firmware-Guide.md)

## Workflow highlights

| Stage | Focus |
|-------|--------|
| Donor capture | Windows-first PCIe config space, BAR masks, capability chain (Arbor / TeleScan PE) |
| HDL / core | [[pcileech-fpga]] SystemVerilog; PCIe core, BAR layout, shadow config |
| Protection | Write-mask paths; capability-structure fidelity beyond ID spoofing |
| TLP / response | Realistic completion and config-read behavior |
| Build / flash | Vivado bitstreams for Squirrel, CaptainDMA, LeetDMA, Enigma, ZDMA |
| Validation | Cold-boot enumerate checks; recovery when firmware fails to appear |
| Advanced | Zero4K BAR, Vivado ILA debug; optional Linux donor capture |

Complements [[dma-cfw-guide]] (**pcileech-fpga v4.15** hand-edit path), [[dma-fw-guide-2.0]] (multi-language comprehensive walkthrough), and automated donor pipelines like [[pcileechgen]]. Emphasis on **full donor emulation** (BAR, capabilities, TLP) aligns with firmware tiers 2–4 in [[overviews/dma-attack]]—config-space integrity, writemask probes, BAR MMIO, and bus behavior—not stock Tier-0/1 placeholder IDs alone.

## Links

- Repo: https://github.com/16SalomonArs/Pcileech-DMA-Firmware-Guide

## Related

[[pcileech-fpga]] · [[pcileech]] · [[pcileechgen]] · [[dma-cfw-guide]] · [[dma-fw-guide-2.0]] · [[dma-attack-firmware-customization]] · [[entities/dma]] · [[xilinx-fpga-pcie-xdma-tutorial]] · [[learn-fpga-programming]] · [[concepts/dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
