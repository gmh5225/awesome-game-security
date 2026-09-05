---
title: DMA (Direct Memory Access)
kind: concept
topics: [dma-attack, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md
  - wiki/sources/descriptions/un4ckn0wl3z__DMAInvoker.md
  - wiki/sources/descriptions/un4ckn0wl3z__DMACheatEngineLoader.md
  - wiki/sources/descriptions/ufrisk__pcileech.md
  - wiki/sources/descriptions/ufrisk__pcileech-fpga.md
  - wiki/sources/descriptions/sonodima__physpatch.md
  - wiki/sources/descriptions/slack69__csgo-dma-overlay.md
  - wiki/sources/descriptions/sh1ftd__dma-speedtest-memflow-rs.md
  - wiki/sources/descriptions/realquantumstealth-hub__PCILeech-DMA-Fullstealth.md
  - wiki/sources/descriptions/mltpig__PCILeech-FPGA-DMA_VMD.md
  - wiki/sources/descriptions/sercanarga__fpga-dma-multi-tool.md
  - wiki/sources/descriptions/sh1ftd__dma-tools-rs.md
  - wiki/sources/descriptions/kaijia2022__Cheat-Engine-DMA-Plugin.md
  - wiki/sources/descriptions/kWAYTV__dma-cheat-base.md
  - wiki/sources/descriptions/sercanarga__PCILeechGen.md
  - wiki/sources/descriptions/sercanarga__pcileechgen.md
  - wiki/sources/descriptions/lyk64__VolkDMA.md
  - wiki/sources/descriptions/gmh5225__Pcileech-DMA-NVMe-VMD.md
  - wiki/sources/descriptions/gmh5225__PCIE-Detector.md
  - wiki/sources/descriptions/gmh5225__MemTools.md
  - wiki/sources/descriptions/gmh5225__DMA-PCIE-BOARD-75T.md
  - wiki/sources/descriptions/gmh5225__DDMA-1.md
  - wiki/sources/descriptions/btbd__ddma.md
  - wiki/sources/descriptions/enjoy-digital__litepcie.md
  - wiki/sources/descriptions/ekknod__pcileech-wifi.md
  - wiki/sources/descriptions/ekknod__drvscan.md
  - wiki/sources/descriptions/cakehonolulu__pciem.md
  - wiki/sources/descriptions/WangXuan95__Xilinx-FPGA-PCIe-XDMA-Tutorial.md
  - wiki/sources/descriptions/Trustings__DMA_PE_Dumper.md
  - wiki/sources/descriptions/Spuckwaffel__DMALib.md
  - wiki/sources/descriptions/Metick__DMALibrary.md
  - wiki/sources/descriptions/Metick__CheatEngine-DMA.md
  - wiki/sources/descriptions/PacktPublishing__Learn-FPGA-Programming.md
  - wiki/sources/descriptions/NoviceLevel__Pcileech-QuantumStealth-Max.md
  - wiki/sources/descriptions/MGreif__PCILeech_DMA_Proxy.md
  - wiki/sources/descriptions/JPShag__DMA-FW-Guide-2.0.md
  - wiki/sources/descriptions/JOKOSAHS__DMA-Pcileech.md
  - wiki/sources/descriptions/Herooyyy__Pcileech-Intel-I226-V-FullEmu.md
  - wiki/sources/descriptions/Herooyyy__Pcileech-ISABridge.md
  - wiki/sources/descriptions/Herooyyy__Pcileech-Activator-Anti-crack.md
  - wiki/sources/descriptions/Herooyyy__Pcileech-AMDPCI.md
  - wiki/sources/descriptions/Herooyyy__Free-DMA-Firmware-pcileech.md
  - wiki/sources/descriptions/16SalomonArs__Pcileech-DMA-Firmware-Guide.md
  - wiki/sources/descriptions/12i192i1043__pcileech-cmedia-cmi8738.md
updated: 2026-09-05
confidence: high
---


# DMA (Direct Memory Access)

Hardware-level memory access where a PCIe device issues Memory Read/Write TLPs against host RAM via Bus Master, without executing attacker code in the gaming OS. In game security this usually means an FPGA card (often M.2) linked to a separate cheat PC. (source: wiki/sources/skills/dma-attack.md) Host tooling such as [[pcileech]] drives those PCIe devices for target-memory R/W over DMA. (source: wiki/sources/descriptions/ufrisk__pcileech.md) Device firmware/HDL for those endpoints lives in [[pcileech-fpga]] (Vivado flows, TLP/BAR/config-space shadow across many boards). (source: wiki/sources/descriptions/ufrisk__pcileech-fpga.md) Fullstealth-oriented builds such as [[pcileech-dma-fullstealth]] (Quantumstealth; M2/Squirrel/Captain 75T/Enigma X1) extend that firmware lane for stealth/threat-modeling research. (source: wiki/sources/descriptions/realquantumstealth-hub__PCILeech-DMA-Fullstealth.md) [[pcileech-quantumstealth-max]] (NoviceLevel; multi-board QuantumStealth Max Vivado collection with PCIe config-space/BRAM/FIFO IP cores and batch build scripts for 100T/Squirrel/Captain/M2/Enigma X1/Immortal 75T) complements that lane for firmware developers and memory-forensics researchers. (source: wiki/sources/descriptions/NoviceLevel__Pcileech-QuantumStealth-Max.md) Class-emulation forks such as [[pcileech-fpga-dma-vmd]] (Intel RST VMD `9A0B`; MSI-X, NVMe command path, configurable BARs, TLP config shadow on XC7A75T), [[pcileech-dma-nvme-vmd]] (gmh5225; motherboard VMD/NVMe camouflage for [[pcileech]] DMA), [[pcileech-wifi]] (ekknod; wireless NIC emulation on [[pcileech-fpga]]), [[dma-pcileech]] (JOKOSAHS; open-source network-card-style [[pcileech-fpga]] firmware for Screamer M2/Enigma X1/Squirrel; TLP/config-space shadow/BAR/FT601; educational release after ACE network-card firmware detection) (source: wiki/sources/descriptions/JOKOSAHS__DMA-Pcileech.md), and prebuilt Intel I225/I226 wired-NIC releases such as [[pcileech-intel-i226-v-fullemu]] (Herooyyy; synthetic TCP + persistent active-link emulation for activity-based AC checks) (source: wiki/sources/descriptions/Herooyyy__Pcileech-Intel-I226-V-FullEmu.md) and ISA-bridge-style [[pcileech-isabridge]] firmware (Herooyyy; Verilog/Vivado; PID/VID spoofing through bridge-device simulation for Faceit-class PCIe identity filtering research) (source: wiki/sources/descriptions/Herooyyy__Pcileech-ISABridge.md), and AMD PCI device-model [[pcileech-amdpci]] firmware (Herooyyy; Verilog/SystemVerilog + Vivado IP; 35T/75T/ZDMA build scripts; no-interrupt communication + hardware identity spoofing for Faceit/Vanguard signature research) (source: wiki/sources/descriptions/Herooyyy__Pcileech-AMDPCI.md), legacy audio-class [[pcileech-cmedia-cmi8738]] firmware (12i192i1043; C-Media CMI8738/PCI-SX donor config space + full BAR0; null audio endpoint with interrupts; optional fake MRd bus-activity generator; PCILeech DMA path isolated) (source: wiki/sources/descriptions/12i192i1043__pcileech-cmedia-cmi8738.md), [[free-dma-firmware-pcileech]] (Herooyyy; Verilog/SystemVerilog + Vivado IP; config-space + MSI-X interrupt patterns; multiple hardware persona profiles; VGK/Faceit low-level DMA bypass research) (source: wiki/sources/descriptions/Herooyyy__Free-DMA-Firmware-pcileech.md) raise PCIe behavioral probes toward storage- and network-controller tiers. (source: wiki/sources/descriptions/ekknod__pcileech-wifi.md) (source: wiki/sources/descriptions/mltpig__PCILeech-FPGA-DMA_VMD.md) (source: wiki/sources/descriptions/gmh5225__Pcileech-DMA-NVMe-VMD.md) [[pcileech-activator-anti-crack]] (Herooyyy; FT601 SystemVerilog configs plus C++ activation-signal analysis documenting commercial panel signal registers, state machines, and anti-crack flags on licensed [[pcileech-fpga]] bitstreams) (source: wiki/sources/descriptions/Herooyyy__Pcileech-Activator-Anti-crack.md) documents the firmware **licensing/activation layer** beneath those class-emulation forks. Disk-class DMA frameworks such as [[ddma-1]] (gmh5225; ATA/SCSI presentation; external PCIe R/W with no target-OS cheat footprint) extend that camouflage lane beyond NVMe/VMD. (source: wiki/sources/descriptions/gmh5225__DDMA-1.md) Research PoCs such as [[ddma]] (btbd; HBA ATA disk-controller DMA; SLAT/EPT circumvention when hypervisors pass through unvirtualized storage; Hyper-V runtime modification demonstrated) study hypervisor containment gaps separate from external cheat hardware. (source: wiki/sources/descriptions/btbd__ddma.md)

## Why it matters

Software anti-cheat sees a “normal” PCIe endpoint. Classic process/handle/injection signals may be absent. Defense shifts to PCIe fingerprinting, [[iommu]] policy, hypervisor containment, TPM/measured-boot attestation, and occasionally firmware-level blocks (e.g. BIOS DXE option-ROM attribute stripping in [[x670e-tomahawk-anticheat-update]]). (source: wiki/sources/descriptions/zer0condition__x670e-tomahawk-anticheat-update.md) Physical-page patching tools such as [[physpatch]] (VA→PA walk then direct physical write) illustrate how DMA-class access can alter kernel memory while bypassing software hooks and access monitors. (source: wiki/sources/descriptions/sonodima__physpatch.md)


## Typical stack

Cheat app → LeechCore/pcileech/MemProcFS → FPGA firmware → Memory Read TLPs → walk CR3/page tables → game state; optional HID actuator for input. PE dump tooling such as [[dma-pe-dumper]] (Trustings; C++; LeechCore/VMMDLL; CR3 shuffle + DTB patching for EXE/DLL extraction; memory forensics / AC research) (source: wiki/sources/descriptions/Trustings__DMA_PE_Dumper.md) complements that stack for offline image recovery. Developer libraries such as [[volk-dma]] wrap that LeechCore/MemProcFS path in C++ (RAII sessions, scatter I/O, signature scans, CR3 fix via patched VMM, kernel-derived cursor/keyboard/mouse state without local hooks). (source: wiki/sources/descriptions/lyk64__VolkDMA.md) Lightweight helper libraries such as [[dmalib]] (Spuckwaffel; C++; process lookup, base resolution, R/W, pattern scan, scatter reads over LeechCore/MemProcFS) offer a minimal reusable layer for DMA cheat and research tooling. (source: wiki/sources/descriptions/Spuckwaffel__DMALib.md) Broader C++ toolkit libraries such as [[dmalibrary]] (Metick; signature scan, normal/scatter R/W, dumps, CR3 fix, PID/base lookup, import/export parsing; LeechCore/MemProcFS; cheat / DMA library) sit in the same developer layer. (source: wiki/sources/descriptions/Metick__DMALibrary.md) API-transparent Win32 proxies such as [[pcileech-dma-proxy]] (MGreif; MinHook DLL + loader; standard memory/process/module/thread APIs backed by remote PCILeech/MemProcFS DMA; input/registry access) let local tools exercise external memory without rewriting call sites. (source: wiki/sources/descriptions/MGreif__PCILeech_DMA_Proxy.md) Host-side DMA RPM wrappers such as [[dma-invoker]] ([[dmalibrary]]-backed) sit in the cheat-app layer for Windows process-memory reads. (source: wiki/sources/descriptions/un4ckn0wl3z__DMAInvoker.md) Benchmarks such as [[dma-speedtest-memflow-rs]] (memflow; PCILeech/native; throughput/latency) help characterize that hardware path. (source: wiki/sources/descriptions/sh1ftd__dma-speedtest-memflow-rs.md) Windows board utilities such as [[fpga-dma-multi-tool]] (Artix-7 detect/flash via openFPGALoader + DMA R/W speedtest) and [[dma-tools-rs]] (Rust/egui; OpenOCD + CH347/FTDI RS232 JTAG; Artix-7 35T/75T/100T bitstream + DNA; PCILeech sanity check via memflow-base) sit in the FPGA bring-up layer before host DMA apps. (source: wiki/sources/descriptions/sercanarga__fpga-dma-multi-tool.md) (source: wiki/sources/descriptions/sh1ftd__dma-tools-rs.md) Cross-platform testing tooling such as [[memtools]] (gmh5225; C++/C; Windows/Linux driver and plugin development plus memory analysis) validates DMA paths in the same bring-up lane. (source: wiki/sources/descriptions/gmh5225__MemTools.md) Custom Artix-7 board designs such as [[dma-pcie-board-75t]] (gmh5225; 75T FPGA; firmware/HDL for PCIe DMA R/W) complement upstream [[pcileech-fpga]] flows in that layer. (source: wiki/sources/descriptions/gmh5225__DMA-PCIE-BOARD-75T.md) Reference endpoint cores such as [[litepcie]] (Python/Migen; DMA engines, LTSSM tracing, user-space drivers) support PCIe endpoint and link-layer research outside the Vivado [[pcileech-fpga]] lane. (source: wiki/sources/descriptions/enjoy-digital__litepcie.md) Hands-on Xilinx **XDMA** tutorials such as [[xilinx-fpga-pcie-xdma-tutorial]] (Vivado; BRAM R/W, AXI, Linux host C, MPEG2 workflow) teach PCIe DMA engine bring-up before adapting silicon toward [[pcileech-fpga]]-class endpoints. (source: wiki/sources/descriptions/WangXuan95__Xilinx-FPGA-PCIe-XDMA-Tutorial.md) Foundational **SystemVerilog** coursework such as [[learn-fpga-programming]] (PacktPublishing; logic design through I2C/PS/2/VGA/DDR; HDL literacy before custom DMA firmware) sits earlier in that education lane. (source: wiki/sources/descriptions/PacktPublishing__Learn-FPGA-Programming.md) Curated firmware walkthrough guides such as [[dma-fw-guide-2.0]] (JPShag; donor profiling → PCIe config clone → BAR/interrupt handling → Vivado flash; PCILeech-style stack references; multi-language materials; Guide) document manual FPGA DMA emulation paths alongside [[dma-cfw-guide]], [[pcileech-dma-firmware-guide]] (16SalomonArs; Windows-first full donor emulation—shadow config, writemask protection, capability/TLP work; Squirrel/CaptainDMA/LeetDMA/Enigma/ZDMA; cold-boot validation and recovery; Guide) (source: wiki/sources/descriptions/16SalomonArs__Pcileech-DMA-Firmware-Guide.md), and [[entities/dma]]. (source: wiki/sources/descriptions/JPShag__DMA-FW-Guide-2.0.md) Software-only synthetic device frameworks such as [[pciem]] (Linux kernel; virtual PCIe endpoints on bare metal without FPGA or VM) let researchers study PCI enumeration and driver binding before hardware bring-up. (source: wiki/sources/descriptions/cakehonolulu__pciem.md) Donor-cloning firmware generators such as [[pcileechgen]] (Go; Linux VFIO capture of config space, BARs, and capabilities → SystemVerilog → Vivado bitstreams; scan/check/build/validate; dynamic BAR emulation, NVMe admin-queue/DMA bridge, offline MMIO traces, MSI-X, TLP latency tuning) automate moving from real PCIe silicon to flash-ready [[pcileech-fpga]]-class firmware. (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md) CE-facing DMA loaders such as [[dma-cheat-engine-loader]] (copy CE into `DMACE`; closed-source) bridge classic Cheat Engine installs onto that external DMA path. (source: wiki/sources/descriptions/un4ckn0wl3z__DMACheatEngineLoader.md) The [[cheat-engine-dma-plugin]] (C/C++; LeechCore/pcileech) replaces CE's process-memory backend with DMA physical R/W for scan/edit without OS-visible process access. (source: wiki/sources/descriptions/kaijia2022__Cheat-Engine-DMA-Plugin.md) [[cheatengine-dma]] (Metick; Visual Studio C++ CE plugin; process attach, R/W, search/browse, module/thread enum, pointer scan over DMA hardware) offers a fuller CE-facing plugin stack from the same author lane as [[dmalibrary]]. (source: wiki/sources/descriptions/Metick__CheatEngine-DMA.md) Game-facing samples such as [[csgo-dma-overlay]] pair DMA reads with an overlay for CS:GO research. (source: wiki/sources/descriptions/slack69__csgo-dma-overlay.md) Reusable cheat-base scaffolds such as [[dma-cheat-base]] (C/C++; rendering, animation, SDK generation) sit in the same external-DMA development lane. (source: wiki/sources/descriptions/kWAYTV__dma-cheat-base.md)

## Anti-cheat detection pipeline

No single PCIe or IOMMU signal is durable; production AC layers **causally distinct** evidence and validates joint false-positive rates. (source: wiki/sources/skills/anti-cheat.md)

**Pre-game / inventory:** IOMMU active, interrupt remapping, Secure Boot, VBS/[[hvci]], TPM provisioned, ACS topology verified; full 4 KB config dump per device cross-checked with SMBIOS slots. Kernel config-space drivers such as [[pcie-detector]] (gmh5225) support that inventory lane from ring 0 for Detection:DMA research. (source: wiki/sources/descriptions/gmh5225__PCIE-Detector.md) Scanner/forensics tooling such as [[drvscan]] (ekknod; C; PCIe device enumeration plus pcileech-style physical-memory signature scans) extends the same defensive lane from user mode. (source: wiki/sources/descriptions/ekknod__drvscan.md)

**PCIe-layer checks:** VID/DID/SVID/SDID allowlists; capability-chain integrity; Xilinx/signature-residue patterns; BAR mask vs donor model; BAR memory probes (register layouts for NIC/NVMe/XHCI classes); R/W consistency on writable and W1C bits; link-state and AER baselining; completion-latency distribution tests (KS, Anderson–Darling, Hill tail index).

**Behavioral / cheat-phase:** slow broad discovery then narrow periodic reads; honeypot regions with [[iommu]] fault logging or hypervisor EPT traps; frame-aligned access autocorrelation.

**IOMMU containment (live match):** sandbox domain remapping, Bus Master Enable clear, Downstream Port Containment, AC-owned device domains—containment before attribution.

**External trust anchors:** TPM2_Quote with fresh nonce when local kernel trust fails; PCR[7] DMA Protection Disabled; UEFI DMAR/IVRS and BIOS CVE cross-check.

**Firmware sophistication tiers (detection mapping):** Tier 0 stock VID/DID blacklist → Tier 6 private firmware requiring attestation. Verdicts should require multi-signal correlation, not a fixed signal count.

## Related

[[iommu]] · [[hvci]] · [[pcileech]] · [[pcileech-dma-proxy]] · [[pcie-detector]] · [[drvscan]] · [[dma-pe-dumper]] · [[volk-dma]] · [[dmalib]] · [[dmalibrary]] · [[pcileech-fpga]] · [[pcileechgen]] · [[pcileech-dma-fullstealth]] · [[pcileech-quantumstealth-max]] · [[pcileech-dma-nvme-vmd]] · [[pcileech-wifi]] · [[ddma]] · [[ddma-1]] · [[fpga-dma-multi-tool]] · [[dma-tools-rs]] · [[memtools]] · [[dma-pcie-board-75t]] · [[litepcie]] · [[xilinx-fpga-pcie-xdma-tutorial]] · [[learn-fpga-programming]] · [[dma-fw-guide-2.0]] · [[dma-cfw-guide]] · [[pcileech-dma-firmware-guide]] · [[entities/dma]] · [[pciem]] · [[physpatch]] · [[x670e-tomahawk-anticheat-update]] · [[dma-invoker]] · [[dma-speedtest-memflow-rs]] · [[dma-cheat-engine-loader]] · [[cheat-engine-dma-plugin]] · [[cheatengine-dma]] · [[csgo-dma-overlay]] · [[dma-cheat-base]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]

