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
  - wiki/sources/descriptions/xPasters__.data-ptr-swap.md
  - wiki/sources/descriptions/x90skysn3k__x260-lenovo-opencore.md
  - wiki/sources/descriptions/x86matthew__WinVisor.md
  - wiki/sources/descriptions/waryas__KACE.md
  - wiki/sources/descriptions/x86matthew__InstrumentationCallbackSyscallLogger.md
  - wiki/sources/descriptions/wpdk__wdutf.md
  - wiki/sources/descriptions/winsiderss__systeminformer.md
  - wiki/sources/descriptions/whokilleddb__function-collections.md
  - wiki/sources/descriptions/wesmar__kvc.md
  - wiki/sources/descriptions/wesmar__KvcForensic.md
  - wiki/sources/descriptions/wesmar__WinDefCtl.md
  - wiki/sources/descriptions/wesmar__VaultGuard.md
  - wiki/sources/descriptions/wesmar__KeyboardKit.md
  - wiki/sources/descriptions/wesmar__KernelResearchKit.md
  - wiki/sources/descriptions/wesmar__BootBypass.md
  - wiki/sources/descriptions/wesmar__EfiTool.md
  - wiki/sources/descriptions/weak1337__EvCommunication.md
  - wiki/sources/descriptions/weak1337__DetectTpmSpoofing.md
  - wiki/sources/descriptions/wbenny__injdrv.md
  - wiki/sources/descriptions/wbenny__KSOCKET.md
  - wiki/sources/descriptions/wbaby__DoubleCallBack.md
  - wiki/sources/descriptions/wazuh__wazuh.md
  - wiki/sources/descriptions/waryas__xign_poc_april_2026.md
  - wiki/sources/descriptions/w1u0u1__kinject.md
updated: 2026-07-19
confidence: high
---




# Windows Kernel

Kernel internals that matter for game protection and low-level research: object/process/image callbacks, APC/attach, driver load forensics (PiDDBCache, MmUnloadedDrivers, pool), DSE/[[patchguard]]/[[hvci]], and [[byovd]] paths. (source: wiki/sources/skills/windows-kernel.md)

## Key sub-areas

- **Structures:** EPROCESS/ETHREAD, MMVAD, DRIVER_OBJECT, IRP; SSDT/IDT; pool tables
- **Syscall tables:** extract `ntdll` / `win32u` SSNs via PDB + disassembly tools such as [[ntsleuth]] (JSON / C header dumps for direct-syscall research). (source: wiki/sources/descriptions/xaitax__NTSleuth.md) Runtime Ring3 inspection via Instrumentation Callback (fires on every kernel-syscall return) is covered by samples such as [[instrumentation-callback-syscall-logger]]. (source: wiki/sources/descriptions/x86matthew__InstrumentationCallbackSyscallLogger.md) Broader unconventional Ring3 PoCs (memory analysis / asset pipelines) appear in collections such as [[function-collections]]. (source: wiki/sources/descriptions/whokilleddb__function-collections.md)
- **WinDbg automation:** JS WinDbg scripts such as [[windbg-scripts]] for kernel-level debug/modding workflows (Cheat → WinDbg Plugins). (source: wiki/sources/descriptions/yardenshafir__WinDbg_Scripts.md)
- **Cross-process kernel R/W:** MDL map + physical translate + CR3 page-table walk libraries such as [[ntmemory]] (research for kernel cheat memory paths / AC evasion). (source: wiki/sources/descriptions/zer0condition__NTMemory.md)
- **[[kernel-callbacks]]:** process/thread/image notify, ObRegisterCallbacks, Cm/Flt; defensive enumeration/inspection via anti-rootkit GUIs such as [[openark]] (SSDT/shadow SSDT, drivers, objects); object-symlink access callbacks such as [[symlink-callback]] (LinkTarget → callback) (source: wiki/sources/descriptions/yyl-20020115__OpenArk.md) (source: wiki/sources/descriptions/yardenshafir__SymlinkCallback.md); process/file protection via FSFilter minifilter + access-blocking drivers such as [[vaultguard]] (pure x64 MASM; hide/lock/RO/block-exec; anti-debug tray GUI) (source: wiki/sources/descriptions/wesmar__VaultGuard.md); kernel APC DLL injection on process-create notify such as [[injdrv]] (`LdrLoadDll` via queued user APC) (source: wiki/sources/descriptions/wbenny__injdrv.md); map + APC kernel inject samples such as [[kinject]] (cheat / injection:windows) (source: wiki/sources/descriptions/w1u0u1__kinject.md)
- **Process / system explorers:** host inspection tools such as [[systeminformer]] (formerly Process Hacker) for process/handle/module analysis in the Cheat Windows kernel explorer lane. (source: wiki/sources/descriptions/winsiderss__systeminformer.md)
- **Trust features:** DSE, PatchGuard, VBS/HVCI, Secure Boot; CET/shadow-stack research such as [[cet-research]] under `Windows Security Features` (source: wiki/sources/descriptions/yardenshafir__cet-research.md); TPM 2.0 stack integrity checks such as [[detect-tpm-spoofing]] (KMDF; compare IOCTL `TPM2_ReadPublic` to `TPM.sys` cached buffers to catch EK/public-key forgery) (source: wiki/sources/descriptions/weak1337__DetectTpmSpoofing.md); DSE-bypass / unsigned-load controllers such as [[kvc]] (`g_CiOptions` via signed Microsoft driver, `skci.dll` / `SeCiCallbacks` loaders, PP/PPL→LSASS on HVCI/VBS) (source: wiki/sources/descriptions/wesmar__kvc.md); Win11 25H2 boot-time DSE / CI research kits such as [[kernel-research-kit]] (native-subsystem `SeCiCallbacks` patch, manual map / IRP hijack / BYOVD load paths, anti-loop dual-path) (source: wiki/sources/descriptions/wesmar__KernelResearchKit.md); Secure Boot / boot-manager + CI.dll early-phase DSE/HVCI bypass such as [[bootbypass]] (`subsystem:native`; smart `SeCiCallbacks` patching; independent Memory Integrity management) (source: wiki/sources/descriptions/wesmar__BootBypass.md); LSA credential forensics from live LSASS / `lsass.dmp` via [[kvcforensic]] (MSV/WDigest/Kerberos/CredMan/DPAPI; Win11 24H2–26H1) (source: wiki/sources/descriptions/wesmar__KvcForensic.md); Defender real-time / Tamper Protection control via kernel privilege-escalation CLIs such as [[windefctl]] (Win11 26H1; UAC/GUI bypass, stealth execution) (source: wiki/sources/descriptions/wesmar__WinDefCtl.md)

- **[[byovd]]:** signed vulnerable drivers → kernel R/W → unsigned load / blind AC; educational kernel-exploit guides such as [[windows-kernel-exploits]] (Cheat Vulnerable Driver lane); AV/EDR-evasion research such as [[ven0m-ransomware]] via `iMFForceDelete.sys` (IObit Malware Fighter) and [[av-edr-killer]] via `wsftprm.sys` IOCTL `0x22201C` (PID in first DWORD of 1036-byte buffer); AC-driver IRP abuse such as [[xign-poc-april-2026]] (`xhunter64.sys` / XIGNCODE3: `IRP_MJ_WRITE` → phys R/W, kernel address leak, process kill) (source: wiki/sources/descriptions/xct__windows-kernel-exploits.md) (source: wiki/sources/descriptions/xM0kht4r__VEN0m-Ransomware.md) (source: wiki/sources/descriptions/xM0kht4r__AV-EDR-Killer.md) (source: wiki/sources/descriptions/waryas__xign_poc_april_2026.md)
- **Trusted-process mappers:** extend a high-trust process (e.g. lsass) and map unsigned driver code in that context to skip normal load telemetry — research ref [[lsass-extend-mapper]] (source: wiki/sources/descriptions/zorftw__lsass-extend-mapper.md)
- **Pool / Segment Heap:** HeapKey-aware scanning for hidden modules and shellcode; post-map cleanup research such as [[revert-mapper]] (free mapping + strip pool tags / refs after unsigned-driver entry) (source: wiki/sources/descriptions/zorftw__revert-mapper.md)
- **ETW:** provider/event schema discovery (manifest + TraceLogging) via tools such as [[etw-explorer]]; ThreatIntel consumers such as [[tietwagent]] (Microsoft-Windows-Threat-Intelligence injection telemetry; krabsetw/Yara; ELAM/PPL) show how those providers feed AC/EDR detection without fragile userland hooks (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md) (source: wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md)
- **Host XDR / HIDS:** enterprise agent–manager platforms such as [[wazuh]] (intrusion detection, FIM, log correlation, Elasticsearch viz; Linux/Windows/macOS) illustrate SOC-style endpoint telemetry adjacent to AC/EDR research under README `[XDR]`. (source: wiki/sources/descriptions/wazuh__wazuh.md)
- **Hypervisor defense:** EPT-protected callback/ETW/AC pages; WHP research tracing; WHP user-mode x64 PE emulation such as [[winvisor]] (`Windows Emulator` lane); RING3 kernel-driver emulation such as [[kace]] (self context mapping or Unicorn; sandboxed AC/driver analysis); hacked-hypervisor stress/test tooling such as [[vt-debuuger]]; minimal VT-x Type-2 learning drivers such as [[hv]] (VMX root / VMCS / CPUID-MSR-CR exits); stealth Type-2 research such as [[ophion]] (EPT, CPUID cache, CR4.VMXE hide, TSC compensation, private host CR3); user-mode HV presence checks such as [[checkhv-um]] (CPUID leaf / RDTSC timing / VMCS artifacts / signatures, no driver) (source: wiki/sources/descriptions/x86matthew__WinVisor.md) (source: wiki/sources/descriptions/waryas__KACE.md) (source: wiki/sources/descriptions/zxd1994__vt-debuuger.md) (source: wiki/sources/descriptions/zer0condition__hv.md) (source: wiki/sources/descriptions/zer0condition__Ophion.md) (source: wiki/sources/descriptions/zer0condition__checkhv_um.md)
- **EFI:** pre-kernel mappers that skip normal driver-load telemetry — e.g. [[xigmapper]] (EFI manual map; payload must not be USB-hosted when studying early-load AC such as [[vanguard]]) (source: wiki/sources/descriptions/xtremegamer1__xigmapper.md); in-RAM `SYSTEM` hive patching at `ExitBootServices` such as [[efitool]] (SYSTEM shell before logon; no disk writes / no kernel driver; BitLocker PCR notes) (source: wiki/sources/descriptions/wesmar__EfiTool.md); Hackintosh OpenCore EFI packs such as [[x260-lenovo-opencore]] (ThinkPad X260) are a separate EFI lane for macOS-on-PC research hosts rather than cheat mapping. (source: wiki/sources/descriptions/x90skysn3k__x260-lenovo-opencore.md)
- **Legitimate-driver hijack / stealth I/O:** research such as [[boom]] hijacks `Beep.sys` and changes communication so Ring0↔usermode paths are less obvious to AC telemetry; composition-surface channels such as [[data-ptr-swap]] (`NtSetCompositionSurfaceAnalogExclusive`) sit in the same cheat / driver-communication lane; kernel DWM composition samples such as [[double-callback]] (C/C++; DWM in kernel / render-draw) ride the same composition stack from Ring0; named-event channels such as [[evcommunication]] (`Zw*Event` + `NtTokenManager` hook; `MmCopyVirtualMemory` R/W) avoid monitored IOCTL surfaces. (source: wiki/sources/descriptions/zoand__BOOM.md) (source: wiki/sources/descriptions/xPasters__.data-ptr-swap.md) (source: wiki/sources/descriptions/wbaby__DoubleCallBack.md) (source: wiki/sources/descriptions/weak1337__EvCommunication.md)
- **Keyboard IRP filter / keylog research:** educational samples such as [[keyboardkit]] intercept keyboard IRPs in a filter driver, exfiltrate via UDP usermode, and demonstrate ExplorerFrame DLL-hijack persistence (offensive + defensive IRP-hook analysis). (source: wiki/sources/descriptions/wesmar__KeyboardKit.md)
- **Kernel-mode sockets (WSK):** BSD-style wrappers such as [[ksocket]] expose TCP/UDP from ring 0 via Windows Sockets Kernel with no user-mode component—covert kernel network-channel research. (source: wiki/sources/descriptions/wbenny__KSOCKET.md)
- **System / hidden threads:** detectors such as [[system-thread-finder]] enumerate threads (`NtQuerySystemInformation`) and flag start addresses outside loaded driver images (BE-style manual-map thread heuristics). (source: wiki/sources/descriptions/weak1337__SystemThreadFinder.md) PoCs such as [[zero-thread-kernel]] evade that lane by running via existing contexts / timers instead of new system threads. (source: wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md)
- **Driver unit testing:** frameworks such as [[wdutf]] host Microsoft C++ unit tests in user space against kernel-driver code (AC / defensive driver harness lane). (source: wiki/sources/descriptions/wpdk__wdutf.md)


Version-specific PatchGuard research (e.g. [[pg1903]] on Win10 1903 via context-page NX manipulation) illustrates how PG bypass studies map to the Demo NX / Cheat PatchGuard README lane. (source: wiki/sources/descriptions/zzhouhe__PG1903.md) Educational demystification material such as [[demystifying-patchguard]] sits in the same lane for RE of [[patchguard]] internals. (source: wiki/sources/descriptions/zer0condition__Demystifying-PatchGuard.md)

## Related concepts

[[kernel-callbacks]] · [[byovd]] · [[windows-kernel-exploits]] · [[ven0m-ransomware]] · [[av-edr-killer]] · [[xign-poc-april-2026]] · [[kvc]] · [[kernel-research-kit]] · [[bootbypass]] · [[kvcforensic]] · [[windefctl]] · [[vaultguard]] · [[keyboardkit]] · [[ksocket]] · [[hvci]] · [[cet-research]] · [[windbg-scripts]] · [[symlink-callback]] · [[patchguard]] · [[pg1903]] · [[demystifying-patchguard]] · [[ntmemory]] · [[ntsleuth]] · [[instrumentation-callback-syscall-logger]] · [[function-collections]] · [[winvisor]] · [[kace]] · [[hv]] · [[ophion]] · [[checkhv-um]] · [[vt-debuuger]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[xigmapper]] · [[efitool]] · [[x260-lenovo-opencore]] · [[etw-explorer]] · [[tietwagent]] · [[wazuh]] · [[openark]] · [[systeminformer]] · [[system-thread-finder]] · [[boom]] · [[data-ptr-swap]] · [[double-callback]] · [[injdrv]] · [[kinject]] · [[zero-thread-kernel]] · [[wdutf]] · [[dma]] · [[overviews/anti-cheat]]




## README map

Cheat PatchGuard/DSE/Windows Kernel Explorer/Vulnerable Driver; Anti Cheat Detection:Attach|Hide|Vulnerable Driver|Hacked Hypervisor; `Windows Security Features` (~9: CET/shadow stack, TPM PCR attestation of virt/IOMMU/Secure Boot/VBS/HVCI/DSE/blocklist); `Some Tricks` (~112) `> Windows Ring0`; adjacent `Windows Emulator` (~7; WHP trap-driven guests + hybrid semi-emulated kernel-driver stacks for rootkit/AC analysis) and `WSL` (~4; WSL2 Linux-kernel research hosts). (source: wiki/sources/README-categories.md)
