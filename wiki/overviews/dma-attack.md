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
  - wiki/sources/descriptions/cs1ime__ceserver-rawmem.md
  - wiki/sources/descriptions/cs1ime__blacksun-framework.md
  - wiki/sources/descriptions/cutecatsandvirtualmachines__DmaProtect.md
  - wiki/sources/descriptions/paul01784__MeatyEFTRelease.md
  - wiki/sources/descriptions/bytemyass__EFTLeecher.md
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
  - wiki/sources/descriptions/btbd__ddma.md
  - wiki/sources/descriptions/LabGuy94__Diskjacker.md
  - wiki/sources/descriptions/boowampp__ApexDmaCheatUpdated.md
  - wiki/sources/descriptions/chao-shushu__CS2-DMA.md
  - wiki/sources/descriptions/atombottle__cs2_kvm_dma.md
  - wiki/sources/descriptions/Y33Tcoder__EzApexDMAAimbot.md
  - wiki/sources/descriptions/eden13378__CS2-DMA-Cheat.md
  - wiki/sources/descriptions/gmh5225__CS2-Dma-Radar.md
  - wiki/sources/descriptions/MoZiHao__CS2_DMA_Radar.md
  - wiki/sources/descriptions/MoZiHao__CS2_DMA_Extrnal.md
  - wiki/sources/descriptions/MisterY52__apex_dma_kvm_pub.md
  - wiki/sources/descriptions/LWSS__Ape-ex-Abominations.md
  - wiki/sources/descriptions/fsquirt__SEWindows.md
  - wiki/sources/descriptions/fmc999__GTA5-DMA-CHEAT.md
  - wiki/sources/descriptions/enjoy-digital__litepcie.md
  - wiki/sources/descriptions/ekknod__vm.md
  - wiki/sources/descriptions/ekknod__pcileech-wifi.md
  - wiki/sources/descriptions/dom0ng__pcileech-wifi-v2.md
  - wiki/sources/descriptions/ekknod__drvscan.md
  - wiki/sources/descriptions/d1skq__vgk-dma-bypass.md
  - wiki/sources/descriptions/cakehonolulu__pciem.md
  - wiki/sources/descriptions/acageduser__DMA-Attack-Firmware-Customization.md
  - wiki/sources/descriptions/a0yark__ArcRaidersRadar-dma-Radar.md
  - wiki/sources/descriptions/WangXuan95__Xilinx-FPGA-PCIe-XDMA-Tutorial.md
  - wiki/sources/descriptions/Trustings__DMA_PE_Dumper.md
  - wiki/sources/descriptions/Spuckwaffel__DMALib.md
  - wiki/sources/descriptions/Metick__DMALibrary.md
  - wiki/sources/descriptions/Metick__CheatEngine-DMA.md
  - wiki/sources/descriptions/Silverr12__DMA-CFW-Guide.md
  - wiki/sources/descriptions/Rakeshmonkee__DMA.md
  - wiki/sources/descriptions/PacktPublishing__Learn-FPGA-Programming.md
  - wiki/sources/descriptions/Neverdecel__pcileech-memprocfs-mcp.md
  - wiki/sources/descriptions/NoviceLevel__Pcileech-QuantumStealth-Max.md
  - wiki/sources/descriptions/MGreif__PCILeech_DMA_Proxy.md
  - wiki/sources/descriptions/JPShag__DMA-FW-Guide-2.0.md
updated: 2026-08-24
confidence: high
---

# DMA Attack

PCIe Direct Memory Access threat modeling for game security: FPGA endpoints (often M.2), host tools like [[pcileech]]/MemProcFS, and defenses that software anti-cheat alone cannot fully cover once a hostile bus-master can read RAM. (source: wiki/sources/skills/dma-attack.md)

## Threat model

Typical external DMA cheat: **cheat PC** (signatures, ESP, aim logic) + **DMA card** (FPGA in an M.2 or add-in slot issuing Memory Read TLPs) + optional **HID actuator** (USB keyboard/mouse emulator). No attacker code need run on the gaming OS—the machine sees a PCIe device performing ordinary-looking DMA mediated by chipset and (when configured) the [[iommu]]. (source: wiki/sources/skills/dma-attack.md)

Raw physical-memory Cheat Engine ceserver via [[ceserver-rawmem]] (cs1ime; ceserver protocol over `/dev/mem` or DMA; bypasses OS process-memory APIs and anti-cheat monitoring) complements PCILeech-backed [[cheat-engine-ceserver-pcileech]] when researchers want familiar CE remote workflows on a generic physical-RAM path. (source: wiki/sources/descriptions/cs1ime__ceserver-rawmem.md)

Host stack in the curated list: [[pcileech]] → LeechCore → [[pcileech-fpga]] firmware; PE image dump tooling such as [[dma-pe-dumper]] (Trustings; C++; LeechCore/VMMDLL; CR3 shuffle + DTB patching for EXE/DLL extraction; memory forensics / AC research) (source: wiki/sources/descriptions/Trustings__DMA_PE_Dumper.md); C++ developer libraries such as [[volk-dma]] (RAII LeechCore/MemProcFS wrapper — scatter I/O, signature scans, CR3 fix, kernel-derived input state) (source: wiki/sources/descriptions/lyk64__VolkDMA.md), lightweight helpers such as [[dmalib]] (Spuckwaffel; process lookup, base resolution, R/W, pattern scan, scatter reads; cheat / DMA library) (source: wiki/sources/descriptions/Spuckwaffel__DMALib.md), broader toolkit libraries such as [[dmalibrary]] (Metick; signature scan, normal/scatter R/W, dumps, CR3 fix, PID/base lookup, import/export parsing; LeechCore/MemProcFS; cheat / DMA library) (source: wiki/sources/descriptions/Metick__DMALibrary.md), API-transparent proxies such as [[pcileech-dma-proxy]] (MGreif; DLL + loader; MinHook on process/module/thread/memory Win32 APIs; redirects calls to remote PCILeech/MemProcFS DMA with input/registry helpers; DMA-proxied game interaction research) (source: wiki/sources/descriptions/MGreif__PCILeech_DMA_Proxy.md), and transport-agnostic [[vm]] (ekknod; unified `vm.h` over PCILeech/LeechCore plus kernel, user-mode, KVM, Proton, and EFI backends) (source: wiki/sources/descriptions/ekknod__vm.md) and modular cheat frameworks with pluggable DMA backends such as [[blacksun-framework]] (cs1ime; C++; separates access backends from cheat logic; user-mode, kernel, and DMA paths) (source: wiki/sources/descriptions/cs1ime__blacksun-framework.md); donor-cloning generators ([[pcileechgen]] — Go/VFIO donor capture → SystemVerilog/COE → Vivado bitstreams), wrappers ([[dma-invoker]], [[dma-cheat-engine-loader]], [[cheat-engine-dma-plugin]] — CE plugin swapping process memory for LeechCore DMA R/W; [[cheatengine-dma]] — Metick Visual Studio C++ CE plugin with process attach, R/W, search/browse, module/thread enum, and pointer scan over DMA hardware; cheat / CheatEngine DMA) (source: wiki/sources/descriptions/Metick__CheatEngine-DMA.md); [[cheat-engine-ceserver-pcileech]] — remote ceserver protocol over PCILeech/LeechCore so CE scan/edit stays off the target OS), Unity Mono dump bridges such as [[unispect-dma-plugin]] (Unispect fork; fixes Razchek Memory Plugin dispose bug; cheat / game engine explorer:Unity), ReClass.NET DMA structure plugins such as [[reclass-dma]] (C/C++ plugin; ReClass memory recon over external DMA; cheat / debugging) (source: wiki/sources/descriptions/gmh5225__ReClass-DMA.md), benchmarks ([[dma-speedtest-memflow-rs]]), agent MCP bridges such as [[pcileech-memprocfs-mcp]] (Neverdecel; Linux-native Python MCP over memprocfs/leechcorepyc; live DMA R/W, pattern/pointer-chain/xref scans, UE/Unity SDK dump helpers, FPGA TLP control; natural-language DMA RE) (source: wiki/sources/descriptions/Neverdecel__pcileech-memprocfs-mcp.md), board utilities ([[fpga-dma-multi-tool]], [[dma-tools-rs]] — OpenOCD JTAG flash/DNA + PCILeech sanity check on Artix-7; [[memtools]] — gmh5225; Windows/Linux DMA testing via driver/plugin development and memory analysis), custom board designs such as [[dma-pcie-board-75t]] (gmh5225; Artix-7 75T PCIe DMA; firmware + HDL sources) (source: wiki/sources/descriptions/gmh5225__DMA-PCIE-BOARD-75T.md), reference endpoint cores such as [[litepcie]] (Python/Migen; DMA engines, LTSSM trace, user-space drivers; KC705/KCU105/XCU1525/Acorn) (source: wiki/sources/descriptions/enjoy-digital__litepcie.md), Vivado/XDMA educational flows such as [[xilinx-fpga-pcie-xdma-tutorial]] (WangXuan95; BRAM R/W, AXI integration, Linux host C, MPEG2 acceleration; DMA tutorial lane) (source: wiki/sources/descriptions/WangXuan95__Xilinx-FPGA-PCIe-XDMA-Tutorial.md), foundational SystemVerilog book companion code such as [[learn-fpga-programming]] (PacktPublishing; chapter-organized HDL from logic design through I2C/PS/2/VGA/DDR; FPGA fundamentals before custom DMA hardware; Guide) (source: wiki/sources/descriptions/PacktPublishing__Learn-FPGA-Programming.md), software-only synthetic device lab tools such as [[pciem]] (Linux kernel module; userspace PCIe emulation on bare metal without FPGA, VM, or QEMU—contrasts with libvfio-user) (source: wiki/sources/descriptions/cakehonolulu__pciem.md), stealth forks ([[pcileech-dma-fullstealth]], [[pcileech-quantumstealth-max]] (NoviceLevel; QuantumStealth Max Vivado firmware collection + batch scripts for M2/Squirrel/100T/Captain 75T/Enigma X1/Immortal 75T; PCIe config-space/BRAM/FIFO IP cores; memory forensics / DMA firmware research) (source: wiki/sources/descriptions/NoviceLevel__Pcileech-QuantumStealth-Max.md)), class-emulation firmware such as [[pcileech-fpga-dma-vmd]] (Intel RST VMD `9A0B`; MSI-X/NVMe/BAR shadow on Artix-7 75T), [[pcileech-dma-nvme-vmd]] (gmh5225; motherboard VMD/NVMe real camouflage for [[pcileech]] DMA; Windows reinstall may be needed for driver init), [[pcileech-wifi]] (ekknod; [[pcileech-fpga]] wireless NIC class emulation for anti-cheat / DMA research) (source: wiki/sources/descriptions/ekknod__pcileech-wifi.md), [[pcileech-wifi-v2]] (dom0ng; Verilog PCIe 7x IP + customizable device-ID scripts on the ekknod WiFi baseline) (source: wiki/sources/descriptions/dom0ng__pcileech-wifi-v2.md), [[dma-attack-firmware-customization]] (acageduser; Screamer Squirrel 35T manual RTL8111 NIC donor-cloning guide—MindShare Arbor harvest → [[pcileech-fpga]] SystemVerilog/Vivado patch; BattlEye/EAC evasion testing) (source: wiki/sources/descriptions/acageduser__DMA-Attack-Firmware-Customization.md), [[dma-cfw-guide]] (Silverr12; **pcileech-fpga v4.15** custom firmware guide for Squirrel/EnigmaX1/ZDMA—Arbor/Telescan PE donor harvest, Vivado IP patch, TLP emulation, `.coe`/writemask shadow config; anti-cheat evasion threat modeling) (source: wiki/sources/descriptions/Silverr12__DMA-CFW-Guide.md), [[dma-fw-guide-2.0]] (JPShag; comprehensive FPGA PCIe DMA device-emulation firmware guide—donor profiling, config-space clone, BAR/interrupt handling, Vivado flash workflows; PCILeech-style stack references; multi-language materials; Guide) (source: wiki/sources/descriptions/JPShag__DMA-FW-Guide-2.0.md), [[entities/dma]] (Rakeshmonkee; Vivado customization + Python/Tcl auto-generation; config-space cloning and flash workflows for FPGA DMA firmware; anti-cheat evasion research guide) (source: wiki/sources/descriptions/Rakeshmonkee__DMA.md), [[vgk-dma-bypass]] (d1skq; Artix-7 `pcileech_pcie_cfg_a7.sv` CFG-space/MSI-X fork for [[vanguard]] DMA threat-model research) (source: wiki/sources/descriptions/d1skq__vgk-dma-bypass.md), disk-class frameworks such as [[ddma-1]] (gmh5225; ATA/SCSI disk-based DMA; zero target-OS software footprint) (source: wiki/sources/descriptions/gmh5225__DDMA-1.md), disk HBA SLAT-bypass research such as [[ddma]] (btbd; ATA HBA controller DMA; Hyper-V runtime modification on bare metal; kernel/hypervisor security PoC) (source: wiki/sources/descriptions/btbd__ddma.md), runtime Hyper-V VM-exit hijacking via DDMA-style primitives such as [[diskjacker]] (LabGuy94; C++ kernel + usermode + asm stubs; low-level mapping and execution transfer; hardware/virtualization preconditions; hypervisor security PoC) (source: wiki/sources/descriptions/LabGuy94__Diskjacker.md), kernel physical patches ([[physpatch]]), title samples ([[csgo-dma-overlay]], [[fn-dma-cheat]], [[meatyeftrelease]] — EFT external radar via LeechCore/MemProcFS + DX11 fuser overlay; [[eftleecher]] — EFT DMA toolbox via MemProcFS/FPGA (visor/night/thermal/recoil/stamina/weight mods; INI config; map files; auto-disconnect OPSEC; cheat / game:eft [DMA]) (source: wiki/sources/descriptions/bytemyass__EFTLeecher.md); [[eft-dma-radar-1]] — EFT DMA radar via PCILeech-compatible hardware + separate-screen Unity player/loot/map overlay; [[nathans-tarkov-radar-public]] — public EFT radar via Vmread external or DMA + secondary-display Unity player/scav/loot/extraction overlay; [[cs2-dma-radar]] — CS2 DMA radar via PCIe hardware + real-time overlay (gmh5225) or browser tactical map via Spring Boot/WebSocket/Leaflet + VMM/LeechCore (MoZiHao; cheat / game:cs2 [DMA Radar]); [[cs2-dma-cheat]] — CS2 DMA cheat (C++; shader/rendering/audio; zero target-OS software; cheat / game:cs2 [DMA]) (source: wiki/sources/descriptions/eden13378__CS2-DMA-Cheat.md); [[cs2-dma-extrnal]] — CS2 external DMA toolset (MoZiHao; C++; LeechCore/VMMDLL; aimbot/triggerbot/radar/bhop/anti-flash; ImGui control UI; JSON offsets; zero target-OS software; cheat / game:cs2 [DMA External]) (source: wiki/sources/descriptions/MoZiHao__CS2_DMA_Extrnal.md); [[cs2-dma]] — open-source CS2 DMA external (FPGA/LeechCore; read-only ESP, LAN web radar, grenade helper; MemProcFS scatter reads; cs2-dumper offsets; zero target-OS software; cheat / game:cs2 [DMA]) (source: wiki/sources/descriptions/chao-shushu__CS2-DMA.md); [[cs2-kvm-dma]] — CS2 KVM/DMA cheat (cheat logic in separate VM or host; physical memory via DMA hardware or KVM mapping; radar/ESP rendered outside guest OS; invisible to in-guest AC; cheat / game:cs2 [KVM/DMA]) (source: wiki/sources/descriptions/atombottle__cs2_kvm_dma.md); [[gta5-dma-cheat]] — GTA5/GTA5 Enhanced DMA cheat via MemProcFS + ImGui/DX11 overlay; Legacy/Enhanced CE offset tables incl. BattlEye patches; zero target-OS software; [[apex-dma-cheat-updated]] — Apex Legends DMA external (C++; PCILeech/MemProcFS FPGA reads; aimbot/recoil/ESP/camera math; DMA memory library with input/registry/shellcode injection; cheat / game:apex legends [DMA]) (source: wiki/sources/descriptions/boowampp__ApexDmaCheatUpdated.md); [[ez-apex-dma-aimbot]] — Apex Legends KVM/DMA aimbot + glow (C/C++; KVM-based memory reader; Linux host reads game state with guest-side control; recoil randomization, non-linear smoothing, target-bone randomization, team-aware glow; experimental DMA workflow + detection-surface reduction; cheat / game:apex legends [KVM]; Y33Tcoder) (source: wiki/sources/descriptions/Y33Tcoder__EzApexDMAAimbot.md); [[apex-dma-kvm-pub]] — Apex Legends external cheat framework (MisterY52; C++ gameplay + Rust memflow + C FFI; QEMU/KVM virtualization connectors; ESP/aim/prediction; Linux build scripts; DMA/VM-assisted cheat + AC detection research; cheat / game:apex legends [KVM/DMA]) (source: wiki/sources/descriptions/MisterY52__apex_dma_kvm_pub.md); [[ape-ex-abominations]] — Apex Legends DMA-oriented cheat (LWSS; C++ feature modules + shell gdb injection/extraction/reload tooling; interface discovery + pattern scanning; QEMU/VFIO workflows; evdev-mirror kernel module input; virtualized/hardware-assisted cheat research; cheat / game:apex legends [Apex]) (source: wiki/sources/descriptions/LWSS__Ape-ex-Abominations.md); [[arc-raiders-radar-dma-radar]] — Arc Raiders DMA radar/ESP (C++; FPGA + MemProcFS; Unicorn Engine emulates game decryption for GWorld/GameInstance/CameraManager/BoneBase; player/actor iteration; cheat / game:arc raiders [DMA]; a0yark) (source: wiki/sources/descriptions/a0yark__ArcRaidersRadar-dma-Radar.md)), and cheat-base scaffolds ([[dma-cheat-base]] — rendering, animation, SDK generation). (source: wiki/sources/descriptions/sercanarga__PCILeechGen.md) (source: wiki/sources/descriptions/mltpig__PCILeech-FPGA-DMA_VMD.md) (source: wiki/sources/descriptions/sh1ftd__dma-tools-rs.md) (source: wiki/sources/descriptions/lauralex__fn-dma-cheat.md) (source: wiki/sources/descriptions/kaijia2022__Cheat-Engine-DMA-Plugin.md) (source: wiki/sources/descriptions/kWAYTV__dma-cheat-base.md) (source: wiki/sources/descriptions/paul01784__MeatyEFTRelease.md) (source: wiki/sources/descriptions/gmh5225__eft-dma-radar-1.md) (source: wiki/sources/descriptions/gmh5225__Nathans-Tarkov-Radar-Public.md) (source: wiki/sources/descriptions/gmh5225__CS2-Dma-Radar.md) (source: wiki/sources/descriptions/MoZiHao__CS2_DMA_Radar.md) (source: wiki/sources/descriptions/fmc999__GTA5-DMA-CHEAT.md) (source: wiki/sources/descriptions/gmh5225__cheat-engine-ceserver-pcileech.md)

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

Legitimate drivers map only explicit IOVAs; game memory should stay outside device domains. Active cheat paths include IOMMU disabled, pre-boot DMA, identity/passthrough domains, driver page over-allocation (Thunderclap class), **legitimate-path exfil** (spoofed NIC reading its own RX ring), and kernel reprogramming of IOMMU tables via [[byovd]]. Windows PoC [[diedmaprotection]] demonstrates runtime disable of DMA remapping (IOMMU/VT-d) from a kernel driver to re-enable FPGA [[pcileech]]-class physical reads. (source: wiki/sources/descriptions/iqrw0__DieDMAProtection.md) Defensive sample [[dmaprotect]] programs VT-d/AMD-Vi remapping tables from kernel mode to block unauthorized PCIe DMA while allowing legitimate devices—illustrating the mitigation side of the same remapping surface. (source: wiki/sources/descriptions/cutecatsandvirtualmachines__DmaProtect.md) ACS Source Validation + P2P redirect and ATS-untrusted policy for untrusted endpoints are mandatory in threat models. See [[iommu]] for the condensed bypass catalog.

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

[[dma]] · [[iommu]] · [[helloiommupkg]] · [[dmaprotect]] · [[diedmaprotection]] · [[hvci]] · [[byovd]] · [[research-rigor]] · [[pcileech]] · [[pcie-detector]] · [[drvscan]] · [[dma-pe-dumper]] · [[volk-dma]] · [[dmalib]] · [[dmalibrary]] · [[vm]] · [[pcileech-fpga]] · [[pcileechgen]] · [[pcileech-dma-fullstealth]] · [[pcileech-quantumstealth-max]] · [[pcileech-fpga-dma-vmd]] · [[pcileech-dma-nvme-vmd]] · [[pcileech-wifi]] · [[pcileech-wifi-v2]] · [[dma-attack-firmware-customization]] · [[dma-cfw-guide]] · [[dma-fw-guide-2.0]] · [[entities/dma]] · [[vgk-dma-bypass]] · [[ddma]] · [[ddma-1]] · [[diskjacker]] · [[fpga-dma-multi-tool]] · [[dma-tools-rs]] · [[memtools]] · [[dma-pcie-board-75t]] · [[litepcie]] · [[xilinx-fpga-pcie-xdma-tutorial]] · [[learn-fpga-programming]] · [[pciem]] · [[physpatch]] · [[x670e-tomahawk-anticheat-update]] · [[dma-invoker]] · [[dma-speedtest-memflow-rs]] · [[pcileech-memprocfs-mcp]] · [[dma-cheat-engine-loader]] · [[cheat-engine-dma-plugin]] · [[cheatengine-dma]] · [[cheat-engine-ceserver-pcileech]] · [[ceserver-rawmem]] · [[csgo-dma-overlay]] · [[fn-dma-cheat]] · [[meatyeftrelease]] · [[eftleecher]] · [[eft-dma-radar-1]] · [[nathans-tarkov-radar-public]] · [[cs2-dma-radar]] · [[cs2-dma-cheat]] · [[cs2-dma-extrnal]] · [[cs2-dma]] · [[cs2-kvm-dma]] · [[gta5-dma-cheat]] · [[apex-dma-cheat-updated]] · [[apex-dma-kvm-pub]] · [[ape-ex-abominations]] · [[arc-raiders-radar-dma-radar]] · [[dma-cheat-base]] · [[unispect-dma-plugin]] · [[reclass-dma]] · [[overviews/anti-cheat]]

## README map

No top-level DMA section — maps via `Cheat` (~2744) DMA lanes and `Anti Cheat > Detection:DMA` (~690), plus hypervisor/virtualization/HWID detection and `Windows Security Features` (~9; CET/shadow stack + TPM PCR attestation of virt/IOMMU/Secure Boot/VBS/HVCI/DSE/blocklist — e.g. [[sewindows]] local replay and remote attestation). (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/fsquirt__SEWindows.md)
