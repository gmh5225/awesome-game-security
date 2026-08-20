---
title: DMA PE Dumper
kind: entity
topics: [dma-attack, reverse-engineering, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/Trustings__DMA_PE_Dumper.md
updated: 2026-08-20
confidence: medium
---

# DMA PE Dumper

C++ **DMA-based PE dumper** for extracting process executable or DLL images through a PCIe FPGA setup. Integrates **LeechCore** and **VMMDLL**-style components for low-level physical memory access without running attacker code on the gaming OS. Handles difficult scenarios such as **CR3 shuffling** and **DTB patching** while locating and reconstructing target PE images. Primary use cases: advanced memory forensics and game anti-cheat research workflows. (source: wiki/sources/descriptions/Trustings__DMA_PE_Dumper.md)

## Capabilities

- DMA physical-memory PE extraction (EXE/DLL) via FPGA
- LeechCore / VMMDLL integration for page-table walks
- CR3 shuffle / DTB patching for unstable page-table contexts

## Links

- Repo: https://github.com/Trustings/DMA_PE_Dumper

## Related

[[dma]] · [[pcileech]] · [[volk-dma]] · [[dumpepe]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
