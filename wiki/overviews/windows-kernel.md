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
  - wiki/sources/descriptions/zer0condition__checkhv_um.md
  - wiki/sources/descriptions/yyl-20020115__OpenArk.md
  - wiki/sources/descriptions/yardenshafir__cet-research.md
  - wiki/sources/descriptions/yardenshafir__WinDbg_Scripts.md
  - wiki/sources/descriptions/yardenshafir__SymlinkCallback.md
  - wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md
  - wiki/sources/descriptions/xtremegamer1__xigmapper.md
  - wiki/sources/descriptions/xct__windows-kernel-exploits.md
  - wiki/sources/descriptions/xaitax__NTSleuth.md
updated: 2026-07-18
confidence: high
---



# Windows Kernel

Kernel internals that matter for game protection and low-level research: object/process/image callbacks, APC/attach, driver load forensics (PiDDBCache, MmUnloadedDrivers, pool), DSE/[[patchguard]]/[[hvci]], and [[byovd]] paths. (source: wiki/sources/skills/windows-kernel.md)

## Key sub-areas

- **Structures:** EPROCESS/ETHREAD, MMVAD, DRIVER_OBJECT, IRP; SSDT/IDT; pool tables
- **Syscall tables:** extract `ntdll` / `win32u` SSNs via PDB + disassembly tools such as [[ntsleuth]] (JSON / C header dumps for direct-syscall research). (source: wiki/sources/descriptions/xaitax__NTSleuth.md)
- **WinDbg automation:** JS WinDbg scripts such as [[windbg-scripts]] for kernel-level debug/modding workflows (Cheat → WinDbg Plugins). (source: wiki/sources/descriptions/yardenshafir__WinDbg_Scripts.md)
- **Cross-process kernel R/W:** MDL map + physical translate + CR3 page-table walk libraries such as [[ntmemory]] (research for kernel cheat memory paths / AC evasion). (source: wiki/sources/descriptions/zer0condition__NTMemory.md)
- **[[kernel-callbacks]]:** process/thread/image notify, ObRegisterCallbacks, Cm/Flt; defensive enumeration/inspection via anti-rootkit GUIs such as [[openark]] (SSDT/shadow SSDT, drivers, objects); object-symlink access callbacks such as [[symlink-callback]] (LinkTarget → callback) (source: wiki/sources/descriptions/yyl-20020115__OpenArk.md) (source: wiki/sources/descriptions/yardenshafir__SymlinkCallback.md)
- **Trust features:** DSE, PatchGuard, VBS/HVCI, Secure Boot; CET/shadow-stack research such as [[cet-research]] under `Windows Security Features` (source: wiki/sources/descriptions/yardenshafir__cet-research.md)
- **[[byovd]]:** signed vulnerable drivers → kernel R/W → unsigned load / blind AC; educational kernel-exploit guides such as [[windows-kernel-exploits]] (Cheat Vulnerable Driver lane) (source: wiki/sources/descriptions/xct__windows-kernel-exploits.md)
- **Trusted-process mappers:** extend a high-trust process (e.g. lsass) and map unsigned driver code in that context to skip normal load telemetry — research ref [[lsass-extend-mapper]] (source: wiki/sources/descriptions/zorftw__lsass-extend-mapper.md)
- **Pool / Segment Heap:** HeapKey-aware scanning for hidden modules and shellcode; post-map cleanup research such as [[revert-mapper]] (free mapping + strip pool tags / refs after unsigned-driver entry) (source: wiki/sources/descriptions/zorftw__revert-mapper.md)
- **ETW:** provider/event schema discovery (manifest + TraceLogging) via tools such as [[etw-explorer]]; ThreatIntel consumers such as [[tietwagent]] (Microsoft-Windows-Threat-Intelligence injection telemetry; krabsetw/Yara; ELAM/PPL) show how those providers feed AC/EDR detection without fragile userland hooks (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md) (source: wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md)
- **Hypervisor defense:** EPT-protected callback/ETW/AC pages; WHP research tracing; hacked-hypervisor stress/test tooling such as [[vt-debuuger]]; minimal VT-x Type-2 learning drivers such as [[hv]] (VMX root / VMCS / CPUID-MSR-CR exits); stealth Type-2 research such as [[ophion]] (EPT, CPUID cache, CR4.VMXE hide, TSC compensation, private host CR3); user-mode HV presence checks such as [[checkhv-um]] (CPUID leaf / RDTSC timing / VMCS artifacts / signatures, no driver) (source: wiki/sources/descriptions/zxd1994__vt-debuuger.md) (source: wiki/sources/descriptions/zer0condition__hv.md) (source: wiki/sources/descriptions/zer0condition__Ophion.md) (source: wiki/sources/descriptions/zer0condition__checkhv_um.md)
- **EFI:** pre-kernel mappers that skip normal driver-load telemetry — e.g. [[xigmapper]] (EFI manual map; payload must not be USB-hosted when studying early-load AC such as [[vanguard]]) (source: wiki/sources/descriptions/xtremegamer1__xigmapper.md)
- **Legitimate-driver hijack / stealth I/O:** research such as [[boom]] hijacks `Beep.sys` and changes communication so Ring0↔usermode paths are less obvious to AC telemetry. (source: wiki/sources/descriptions/zoand__BOOM.md)
- **Threadless kernel execution:** PoCs such as [[zero-thread-kernel]] run code via existing thread contexts / timer callbacks instead of creating visible system threads (evasion research vs AC thread enumeration of manual maps). (source: wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md)


Version-specific PatchGuard research (e.g. [[pg1903]] on Win10 1903 via context-page NX manipulation) illustrates how PG bypass studies map to the Demo NX / Cheat PatchGuard README lane. (source: wiki/sources/descriptions/zzhouhe__PG1903.md) Educational demystification material such as [[demystifying-patchguard]] sits in the same lane for RE of [[patchguard]] internals. (source: wiki/sources/descriptions/zer0condition__Demystifying-PatchGuard.md)

## Related concepts

[[kernel-callbacks]] · [[byovd]] · [[windows-kernel-exploits]] · [[hvci]] · [[cet-research]] · [[windbg-scripts]] · [[symlink-callback]] · [[patchguard]] · [[pg1903]] · [[demystifying-patchguard]] · [[ntmemory]] · [[ntsleuth]] · [[hv]] · [[ophion]] · [[checkhv-um]] · [[vt-debuuger]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[xigmapper]] · [[etw-explorer]] · [[tietwagent]] · [[openark]] · [[boom]] · [[zero-thread-kernel]] · [[dma]] · [[overviews/anti-cheat]]



## README map

Cheat PatchGuard/DSE/Windows Kernel Explorer/Vulnerable Driver; Anti Cheat Detection:Attach|Hide|Vulnerable Driver|Hacked Hypervisor; `Windows Security Features` (~9: CET/shadow stack, TPM PCR attestation of virt/IOMMU/Secure Boot/VBS/HVCI/DSE/blocklist); `Some Tricks` (~112) `> Windows Ring0`; adjacent `Windows Emulator` (~7; WHP trap-driven guests + hybrid semi-emulated kernel-driver stacks for rootkit/AC analysis). (source: wiki/sources/README-categories.md)
