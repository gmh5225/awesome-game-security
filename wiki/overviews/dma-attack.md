---
title: DMA Attack
kind: overview
topics: [dma-attack]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md
  - wiki/sources/descriptions/un4ckn0wl3z__DMAInvoker.md
  - wiki/sources/descriptions/un4ckn0wl3z__DMACheatEngineLoader.md
  - wiki/sources/descriptions/ufrisk__pcileech.md
  - wiki/sources/descriptions/ufrisk__pcileech-fpga.md
  - wiki/sources/descriptions/tandasat__HelloIommuPkg.md
  - wiki/sources/descriptions/sonodima__physpatch.md
  - wiki/sources/descriptions/lauralex__fn-dma-cheat.md
  - wiki/sources/descriptions/slack69__csgo-dma-overlay.md
  - wiki/sources/descriptions/sh1ftd__dma-speedtest-memflow-rs.md
  - wiki/sources/descriptions/realquantumstealth-hub__PCILeech-DMA-Fullstealth.md
  - wiki/sources/descriptions/mltpig__PCILeech-FPGA-DMA_VMD.md
  - wiki/sources/descriptions/sercanarga__fpga-dma-multi-tool.md
  - wiki/sources/descriptions/sh1ftd__dma-tools-rs.md
  - wiki/sources/descriptions/kaijia2022__Cheat-Engine-DMA-Plugin.md
  - wiki/sources/descriptions/kWAYTV__dma-cheat-base.md
  - wiki/sources/descriptions/sercanarga__PCILeechGen.md
updated: 2026-08-03
confidence: high
---

# DMA Attack

PCIe Direct Memory Access threat modeling for game security: FPGA endpoints (often M.2), host tools like [[pcileech]]/MemProcFS, and defenses that software anti-cheat alone cannot fully cover once a hostile bus-master can read RAM. (source: wiki/sources/skills/dma-attack.md)

## Threat model

Typical external DMA cheat: **cheat PC** (signatures, ESP, aim logic) + **DMA card** (FPGA in an M.2 or add-in slot issuing Memory Read TLPs) + optional **HID actuator** (USB keyboard/mouse emulator). No attacker code need run on the gaming OS—the machine sees a PCIe device performing ordinary-looking DMA mediated by chipset and (when configured) the [[iommu]]. (source: wiki/sources/skills/dma-attack.md)

Host stack in the curated list: [[pcileech]] → LeechCore → [[pcileech-fpga]] firmware; donor-cloning generators ([[pcileechgen]] — Go/VFIO donor capture → SystemVerilog/COE → Vivado bitstreams), wrappers ([[dma-invoker]], [[dma-cheat-engine-loader]], [[cheat-engine-dma-plugin]] — CE plugin swapping process memory for LeechCore DMA R/W), benchmarks ([[dma-speedtest-memflow-rs]]), board utilities ([[fpga-dma-multi-tool]], [[dma-tools-rs]] — OpenOCD JTAG flash/DNA + PCILeech sanity check on Artix-7), stealth forks ([[pcileech-dma-fullstealth]]), class-emulation firmware such as [[pcileech-fpga-dma-vmd]] (Intel RST VMD `9A0B`; MSI-X/NVMe/BAR shadow on Artix-7 75T), kernel physical patches ([[physpatch]]), title samples ([[csgo-dma-overlay]], [[fn-dma-cheat]]), and cheat-base scaffolds ([[dma-cheat-base]] — rendering, animation, SDK generation). (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md) (source: wiki/sources/descriptions/mltpig__PCILeech-FPGA-DMA_VMD.md) (source: wiki/sources/descriptions/sh1ftd__dma-tools-rs.md) (source: wiki/sources/descriptions/lauralex__fn-dma-cheat.md) (source: wiki/sources/descriptions/kaijia2022__Cheat-Engine-DMA-Plugin.md) (source: wiki/sources/descriptions/kWAYTV__dma-cheat-base.md)

## Three defense layers

| Layer | Mechanism | Catches |
|-------|-----------|---------|
| PCIe fingerprinting | Config Space, BAR probes, TLP/link behavior vs donor silicon | Identity mismatch, inert BARs, stock Xilinx IDs |
| [[iommu]] enforcement | IOVA translation, ACS, interrupt remapping | Out-of-domain DMA (when active and strict) |
| External attestation | TPM Quote, measured boot, Secure Launch PCRs | Boot-chain / IOMMU-policy subversion |

Hypervisor containment ([[hvci]], EPT traps, honeypot pages) and firmware policy (pre-boot DMA protection, BIOS DXE hardening in [[x670e-tomahawk-anticheat-update]]) stack on top. (source: wiki/sources/skills/dma-attack.md)

## PCIe stack (detection-relevant)

- **TLPs:** Memory Read/Write, Config R/W, Completions; Requester ID (BDF) drives IOMMU lookup; completion splitting (MRRS/RCB/MPS) and tag turnover are donor-class fingerprints.
- **Config Space:** 256-byte legacy header + extended capabilities (AER, DSN, ATS, ACS, SR-IOV); capability-chain walk, BAR mask probe, R/W consistency on Command/Device Control and W1C bits.
- **Behavioral:** LTSSM/link width, ASPM transitions, AER correctable-error baselines, MSI/MSI-X interrupt distribution, completion-latency distribution (KS / Anderson–Darling vs donor reference).

Stock [[pcileech-fpga]] builds expose trivial Tier-0/1 signals (placeholder `10EE:0666`, zerowrite4k BAR, missing AER). Sophisticated firmware climbs tiers 2–6 (shadow config → overlay RAM → BAR MMIO + MSI → behavioral emulation → private randomized layouts). (source: wiki/sources/skills/dma-attack.md)

## IOMMU and bypass surface

Legitimate drivers map only explicit IOVAs; game memory should stay outside device domains. Active cheat paths include IOMMU disabled, pre-boot DMA, identity/passthrough domains, driver page over-allocation (Thunderclap class), **legitimate-path exfil** (spoofed NIC reading its own RX ring), and kernel reprogramming of IOMMU tables via [[byovd]]. ACS Source Validation + P2P redirect and ATS-untrusted policy for untrusted endpoints are mandatory in threat models. See [[iommu]] for the condensed bypass catalog.

## Layered detection pipeline

Apply [[research-rigor]] when turning signals into enforcement. (source: wiki/sources/skills/dma-attack.md)

1. **Pre-game:** IOMMU + IR active, Secure Boot, VBS/[[hvci]], TPM provisioned, attestation Quote, ACS topology walk, full 4 KB config dump per device, SMBIOS slot cross-check.
2. **PCIe integrity:** VID/DID allowlists, signature residue, BAR/class probes, R/W and W1C probes, link/AER baselines, latency statistics.
3. **Runtime:** per-device IOMMU fault rate, interrupt accounting, cheat-phase access patterns (discovery → narrow periodic reads), honeypot regions with fault/EPT logging.
4. **Containment before verdict:** sandbox domain remapping, Bus Master Enable clear, DPC; correlate multi-signal evidence server-side.

Tier-6 firmware operating only within driver-mapped domains and matching donor behavior on tested dimensions can evade isolated PCIe/IOMMU signatures—external trust anchors (TPM PCR[7] DMA Protection Disabled, DRTM, remote attestation) address what bus-layer checks cannot prove alone.

## Key sub-areas

- **PCIe stack:** TLPs, Config Space, BAR probing, MSI/MSI-X, AER, link/ASPM behavior
- **Firmware tiers:** stock pcileech fingerprints → donor shadow config → BAR/MSI behavioral emulation
- **[[iommu]]:** VT-d / AMD-Vi domains, ACS, ATS trust, fault-rate monitoring, containment
- **Hypervisor / attestation:** EPT protections, VBS/[[hvci]], TPM Quote + measured-boot PCRs
- **Thunderbolt/USB4:** hot-plug PCIe tunneling vs Kernel DMA Protection

## Related concepts

[[dma]] · [[iommu]] · [[helloiommupkg]] · [[hvci]] · [[byovd]] · [[research-rigor]] · [[pcileech]] · [[pcileech-fpga]] · [[pcileechgen]] · [[pcileech-dma-fullstealth]] · [[pcileech-fpga-dma-vmd]] · [[fpga-dma-multi-tool]] · [[dma-tools-rs]] · [[physpatch]] · [[x670e-tomahawk-anticheat-update]] · [[dma-invoker]] · [[dma-speedtest-memflow-rs]] · [[dma-cheat-engine-loader]] · [[cheat-engine-dma-plugin]] · [[csgo-dma-overlay]] · [[fn-dma-cheat]] · [[dma-cheat-base]] · [[overviews/anti-cheat]]

## README map

No top-level DMA section — maps via `Cheat` (~2646) DMA lanes and `Anti Cheat > Detection:DMA` (~640), plus hypervisor/virtualization/HWID detection and `Windows Security Features` (~9; CET/shadow stack + TPM PCR attestation of virt/IOMMU/Secure Boot/VBS/HVCI/DSE/blocklist — e.g. SEWindows local replay and remote attestation). (source: wiki/sources/README-categories.md)
