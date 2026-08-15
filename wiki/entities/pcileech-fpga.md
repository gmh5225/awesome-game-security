---
title: PCILeech-FPGA
kind: entity
topics: [dma-attack, reverse-engineering, game-hacking]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/descriptions/ufrisk__pcileech-fpga.md
  - wiki/sources/descriptions/sercanarga__PCILeechGen.md
updated: 2026-08-05
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

Artix-7 (T35–T200) dominates consumer boards; BRAM/LUT budgets constrain how many behavioral subsystems fit without Zynq-class resources. Donor-cloning generators such as [[pcileechgen]] automate VFIO capture → SystemVerilog/COE → Vivado bitstreams (scan/check/build/validate; dynamic BAR, NVMe admin-queue, MMIO trace import) for many PCILeech-compatible boards. (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md)

## Links

- Repo: https://github.com/ufrisk/pcileech-fpga

## Related

[[pcileech]] · [[pcileechgen]] · [[pcileech-wifi]] · [[pcileech-dma-fullstealth]] · [[pcileech-fpga-dma-vmd]] · [[fpga-dma-multi-tool]] · [[dma]] · [[iommu]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
