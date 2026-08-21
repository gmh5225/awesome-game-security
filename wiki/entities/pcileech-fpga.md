---
title: PCILeech-FPGA
kind: entity
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/descriptions/ufrisk__pcileech-fpga.md
  - wiki/sources/descriptions/sercanarga__PCILeechGen.md
  - wiki/sources/descriptions/acageduser__DMA-Attack-Firmware-Customization.md
  - wiki/sources/descriptions/Silverr12__DMA-CFW-Guide.md
updated: 2026-08-21
confidence: high
---

# PCILeech-FPGA

FPGA **HDL/firmware** and **Vivado** build flows for [[pcileech]] DMA devices that access target system memory over PCIe. Primarily **SystemVerilog/Verilog** with Xilinx IP for CaptainDMA, ScreamerM2, EnigmaX1, and related boards. (source: wiki/sources/descriptions/ufrisk__pcileech-fpga.md)

## Architecture

Key modules: TLP source/sink (`pcileech_pcie_tlps128_bram_rdwr`), **shadow config space** in BRAM (`pcileech_pcie_cfgspace_shadow`, `.coe` init), BAR implementations (`zerowrite4k`, `loopaddr`, `none`), and config management via `cfg_mgmt_*`. Shadow config is spoofable but ships with placeholder Xilinx IDs until replaced with a donor dump. (source: wiki/sources/skills/dma-attack.md)

## Firmware sophistication tiers

| Tier | Description | Detection |
|------|-------------|-------------|
| 0 | Stock upstream | Trivial — VID/DID blacklist |
| 1 | Bridge (.coe VID/DID only) | Easy — IP residue, driverless BME |
| 2 | Full 4 KB shadow, no overlay | Medium — silent write-drop probes |
| 3 | Shadow + per-register overlay RAM | Medium-hard — W1C/reserved-bit probes |
| 4 | BAR MMIO + MSI generator | Hard — class-functional A/B tests |
| 5 | Behavioral (ASPM, AER, latency jitter) | Very hard — statistical baselines |
| 6 | Private randomized layouts | Requires attestation beyond bus signatures |

Artix-7 (T35–T200) dominates consumer boards; BRAM/LUT budgets constrain how many behavioral subsystems fit without Zynq-class resources. Donor-cloning generators such as [[pcileechgen]] automate VFIO capture → SystemVerilog/COE → Vivado bitstreams (scan/check/build/validate; dynamic BAR, NVMe admin-queue, MMIO trace import) for many PCILeech-compatible boards. (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md) Manual customization guides such as [[dma-attack-firmware-customization]] document hand-patching Screamer Squirrel 35T firmware to emulate a Realtek RTL8111 NIC (MindShare Arbor donor harvest → Vivado bitstream; BattlEye/EAC evasion testing). (source: wiki/sources/descriptions/acageduser__DMA-Attack-Firmware-Customization.md) [[dma-cfw-guide]] (Silverr12) generalizes the hand-edit workflow for **pcileech-fpga v4.15** across Squirrel, EnigmaX1, and ZDMA—Arbor/Telescan PE donor harvest, Vivado IP patch, TLP emulation, and `.coe`/writemask shadow-config paths. (source: wiki/sources/descriptions/Silverr12__DMA-CFW-Guide.md)

## Links

- Repo: https://github.com/ufrisk/pcileech-fpga

## Related

[[pcileech]] · [[pcileechgen]] · [[dma-attack-firmware-customization]] · [[dma-cfw-guide]] · [[pcileech-wifi]] · [[pcileech-wifi-v2]] · [[pcileech-dma-fullstealth]] · [[pcileech-fpga-dma-vmd]] · [[fpga-dma-multi-tool]] · [[dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
