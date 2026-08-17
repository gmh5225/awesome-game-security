---
title: PCIeM
kind: entity
topics: [dma-attack, reverse-engineering]
sources:
  - wiki/sources/descriptions/cakehonolulu__pciem.md
updated: 2026-08-17
confidence: medium
---

# PCIeM

**Linux kernel framework** for **synthetic userspace PCIe device emulation** without physical hardware. A kernel module registers virtual PCIe endpoints that appear as legitimate PCI devices to the host OS, enabling driver development and security research entirely in software. (source: wiki/sources/descriptions/cakehonolulu__pciem.md)

## Role in the DMA stack

**Software-only PCIe lab lane** — not an FPGA DMA attack tool like [[pcileech]]. Useful for PCIe security researchers and DMA tool developers studying **device emulation**, **config-space population**, and **driver interaction** before moving to silicon or VM-based setups. Operates **directly on the host** (no VM or QEMU), contrasting with libvfio-user-style paths. (source: wiki/sources/descriptions/cakehonolulu__pciem.md)

Complements hardware endpoint research ([[litepcie]], [[pcileech-fpga]]) and donor-cloning flows ([[pcileechgen]]) when validating how the OS PCI subsystem enumerates and binds synthetic devices.

## Links

- Repo: https://github.com/cakehonolulu/pciem

## Related

[[dma]] · [[pcileech]] · [[pcileech-fpga]] · [[pcileechgen]] · [[litepcie]] · [[pcie-detector]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
