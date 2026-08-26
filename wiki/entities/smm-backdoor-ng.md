---
title: SmmBackdoorNg
kind: entity
topics: [windows-kernel, reverse-engineering, dma-attack]
sources:
  - wiki/sources/descriptions/Cr4sh__SmmBackdoorNg.md
updated: 2026-08-26
confidence: medium
---

# SmmBackdoorNg

**SmmBackdoorNg** (Cr4sh) is a **UEFI System Management Mode backdoor framework** with separate **firmware** and **client-side** components for low-level platform research. It combines **C-based DXE and SMM code** with **Python tooling** for **Windows and Linux** interaction, deployment, and demonstrations. Deployment paths include **flash-image infection** and **pre-boot DMA-assisted loading**; the repository includes examples around **privilege escalation** and **hypervisor interaction**. It targets **firmware security research**, **persistence studies**, and analysis of **pre-OS attack surfaces**. (source: wiki/sources/descriptions/Cr4sh__SmmBackdoorNg.md)

From the same author as compact pre-boot DMA stacks [[pico-dma]] and [[s6-pcie-microblaze]], but focused on **Ring -2 SMM persistence** rather than runtime PCIe TLP exfiltration.

## Links

- Repo: https://github.com/Cr4sh/SmmBackdoorNg

## Related

[[smm-infect]] · [[smm]] · [[pico-dma]] · [[s6-pcie-microblaze]] · [[bootlicker]] · [[efiguard]] · [[overviews/windows-kernel]] · [[overviews/dma-attack]]
