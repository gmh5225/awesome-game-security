---
title: Windows Kernel
kind: overview
topics: [windows-kernel]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zzhouhe__PG1903.md
  - wiki/sources/descriptions/zxd1994__vt-debuuger.md
  - wiki/sources/descriptions/zorftw__revert-mapper.md
  - wiki/sources/descriptions/zorftw__lsass-extend-mapper.md
  - wiki/sources/descriptions/zodiacon__EtwExplorer.md
  - wiki/sources/descriptions/zoand__BOOM.md
  - wiki/sources/descriptions/zer0condition__Demystifying-PatchGuard.md
  - wiki/sources/descriptions/zer0condition__NTMemory.md
  - wiki/sources/descriptions/zer0condition__hv.md
  - wiki/sources/descriptions/zer0condition__Ophion.md
  - wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md
  - wiki/sources/descriptions/weak1337__SystemThreadFinder.md
  - wiki/sources/descriptions/zer0condition__checkhv_um.md
  - wiki/sources/descriptions/void-stack__Hypervisor-Detection.md
  - wiki/sources/descriptions/valium007__BareSVM.md
  - wiki/sources/descriptions/yyl-20020115__OpenArk.md
  - wiki/sources/descriptions/yardenshafir__cet-research.md
  - wiki/sources/descriptions/yardenshafir__WinDbg_Scripts.md
  - wiki/sources/descriptions/yardenshafir__SymlinkCallback.md
  - wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md
  - wiki/sources/descriptions/xtremegamer1__xigmapper.md
  - wiki/sources/descriptions/xct__windows-kernel-exploits.md
  - wiki/sources/descriptions/xM0kht4r__VEN0m-Ransomware.md
  - wiki/sources/descriptions/xM0kht4r__AV-EDR-Killer.md
  - wiki/sources/descriptions/xaitax__NTSleuth.md
  - wiki/sources/descriptions/sonyps5201314__pdb.md
  - wiki/sources/descriptions/xPasters__.data-ptr-swap.md
  - wiki/sources/descriptions/x90skysn3k__x260-lenovo-opencore.md
  - wiki/sources/descriptions/x86matthew__WinVisor.md
  - wiki/sources/descriptions/waryas__KACE.md
  - wiki/sources/descriptions/x86matthew__InstrumentationCallbackSyscallLogger.md
  - wiki/sources/descriptions/ssnob__hidden_syscall_monitoring.md
  - wiki/sources/descriptions/wpdk__wdutf.md
  - wiki/sources/descriptions/winsiderss__systeminformer.md
  - wiki/sources/descriptions/whokilleddb__function-collections.md
  - wiki/sources/descriptions/wesmar__kvc.md
  - wiki/sources/descriptions/wesmar__KvcForensic.md
  - wiki/sources/descriptions/wesmar__WinDefCtl.md
  - wiki/sources/descriptions/wesmar__VaultGuard.md
  - wiki/sources/descriptions/wesmar__KeyboardKit.md
  - wiki/sources/descriptions/vsaint1__kernel-mouse.md
  - wiki/sources/descriptions/wesmar__KernelResearchKit.md
  - wiki/sources/descriptions/wesmar__BootBypass.md
  - wiki/sources/descriptions/utoni__PastDSE.md
  - wiki/sources/descriptions/wesmar__EfiTool.md
  - wiki/sources/descriptions/wesmar__CmdT.md
  - wiki/sources/descriptions/weak1337__EvCommunication.md
  - wiki/sources/descriptions/weak1337__DetectTpmSpoofing.md
  - wiki/sources/descriptions/synctop__tpm-mmio.md
  - wiki/sources/descriptions/wbenny__injdrv.md
  - wiki/sources/descriptions/wbenny__KSOCKET.md
  - wiki/sources/descriptions/wbaby__DoubleCallBack.md
  - wiki/sources/descriptions/wazuh__wazuh.md
  - wiki/sources/descriptions/waryas__xign_poc_april_2026.md
  - wiki/sources/descriptions/w1u0u1__kinject.md
  - wiki/sources/descriptions/sum-catnip__kptnhook.md
  - wiki/sources/descriptions/volatilityfoundation__volatility3.md
  - wiki/sources/descriptions/volatilityfoundation__volatility.md
  - wiki/sources/descriptions/vmi-rs__ephemera.md
  - wiki/sources/descriptions/tasox__miniDumpReader.md
  - wiki/sources/descriptions/skelsec__minidump.md
  - wiki/sources/descriptions/sina85__hide-file.md
  - wiki/sources/descriptions/vmcall__owned_alignment.md
  - wiki/sources/descriptions/vergamota__KslKatz.md
  - wiki/sources/descriptions/unkvolism__Solemn.md
  - wiki/sources/descriptions/un4ckn0wl3z__dioprocess-private.md
  - wiki/sources/descriptions/thetuh__anticheat-poc.md
  - wiki/sources/descriptions/thesecretclub__window_hijack.md
  - wiki/sources/descriptions/thesecretclub__callout-poc.md
  - wiki/sources/descriptions/thalium__ida_kmdf.md
  - wiki/sources/descriptions/tandasat__Sushi.md
  - wiki/sources/descriptions/tandasat__MiniVisorPkg.md
  - wiki/sources/descriptions/synacktiv__windows_kernel_shadow_stack.md
  - wiki/sources/descriptions/symeonp__Lenovo-CVE-2025-8061.md
  - wiki/sources/descriptions/sxlmnwb__windows-subsystem-linux.md
  - wiki/sources/descriptions/svnscha__mcp-windbg.md
  - wiki/sources/descriptions/supermanc88__Document.md
  - wiki/sources/descriptions/stuxnet147__PiDqSerializationWrite-Example.md
  - wiki/sources/descriptions/stuxnet147__Known-Driver-Mappers.md
  - wiki/sources/descriptions/stdhu__windows-kernel-pagehook.md
  - wiki/sources/descriptions/snare__ida-efiutils.md
updated: 2026-07-22
confidence: high
---






# Windows Kernel

Kernel internals that matter for game protection and low-level research: object/process/image callbacks, APC/attach, driver load forensics (PiDDBCache, MmUnloadedDrivers, pool), DSE/[[patchguard]]/[[hvci]], and [[byovd]] paths. (source: wiki/sources/skills/windows-kernel.md)

## Key sub-areas

- **Structures:** EPROCESS/ETHREAD, MMVAD, DRIVER_OBJECT, IRP; SSDT/IDT; pool tables
- **KMDF framework RE:** IDA Pro plugin [[ida-kmdf]] annotates WDF structures, callback registrations, I/O queues, and device-init patterns in KMDF driver binaries (type defs + named framework calls). (source: wiki/sources/descriptions/thalium__ida_kmdf.md)
- **Syscall tables:** extract `ntdll` / `win32u` SSNs via PDB + disassembly tools such as [[ntsleuth]] (JSON / C header dumps for direct-syscall research). (source: wiki/sources/descriptions/xaitax__NTSleuth.md) General Windows PDB read/merge/analyze via [[pdb]] (C++ DIA SDK; old formats + `pdb.cfg`) supports the same symbol-resolution lane for kernel/usermode debug databases. (source: wiki/sources/descriptions/sonyps5201314__pdb.md) Runtime Ring3 inspection via Instrumentation Callback (fires on every kernel-syscall return) is covered by samples such as [[instrumentation-callback-syscall-logger]]. (source: wiki/sources/descriptions/x86matthew__InstrumentationCallbackSyscallLogger.md) Title-specific monitors of hidden syscalls from Call of Duty anticheat such as [[hidden-syscall-monitoring]] sit in the same syscall-telemetry RE lane. (source: wiki/sources/descriptions/ssnob__hidden_syscall_monitoring.md) Educational Windows AC PoCs tagged Instrumentation Callback such as [[anticheat-poc]] (debugger / integrity / signature-scan / process enum) sit in the same lane. (source: wiki/sources/descriptions/thetuh__anticheat-poc.md) Broader unconventional Ring3 PoCs (memory analysis / asset pipelines) appear in collections such as [[function-collections]]. (source: wiki/sources/descriptions/whokilleddb__function-collections.md)
- **WinDbg automation:** JS WinDbg scripts such as [[windbg-scripts]] for kernel-level debug/modding workflows (Cheat → WinDbg Plugins). (source: wiki/sources/descriptions/yardenshafir__WinDbg_Scripts.md) Agent-facing CDB/WinDbg MCP via [[mcp-windbg]] (Python; crash-dump triage + remote debug sessions) sits in the same WinDbg Plugins / MCP lane. (source: wiki/sources/descriptions/svnscha__mcp-windbg.md)
- **Cross-process kernel R/W:** MDL map + physical translate + CR3 page-table walk libraries such as [[ntmemory]] (research for kernel cheat memory paths / AC evasion). (source: wiki/sources/descriptions/zer0condition__NTMemory.md) Per-process PTE hook samples such as [[windows-kernel-pagehook]] exploit shared kernel VA with distinct CR3 roots (Some Tricks / Windows Ring0 / PTE Hook). (source: wiki/sources/descriptions/stdhu__windows-kernel-pagehook.md)
- **[[kernel-callbacks]]:** process/thread/image notify, ObRegisterCallbacks, Cm/Flt; defensive enumeration/inspection via anti-rootkit GUIs such as [[openark]] (SSDT/shadow SSDT, drivers, objects); object-symlink access callbacks such as [[symlink-callback]] (LinkTarget → callback) (source: wiki/sources/descriptions/yyl-20020115__OpenArk.md) (source: wiki/sources/descriptions/yardenshafir__SymlinkCallback.md); process/file protection via FSFilter minifilter + access-blocking drivers such as [[vaultguard]] (pure x64 MASM; hide/lock/RO/block-exec; anti-debug tray GUI) (source: wiki/sources/descriptions/wesmar__VaultGuard.md); offensive kernel file-hide samples such as [[hide-file]] (C driver; cheat / hide) (source: wiki/sources/descriptions/sina85__hide-file.md); kernel APC DLL injection on process-create notify such as [[injdrv]] (`LdrLoadDll` via queued user APC) (source: wiki/sources/descriptions/wbenny__injdrv.md); map + APC kernel inject samples such as [[kinject]] (cheat / injection:windows) (source: wiki/sources/descriptions/w1u0u1__kinject.md); system-wide kernel DLL inject + function-hook drivers such as [[kptnhook]] (every process from early boot; cheat / injection:windows) (source: wiki/sources/descriptions/sum-catnip__kptnhook.md); kernel callout / spoof-stack PoCs such as [[callout-poc]] (C/C++; kernel debug) (source: wiki/sources/descriptions/thesecretclub__callout-poc.md)
- **Process / system explorers:** host inspection tools such as [[systeminformer]] (formerly Process Hacker) for process/handle/module analysis in the Cheat Windows kernel explorer lane. (source: wiki/sources/descriptions/winsiderss__systeminformer.md) Broader UM+KM+UEFI research frameworks such as [[dioprocess-private]] (Rust/Dioxus process/handle/module/network monitor; kernel events → SQLite; DSE/KPP bootkit path; Win10 22H2 IOCTL research) sit in the same explorer / internals lane. (source: wiki/sources/descriptions/un4ckn0wl3z__dioprocess-private.md) TrustedInstaller-token launchers such as [[cmdt]] (hand-coded x86/x64 asm; token duplication + privilege enablement) reach TI-ACL–protected OS components when SYSTEM alone is insufficient. (source: wiki/sources/descriptions/wesmar__CmdT.md) Windows Driver Development documentation guides such as [[document]] sit in the same Cheat / Windows kernel explorer learning lane. (source: wiki/sources/descriptions/supermanc88__Document.md)
- **Offline memory forensics:** RAM-image frameworks such as [[volatility]] (Python 2; profile-based; modules/rootkit plugins) and [[volatility3]] (Python 3; plugin-based process/network/registry/kernel-object extraction; automagic OS profiles) support post-compromise kernel-state analysis without live attach. (source: wiki/sources/descriptions/volatilityfoundation__volatility.md) (source: wiki/sources/descriptions/volatilityfoundation__volatility3.md) Multiplatform `MEMORY.DMP` analysis with a WinDbg flavor via [[ephemera]] targets faster dump inspection for AC / kernel researchers when WinDbg itself is slow. (source: wiki/sources/descriptions/vmi-rs__ephemera.md) Python minidump readers such as [[minidumpreader]] sit in the same AC / Windows kernel dump-analysis lane. (source: wiki/sources/descriptions/tasox__miniDumpReader.md) Cross-platform minidump parse libraries such as [[minidump]] (skelsec; process memory / threads / modules / exceptions; LSASS dump automation without WinDbg) extend that lane for IR and credential-extraction scripts. (source: wiki/sources/descriptions/skelsec__minidump.md)

- **Trust features:** DSE, PatchGuard, VBS/HVCI, Secure Boot; CET/shadow-stack research such as [[cet-research]] under `Windows Security Features` (source: wiki/sources/descriptions/yardenshafir__cet-research.md); kernel-mode shadow-stack / CET analysis (KVAS init, exception paths, [[patchguard]] interaction) such as [[windows-kernel-shadow-stack]] (source: wiki/sources/descriptions/synacktiv__windows_kernel_shadow_stack.md); TPM 2.0 stack integrity checks such as [[detect-tpm-spoofing]] (KMDF; compare IOCTL `TPM2_ReadPublic` to `TPM.sys` cached buffers to catch EK/public-key forgery) (source: wiki/sources/descriptions/weak1337__DetectTpmSpoofing.md); MMIO-path TPM 2.0 public Endorsement Key reads that bypass OS hooks such as [[tpm-mmio]] (source: wiki/sources/descriptions/synctop__tpm-mmio.md); DSE-bypass / unsigned-load controllers such as [[kvc]] (`g_CiOptions` via signed Microsoft driver, `skci.dll` / `SeCiCallbacks` loaders, PP/PPL→LSASS on HVCI/VBS) (source: wiki/sources/descriptions/wesmar__kvc.md); Win11 25H2 boot-time DSE / CI research kits such as [[kernel-research-kit]] (native-subsystem `SeCiCallbacks` patch, manual map / IRP hijack / BYOVD load paths, anti-loop dual-path) (source: wiki/sources/descriptions/wesmar__KernelResearchKit.md); Secure Boot / boot-manager + CI.dll early-phase DSE/HVCI bypass such as [[bootbypass]] (`subsystem:native`; smart `SeCiCallbacks` patching; independent Memory Integrity management) (source: wiki/sources/descriptions/wesmar__BootBypass.md); HVCI `HvciDisallowedImages` custom-blocklist CLIs such as [[solemn]] (automate driver disallow entries under Memory Integrity) (source: wiki/sources/descriptions/unkvolism__Solemn.md); leaked-cert + clock-rollback DSE research such as [[pastdse]]
 (VeriSign material; BlackBone PE load/reloc; date restore after sign) (source: wiki/sources/descriptions/utoni__PastDSE.md); LSA credential forensics from live LSASS / `lsass.dmp` via [[kvcforensic]] (MSV/WDigest/Kerberos/CredMan/DPAPI; Win11 24H2–26H1) (source: wiki/sources/descriptions/wesmar__KvcForensic.md); Defender real-time / Tamper Protection control via kernel privilege-escalation CLIs such as [[windefctl]] (Win11 26H1; UAC/GUI bypass, stealth execution) (source: wiki/sources/descriptions/wesmar__WinDefCtl.md)

- **[[byovd]]:** signed vulnerable drivers → kernel R/W → unsigned load / blind AC; educational kernel-exploit guides such as [[windows-kernel-exploits]] (Cheat Vulnerable Driver lane); AV/EDR-evasion research such as [[ven0m-ransomware]] via `iMFForceDelete.sys` (IObit Malware Fighter) and [[av-edr-killer]] via `wsftprm.sys` IOCTL `0x22201C` (PID in first DWORD of 1036-byte buffer); AC-driver IRP abuse such as [[xign-poc-april-2026]] (`xhunter64.sys` / XIGNCODE3: `IRP_MJ_WRITE` → phys R/W, kernel address leak, process kill); Defender-driver LSASS credential dumps such as [[kslkatz]] (`KslD.sys` → WDigest/LSA secrets past PPL/AV); OEM-driver LPE such as [[lenovo-cve-2025-8061]] (`LnvMSRIO.sys` / CVE-2025-8061 IOCTL → kernel R/W / SYSTEM shell) (source: wiki/sources/descriptions/xct__windows-kernel-exploits.md) (source: wiki/sources/descriptions/xM0kht4r__VEN0m-Ransomware.md) (source: wiki/sources/descriptions/xM0kht4r__AV-EDR-Killer.md) (source: wiki/sources/descriptions/waryas__xign_poc_april_2026.md) (source: wiki/sources/descriptions/vergamota__KslKatz.md) (source: wiki/sources/descriptions/symeonp__Lenovo-CVE-2025-8061.md)
- **Trusted-process mappers:** extend a high-trust process (e.g. lsass) and map unsigned driver code in that context to skip normal load telemetry — research ref [[lsass-extend-mapper]] (source: wiki/sources/descriptions/zorftw__lsass-extend-mapper.md)
- **Known driver mappers:** catalogs of public Driver Mapper families for AC / stress-testing research — e.g. [[known-driver-mappers]] (source: wiki/sources/descriptions/stuxnet147__Known-Driver-Mappers.md)
- **Pool / Segment Heap:** HeapKey-aware scanning for hidden modules and shellcode; post-map cleanup research such as [[revert-mapper]] (free mapping + strip pool tags / refs after unsigned-driver entry) (source: wiki/sources/descriptions/zorftw__revert-mapper.md)
- **ETW:** provider/event schema discovery (manifest + TraceLogging) via tools such as [[etw-explorer]]; ThreatIntel consumers such as [[tietwagent]] (Microsoft-Windows-Threat-Intelligence injection telemetry; krabsetw/Yara; ELAM/PPL) show how those providers feed AC/EDR detection without fragile userland hooks (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md) (source: wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md)
- **Host XDR / HIDS:** enterprise agent–manager platforms such as [[wazuh]] (intrusion detection, FIM, log correlation, Elasticsearch viz; Linux/Windows/macOS) illustrate SOC-style endpoint telemetry adjacent to AC/EDR research under README `[XDR]`. (source: wiki/sources/descriptions/wazuh__wazuh.md)
- **Hypervisor defense:** EPT-protected callback/ETW/AC pages; WHP research tracing; WHP user-mode x64 PE emulation such as [[winvisor]] (`Windows Emulator` lane); RING3 kernel-driver emulation such as [[kace]] (self context mapping or Unicorn; sandboxed AC/driver analysis); hacked-hypervisor stress/test tooling such as [[vt-debuuger]]; AMD SVM / Rust hacked-hypervisor testing such as [[baresvm]]; minimal VT-x Type-2 learning drivers such as [[hv]] (VMX root / VMCS / CPUID-MSR-CR exits); stealth Type-2 research such as [[ophion]] (EPT, CPUID cache, CR4.VMXE hide, TSC compensation, private host CR3); educational Intel VT-x research HV as UEFI + Windows drivers such as [[minivisorpkg]] (pre-OS inspect; WinDbg-friendly); user-mode HV presence checks such as [[checkhv-um]] (CPUID leaf / RDTSC timing / VMCS artifacts / signatures, no driver); multi-technique C++ detectors such as [[hypervisor-detection]] (`Detection: Hacked Hypervisor`) (source: wiki/sources/descriptions/x86matthew__WinVisor.md) (source: wiki/sources/descriptions/waryas__KACE.md) (source: wiki/sources/descriptions/zxd1994__vt-debuuger.md) (source: wiki/sources/descriptions/valium007__BareSVM.md) (source: wiki/sources/descriptions/zer0condition__hv.md) (source: wiki/sources/descriptions/zer0condition__Ophion.md) (source: wiki/sources/descriptions/tandasat__MiniVisorPkg.md) (source: wiki/sources/descriptions/zer0condition__checkhv_um.md) (source: wiki/sources/descriptions/void-stack__Hypervisor-Detection.md)
- **EFI:** pre-kernel mappers that skip normal driver-load telemetry — e.g. [[xigmapper]] (EFI manual map; payload must not be USB-hosted when studying early-load AC such as [[vanguard]]) (source: wiki/sources/descriptions/xtremegamer1__xigmapper.md); in-RAM `SYSTEM` hive patching at `ExitBootServices` such as [[efitool]] (SYSTEM shell before logon; no disk writes / no kernel driver; BitLocker PCR notes) (source: wiki/sources/descriptions/wesmar__EfiTool.md); educational research HVs with a UEFI-driver path such as [[minivisorpkg]] (pre-boot inspect alongside a Windows-driver debug build) (source: wiki/sources/descriptions/tandasat__MiniVisorPkg.md); IDA-side UEFI binary annotation via [[ida-efiutils]] (protocol GUIDs, Boot/Runtime Services, PEI/DXE entry points; `[EFI binaries]`) (source: wiki/sources/descriptions/snare__ida-efiutils.md); Hackintosh OpenCore EFI packs such as [[x260-lenovo-opencore]] (ThinkPad X260) are a separate EFI lane for macOS-on-PC research hosts rather than cheat mapping. (source: wiki/sources/descriptions/x90skysn3k__x260-lenovo-opencore.md)
- **Legitimate-driver hijack / stealth I/O:** research such as [[boom]] hijacks `Beep.sys` and changes communication so Ring0↔usermode paths are less obvious to AC telemetry; composition-surface channels such as [[data-ptr-swap]] (`NtSetCompositionSurfaceAnalogExclusive`) sit in the same cheat / driver-communication lane; kernel DWM composition samples such as [[double-callback]] (C/C++; DWM in kernel / render-draw) ride the same composition stack from Ring0; named-event channels such as [[evcommunication]] (`Zw*Event` + `NtTokenManager` hook; `MmCopyVirtualMemory` R/W) avoid monitored IOCTL surfaces; window-handle hijack drivers such as [[window-hijack]] (thread-context / window-object KM↔UM channel) sit in the same stealth-I/O lane; alignment-abuse driver/hook samples such as [[owned-alignment]] target cheat / HWID Ring0 surfaces. (source: wiki/sources/descriptions/zoand__BOOM.md) (source: wiki/sources/descriptions/xPasters__.data-ptr-swap.md) (source: wiki/sources/descriptions/wbaby__DoubleCallBack.md) (source: wiki/sources/descriptions/weak1337__EvCommunication.md) (source: wiki/sources/descriptions/thesecretclub__window_hijack.md) (source: wiki/sources/descriptions/vmcall__owned_alignment.md)
- **Keyboard IRP filter / keylog research:** educational samples such as [[keyboardkit]] intercept keyboard IRPs in a filter driver, exfiltrate via UDP usermode, and demonstrate ExplorerFrame DLL-hijack persistence (offensive + defensive IRP-hook analysis). (source: wiki/sources/descriptions/wesmar__KeyboardKit.md)
- **MouClass / kernel mouse input:** research drivers such as [[kernel-mouse]] target mouClass on Windows 10/11 for cheat / triggerbot & aimbot input-path study. (source: wiki/sources/descriptions/vsaint1__kernel-mouse.md)
- **Kernel-mode sockets (WSK):** BSD-style wrappers such as [[ksocket]] expose TCP/UDP from ring 0 via Windows Sockets Kernel with no user-mode component—covert kernel network-channel research. (source: wiki/sources/descriptions/wbenny__KSOCKET.md)
- **System / hidden threads:** detectors such as [[system-thread-finder]] enumerate threads (`NtQuerySystemInformation`) and flag start addresses outside loaded driver images (BE-style manual-map thread heuristics). (source: wiki/sources/descriptions/weak1337__SystemThreadFinder.md) PoCs such as [[zero-thread-kernel]] evade that lane by running via existing contexts / timers instead of new system threads. (source: wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md)
- **Driver unit testing:** frameworks such as [[wdutf]] host Microsoft C++ unit tests in user space against kernel-driver code (AC / defensive driver harness lane). (source: wiki/sources/descriptions/wpdk__wdutf.md)


Version-specific PatchGuard research (e.g. [[pg1903]] on Win10 1903 via context-page NX manipulation) illustrates how PG bypass studies map to the Demo NX / Cheat PatchGuard README lane. (source: wiki/sources/descriptions/zzhouhe__PG1903.md) Educational demystification material such as [[demystifying-patchguard]] sits in the same lane for RE of [[patchguard]] internals. (source: wiki/sources/descriptions/zer0condition__Demystifying-PatchGuard.md) PG monitoring tooling such as [[sushi]] targets the same cheat / PatchGuard-related area. (source: wiki/sources/descriptions/tandasat__Sushi.md)

## Related concepts

[[kernel-callbacks]] · [[callout-poc]] · [[byovd]] · [[windows-kernel-exploits]] · [[ven0m-ransomware]] · [[av-edr-killer]] · [[xign-poc-april-2026]] · [[lenovo-cve-2025-8061]] · [[kvc]] · [[kernel-research-kit]] · [[bootbypass]] · [[solemn]] · [[pastdse]] · [[kvcforensic]] · [[windefctl]] · [[vaultguard]] · [[hide-file]] · [[keyboardkit]] · [[kernel-mouse]] · [[ksocket]] · [[hvci]] · [[cet-research]] · [[windows-kernel-shadow-stack]] · [[detect-tpm-spoofing]] · [[tpm-mmio]]
 · [[windbg-scripts]] · [[mcp-windbg]] · [[symlink-callback]] · [[patchguard]] · [[pg1903]] · [[demystifying-patchguard]] · [[sushi]] · [[ntmemory]] · [[pdb]] · [[ntsleuth]] · [[instrumentation-callback-syscall-logger]] · [[hidden-syscall-monitoring]] · [[anticheat-poc]] · [[function-collections]] · [[winvisor]] · [[kace]] · [[hv]] · [[ophion]] · [[minivisorpkg]] · [[checkhv-um]] · [[hypervisor-detection]] · [[vt-debuuger]] · [[baresvm]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[known-driver-mappers]] · [[xigmapper]] · [[efitool]] · [[ida-efiutils]] · [[cmdt]] · [[x260-lenovo-opencore]] · [[etw-explorer]] · [[tietwagent]] · [[wazuh]] · [[openark]] · [[systeminformer]] · [[document]] · [[dioprocess-private]] · [[volatility]] · [[volatility3]] · [[ephemera]] · [[system-thread-finder]]
 · [[boom]] · [[data-ptr-swap]] · [[double-callback]] · [[window-hijack]] · [[owned-alignment]] · [[injdrv]] · [[kinject]] · [[kptnhook]] · [[zero-thread-kernel]] · [[pidqserializationwrite-example]] · [[windows-kernel-pagehook]] · [[wdutf]] · [[ida-kmdf]] · [[windows-subsystem-linux]] · [[dma]] · [[overviews/anti-cheat]]




## README map

Cheat PatchGuard/DSE/Windows Kernel Explorer/Vulnerable Driver; Anti Cheat Detection:Attach|Hide|Vulnerable Driver|Hacked Hypervisor; `Windows Security Features` (~9: CET/shadow stack, TPM PCR attestation of virt/IOMMU/Secure Boot/VBS/HVCI/DSE/blocklist); `Some Tricks` (~113) `> Windows Ring0` (Unity-centric `PiDqSerializationWrite` samples such as [[pidqserializationwrite-example]]) (source: wiki/sources/descriptions/stuxnet147__PiDqSerializationWrite-Example.md); adjacent `Windows Emulator` (~7; WHP trap-driven guests + hybrid semi-emulated/semi-native kernel-driver stacks such as KDemu for rootkit/AC analysis) and `WSL` (~4; WSL2 Linux-kernel research hosts such as [[windows-subsystem-linux]]). (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/sxlmnwb__windows-subsystem-linux.md)
