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
  - wiki/sources/descriptions/gmh5225__cheat-engine-ceserver-pcileech.md
  - wiki/sources/descriptions/kWAYTV__dma-cheat-base.md
  - wiki/sources/descriptions/sercanarga__PCILeechGen.md
  - wiki/sources/descriptions/sercanarga__pcileechgen.md
  - wiki/sources/descriptions/iqrw0__DieDMAProtection.md
  - wiki/sources/descriptions/paul01784__MeatyEFTRelease.md
  - wiki/sources/descriptions/gmh5225__eft-dma-radar-1.md
  - wiki/sources/descriptions/gmh5225__Nathans-Tarkov-Radar-Public.md
  - wiki/sources/descriptions/gmh5225__unispectDMAPlugin.md
  - wiki/sources/descriptions/gmh5225__ReClass-DMA.md
  - wiki/sources/descriptions/lyk64__VolkDMA.md
  - wiki/sources/descriptions/gmh5225__Pcileech-DMA-NVMe-VMD.md
  - wiki/sources/descriptions/gmh5225__PCIE-Detector.md
  - wiki/sources/descriptions/gmh5225__MemTools.md
  - wiki/sources/descriptions/gmh5225__DMA-PCIE-BOARD-75T.md
  - wiki/sources/descriptions/gmh5225__DDMA-1.md
  - wiki/sources/descriptions/gmh5225__CS2-Dma-Radar.md
  - wiki/sources/descriptions/fsquirt__SEWindows.md
  - wiki/sources/descriptions/fmc999__GTA5-DMA-CHEAT.md
  - wiki/sources/descriptions/enjoy-digital__litepcie.md
  - wiki/sources/descriptions/ekknod__vm.md
  - wiki/sources/descriptions/ekknod__pcileech-wifi.md
  - wiki/sources/descriptions/ekknod__drvscan.md
updated: 2026-08-15
confidence: high
---

# DMA Attack

PCIe Direct Memory Access threat modeling for game security: FPGA endpoints (often M.2), host tools like [[pcileech]]/MemProcFS, and defenses that software anti-cheat alone cannot fully cover once a hostile bus-master can read RAM. (source: wiki/sources/skills/dma-attack.md)

## Threat model

Typical external DMA cheat: **cheat PC** (signatures, ESP, aim logic) + **DMA card** (FPGA in an M.2 or add-in slot issuing Memory Read TLPs) + optional **HID actuator** (USB keyboard/mouse emulator). No attacker code need run on the gaming OS—the machine sees a PCIe device performing ordinary-looking DMA mediated by chipset and (when configured) the [[iommu]]. (source: wiki/sources/skills/dma-attack.md)

Host stack in the curated list: [[pcileech]] → LeechCore → [[pcileech-fpga]] firmware; C++ developer libraries such as [[volk-dma]] (RAII LeechCore/MemProcFS wrapper — scatter I/O, signature scans, CR3 fix, kernel-derived input state) (source: wiki/sources/descriptions/lyk64__VolkDMA.md) and transport-agnostic [[vm]] (ekknod; unified `vm.h` over PCILeech/LeechCore plus kernel, user-mode, KVM, Proton, and EFI backends) (source: wiki/sources/descriptions/ekknod__vm.md); donor-cloning generators ([[pcileechgen]] — Go/VFIO donor capture → SystemVerilog/COE → Vivado bitstreams), wrappers ([[dma-invoker]], [[dma-cheat-engine-loader]], [[cheat-engine-dma-plugin]] — CE plugin swapping process memory for LeechCore DMA R/W; [[cheat-engine-ceserver-pcileech]] — remote ceserver protocol over PCILeech/LeechCore so CE scan/edit stays off the target OS), Unity Mono dump bridges such as [[unispect-dma-plugin]] (Unispect fork; fixes Razchek Memory Plugin dispose bug; cheat / game engine explorer:Unity), ReClass.NET DMA structure plugins such as [[reclass-dma]] (C/C++ plugin; ReClass memory recon over external DMA; cheat / debugging) (source: wiki/sources/descriptions/gmh5225__ReClass-DMA.md), benchmarks ([[dma-speedtest-memflow-rs]]), board utilities ([[fpga-dma-multi-tool]], [[dma-tools-rs]] — OpenOCD JTAG flash/DNA + PCILeech sanity check on Artix-7; [[memtools]] — gmh5225; Windows/Linux DMA testing via driver/plugin development and memory analysis), custom board designs such as [[dma-pcie-board-75t]] (gmh5225; Artix-7 75T PCIe DMA; firmware + HDL sources) (source: wiki/sources/descriptions/gmh5225__DMA-PCIE-BOARD-75T.md), reference endpoint cores such as [[litepcie]] (Python/Migen; DMA engines, LTSSM trace, user-space drivers; KC705/KCU105/XCU1525/Acorn) (source: wiki/sources/descriptions/enjoy-digital__litepcie.md), stealth forks ([[pcileech-dma-fullstealth]]), class-emulation firmware such as [[pcileech-fpga-dma-vmd]] (Intel RST VMD `9A0B`; MSI-X/NVMe/BAR shadow on Artix-7 75T), [[pcileech-dma-nvme-vmd]] (gmh5225; motherboard VMD/NVMe real camouflage for [[pcileech]] DMA; Windows reinstall may be needed for driver init), and [[pcileech-wifi]] (ekknod; [[pcileech-fpga]] wireless NIC class emulation for anti-cheat / DMA research) (source: wiki/sources/descriptions/ekknod__pcileech-wifi.md), disk-class frameworks such as [[ddma-1]] (gmh5225; ATA/SCSI disk-based DMA; zero target-OS software footprint) (source: wiki/sources/descriptions/gmh5225__DDMA-1.md), kernel physical patches ([[physpatch]]), title samples ([[csgo-dma-overlay]], [[fn-dma-cheat]], [[meatyeftrelease]] — EFT external radar via LeechCore/MemProcFS + DX11 fuser overlay; [[eft-dma-radar-1]] — EFT DMA radar via PCILeech-compatible hardware + separate-screen Unity player/loot/map overlay; [[nathans-tarkov-radar-public]] — public EFT radar via Vmread external or DMA + secondary-display Unity player/scav/loot/extraction overlay; [[cs2-dma-radar]] — CS2 DMA radar via PCIe hardware + real-time overlay; [[gta5-dma-cheat]] — GTA5/GTA5 Enhanced DMA cheat via MemProcFS + ImGui/DX11 overlay; Legacy/Enhanced CE offset tables incl. BattlEye patches; zero target-OS software), and cheat-base scaffolds ([[dma-cheat-base]] — rendering, animation, SDK generation). (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md) (source: wiki/sources/descriptions/mltpig__PCILeech-FPGA-DMA_VMD.md) (source: wiki/sources/descriptions/sh1ftd__dma-tools-rs.md) (source: wiki/sources/descriptions/lauralex__fn-dma-cheat.md) (source: wiki/sources/descriptions/kaijia2022__Cheat-Engine-DMA-Plugin.md) (source: wiki/sources/descriptions/kWAYTV__dma-cheat-base.md) (source: wiki/sources/descriptions/paul01784__MeatyEFTRelease.md) (source: wiki/sources/descriptions/gmh5225__eft-dma-radar-1.md) (source: wiki/sources/descriptions/gmh5225__Nathans-Tarkov-Radar-Public.md) (source: wiki/sources/descriptions/gmh5225__CS2-Dma-Radar.md) (source: wiki/sources/descriptions/fmc999__GTA5-DMA-CHEAT.md) (source: wiki/sources/descriptions/gmh5225__cheat-engine-ceserver-pcileech.md)

## Three defense layers

| Layer | Mechanism | Catches |
|-------|-----------|---------|
| PCIe fingerprinting | Config Space, BAR probes, TLP/link behavior vs donor silicon | Identity mismatch, inert BARs, stock Xilinx IDs |
| [[iommu]] enforcement | IOVA translation, ACS, interrupt remapping | Out-of-domain DMA (when active and strict) |
| External attestation | TPM Quote, measured boot, Secure Launch PCRs | Boot-chain / IOMMU-policy subversion |

Hypervisor containment ([[hvci]], EPT traps, honeypot pages) and firmware policy (pre-boot DMA protection, BIOS DXE hardening in [[x670e-tomahawk-anticheat-update]]) stack on top. (source: wiki/sources/skills/dma-attack.md)

## PCIe stack (detection-relevant)

- **TLPs:** Memory Read/Write, Config R/W, Completions; Requester ID (BDF) drives IOMMU lookup; completion splitting (MRRS/RCB/MPS) and tag turnover are donor-class fingerprints.
- **Config Space:** 256-byte legacy header + extended capabilities (AER, DSN, ATS, ACS, SR-IOV); capability-chain walk, BAR mask probe, R/W consistency on Command/Device Control and W1C bits. Kernel config-space tooling such as [[pcie-detector]] (gmh5225; C++ driver) supports defensive inventory beyond user-mode dumps for anti-cheat engineers in the Detection:DMA lane. (source: wiki/sources/descriptions/gmh5225__PCIE-Detector.md) User-mode scanner/forensics tooling such as [[drvscan]] (ekknod; C; PCIe enumeration plus pcileech-style physical-memory signature scans for cheat/rootkit residue) complements that inventory lane. (source: wiki/sources/descriptions/ekknod__drvscan.md)
- **Behavioral:** LTSSM/link width, ASPM transitions, AER correctable-error baselines, MSI/MSI-X interrupt distribution, completion-latency distribution (KS / Anderson–Darling vs donor reference).

Stock [[pcileech-fpga]] builds expose trivial Tier-0/1 signals (placeholder `10EE:0666`, zerowrite4k BAR, missing AER). Sophisticated firmware climbs tiers 2–6 (shadow config → overlay RAM → BAR MMIO + MSI → behavioral emulation → private randomized layouts). (source: wiki/sources/skills/dma-attack.md) Donor-cloning generators such as [[pcileechgen]] automate scan/check/build/validate workflows: Linux VFIO donor capture → SystemVerilog/COE → Vivado bitstreams with dynamic BAR emulation, NVMe admin-queue/DMA bridge, offline MMIO trace import, and TLP latency tuning across many PCILeech-compatible boards. (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md)

## IOMMU and bypass surface

Legitimate drivers map only explicit IOVAs; game memory should stay outside device domains. Active cheat paths include IOMMU disabled, pre-boot DMA, identity/passthrough domains, driver page over-allocation (Thunderclap class), **legitimate-path exfil** (spoofed NIC reading its own RX ring), and kernel reprogramming of IOMMU tables via [[byovd]]. Windows PoC [[diedmaprotection]] demonstrates runtime disable of DMA remapping (IOMMU/VT-d) from a kernel driver to re-enable FPGA [[pcileech]]-class physical reads. (source: wiki/sources/descriptions/iqrw0__DieDMAProtection.md) ACS Source Validation + P2P redirect and ATS-untrusted policy for untrusted endpoints are mandatory in threat models. See [[iommu]] for the condensed bypass catalog.

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

[[dma]] · [[iommu]] · [[helloiommupkg]] · [[diedmaprotection]] · [[hvci]] · [[byovd]] · [[research-rigor]] · [[pcileech]] · [[pcie-detector]] · [[drvscan]] · [[volk-dma]] · [[vm]] · [[pcileech-fpga]] · [[pcileechgen]] · [[pcileech-dma-fullstealth]] · [[pcileech-fpga-dma-vmd]] · [[pcileech-dma-nvme-vmd]] · [[pcileech-wifi]] · [[ddma-1]] · [[fpga-dma-multi-tool]] · [[dma-tools-rs]] · [[memtools]] · [[dma-pcie-board-75t]] · [[litepcie]] · [[physpatch]] · [[x670e-tomahawk-anticheat-update]] · [[dma-invoker]] · [[dma-speedtest-memflow-rs]] · [[dma-cheat-engine-loader]] · [[cheat-engine-dma-plugin]] · [[cheat-engine-ceserver-pcileech]] · [[csgo-dma-overlay]] · [[fn-dma-cheat]] · [[meatyeftrelease]] · [[eft-dma-radar-1]] · [[nathans-tarkov-radar-public]] · [[cs2-dma-radar]] · [[gta5-dma-cheat]] · [[dma-cheat-base]] · [[unispect-dma-plugin]] · [[reclass-dma]] · [[overviews/anti-cheat]]

## README map

No top-level DMA section — maps via `Cheat` (~2705) DMA lanes and `Anti Cheat > Detection:DMA` (~675), plus hypervisor/virtualization/HWID detection and `Windows Security Features` (~9; CET/shadow stack + TPM PCR attestation of virt/IOMMU/Secure Boot/VBS/HVCI/DSE/blocklist — e.g. [[sewindows]] local replay and remote attestation). (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/fsquirt__SEWindows.md)
