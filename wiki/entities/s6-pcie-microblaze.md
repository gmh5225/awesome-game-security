---
title: s6_pcie_microblaze
kind: entity
topics: [dma-attack, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Cr4sh__s6_pcie_microblaze.md
updated: 2026-08-26
confidence: medium
---

# s6_pcie_microblaze

**s6_pcie_microblaze** (Cr4sh) is a **PCI Express DIY hacking toolkit** that implements a **software-controllable PCIe Gen 1.1 endpoint** on a **Xilinx SP605 Spartan-6 FPGA**. Verilog HDL and **MicroBlaze** firmware expose **raw Transaction Layer Packets (TLPs) over Ethernet**, with **Python** host tools for memory read/write, physical memory scanning, and **IOMMU audits**. Proof-of-concept payloads cover **pre-boot DMA** UEFI DXE driver injection, a **Hyper-V VM-exit backdoor** for hypervisor inspection and guest-to-host escape research, and a **Boot Backdoor** with runtime DMA shell commands and file transfer. Primary languages include Verilog, C (MicroBlaze and UEFI payloads), Python, and C++ backdoor clients. (source: wiki/sources/descriptions/Cr4sh__s6_pcie_microblaze.md)

## Role in the DMA stack

Educational **custom FPGA endpoint** lane on legacy **Spartan-6 SP605** hardware—contrasts with Artix-7 [[pcileech-fpga]] M.2 stacks and Cr4sh's compact **pico_dma** pre-boot MicroBlaze flows on smaller boards. Useful for researchers studying **Option ROM / pre-boot compromise**, **protected Windows platform** reverse engineering, and **below-OS DMA** threat models before modern IOMMU policy.

## Links

- Repo: https://github.com/Cr4sh/s6_pcie_microblaze

## Related

[[pcileech]] · [[pcileech-fpga]] · [[litepcie]] · [[xilinx-fpga-pcie-xdma-tutorial]] · [[diskjacker]] · [[ddma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/windows-kernel]]
