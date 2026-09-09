---
title: PCILeech
kind: entity
topics: [dma-attack, game-hacking, reverse-engineering]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/descriptions/ufrisk__pcileech.md
  - wiki/sources/descriptions/Neverdecel__pcileech-memprocfs-mcp.md
  - wiki/sources/descriptions/MGreif__PCILeech_DMA_Proxy.md
  - wiki/sources/descriptions/Herooyyy__Pcileech-Intel-I226-V-FullEmu.md
  - wiki/sources/descriptions/Herooyyy__Pcileech-ISABridge.md
  - wiki/sources/descriptions/Herooyyy__Pcileech-Activator-Anti-crack.md
  - wiki/sources/descriptions/Herooyyy__Pcileech-AMDPCI.md
  - wiki/sources/descriptions/Herooyyy__Free-DMA-Firmware-pcileech.md
  - wiki/sources/descriptions/12i192i1043__pcileech-cmedia-cmi8738.md
updated: 2026-09-09
confidence: high
---

# PCILeech

Host-side tool that uses **PCIe hardware devices** to **read and write target system memory** via **DMA over PCIe**. The **memory initiator** is the FPGA/card bus master on the target; PCILeech/LeechCore/MemProcFS on the cheat PC are transport and analysis layers—distinct from host-mediated WinPmem or `/dev/mem` paths. See [[memory-acquisition-path]]. (source: wiki/sources/skills/dma-attack.md) (source: wiki/sources/descriptions/ufrisk__pcileech.md)

## Project lineage

Five upstream repos form a pipeline: **FPGA firmware** ([[pcileech-fpga]]) → **LeechCore** (device abstraction) → **PCILeech** (attack modules) / **MemProcFS** (target memory as `/proc`-like tree) → **vmm** (analysis API). Typical workflow: broad MemProcFS discovery (modules, VAD, YARA) then narrow periodic reads via vmm.dll/LeechCore in a custom cheat app. (source: wiki/sources/skills/dma-attack.md)

## Links

- Repo: https://github.com/ufrisk/pcileech
- Related: https://github.com/ufrisk/MemProcFS · https://github.com/ufrisk/LeechCore · https://github.com/ufrisk/pcileech-fpga

## FPGA firmware architecture

Key [[pcileech-fpga]] modules: shadow config in BRAM (`pcileech_pcie_cfgspace_shadow.v`), TLP source/sink, BAR implementations (`zerowrite4k`, `loopaddr`, `none`), and cfg_mgmt integration. Stock builds ship placeholder Xilinx IDs in `.coe`—users must replace with donor dumps. Shadow config is spoofable but **not spoofed by default**; active BAR probing can catch stock `zerowrite4k` in one operation. Bridge-style spoofing patches GUI identity fields but retains hard-IP fingerprints; emulated firmware serves full 4 KB extended config from BRAM with common bugs (IP-block mux priority, Type 1 config not intercepted, naive W1C/overlay masks). (source: wiki/sources/skills/dma-attack.md)

## Stock firmware fingerprints

Unmodified [[pcileech-fpga]] builds commonly expose: Xilinx placeholder VID/DID `10EE:0666`, zerowrite4k or loopaddr BAR behavior, absent AER/DSN, deterministic config-read latency, no ASPM transitions, and MSI present without driver-consistent interrupts. Compare against **device evidence dimensions** (identity, config/function, runtime behavior, memory-access policy, platform trust) on [[overviews/dma-attack]]—not a single tier label. (source: wiki/sources/skills/dma-attack.md)

## Related

[[dma]] · [[memory-acquisition-path]] · [[iommu]] · [[pcileech-fpga]] · [[pcileech-activator-anti-crack]] · [[pcileech-amdpci]] · [[free-dma-firmware-pcileech]] · [[pcileech-intel-i226-v-fullemu]] · [[pcileech-isabridge]] · [[pcileech-cmedia-cmi8738]] · [[pcileech-dma-proxy]] · [[pcileech-dma-fullstealth]] · [[pcileech-fpga-dma-vmd]] · [[pcileech-dma-nvme-vmd]] · [[pcileech-memprocfs-mcp]] · [[dma-invoker]] · [[dma-cheat-engine-loader]] · [[dma-speedtest-memflow-rs]] · [[overviews/dma-attack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
