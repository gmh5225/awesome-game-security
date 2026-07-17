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
updated: 2026-07-17
confidence: high
---



# Windows Kernel

Kernel internals that matter for game protection and low-level research: object/process/image callbacks, APC/attach, driver load forensics (PiDDBCache, MmUnloadedDrivers, pool), DSE/[[patchguard]]/[[hvci]], and [[byovd]] paths. (source: wiki/sources/skills/windows-kernel.md)

## Key sub-areas

- **Structures:** EPROCESS/ETHREAD, MMVAD, DRIVER_OBJECT, IRP; SSDT/IDT; pool tables
- **WinDbg automation:** JS WinDbg scripts such as [[windbg-scripts]] for kernel-level debug/modding workflows (Cheat → WinDbg Plugins). (source: wiki/sources/descriptions/yardenshafir__WinDbg_Scripts.md)
- **Cross-process kernel R/W:** MDL map + physical translate + CR3 page-table walk libraries such as [[ntmemory]] (research for kernel cheat memory paths / AC evasion). (source: wiki/sources/descriptions/zer0condition__NTMemory.md)
- **[[kernel-callbacks]]:** process/thread/image notify, ObRegisterCallbacks, Cm/Flt; defensive enumeration/inspection via anti-rootkit GUIs such as [[openark]] (SSDT/shadow SSDT, drivers, objects) (source: wiki/sources/descriptions/yyl-20020115__OpenArk.md)
- **Trust features:** DSE, PatchGuard, VBS/HVCI, Secure Boot; CET/shadow-stack research such as [[cet-research]] under `Windows Security Features` (source: wiki/sources/descriptions/yardenshafir__cet-research.md)
- **[[byovd]]:** signed vulnerable drivers → kernel R/W → unsigned load / blind AC
- **Trusted-process mappers:** extend a high-trust process (e.g. lsass) and map unsigned driver code in that context to skip normal load telemetry — research ref [[lsass-extend-mapper]] (source: wiki/sources/descriptions/zorftw__lsass-extend-mapper.md)
- **Pool / Segment Heap:** HeapKey-aware scanning for hidden modules and shellcode; post-map cleanup research such as [[revert-mapper]] (free mapping + strip pool tags / refs after unsigned-driver entry) (source: wiki/sources/descriptions/zorftw__revert-mapper.md)
- **ETW:** provider/event schema discovery (manifest + TraceLogging) via tools such as [[etw-explorer]]; ThreatIntel and related providers are common AC/EDR telemetry surfaces (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md)
- **Hypervisor defense:** EPT-protected callback/ETW/AC pages; WHP research tracing; hacked-hypervisor stress/test tooling such as [[vt-debuuger]]; minimal VT-x Type-2 learning drivers such as [[hv]] (VMX root / VMCS / CPUID-MSR-CR exits); stealth Type-2 research such as [[ophion]] (EPT, CPUID cache, CR4.VMXE hide, TSC compensation, private host CR3); user-mode HV presence checks such as [[checkhv-um]] (CPUID leaf / RDTSC timing / VMCS artifacts / signatures, no driver) (source: wiki/sources/descriptions/zxd1994__vt-debuuger.md) (source: wiki/sources/descriptions/zer0condition__hv.md) (source: wiki/sources/descriptions/zer0condition__Ophion.md) (source: wiki/sources/descriptions/zer0condition__checkhv_um.md)
- **EFI:** pre-kernel mappers that skip normal driver-load telemetry
- **Legitimate-driver hijack / stealth I/O:** research such as [[boom]] hijacks `Beep.sys` and changes communication so Ring0↔usermode paths are less obvious to AC telemetry. (source: wiki/sources/descriptions/zoand__BOOM.md)
- **Threadless kernel execution:** PoCs such as [[zero-thread-kernel]] run code via existing thread contexts / timer callbacks instead of creating visible system threads (evasion research vs AC thread enumeration of manual maps). (source: wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md)


Version-specific PatchGuard research (e.g. [[pg1903]] on Win10 1903 via context-page NX manipulation) illustrates how PG bypass studies map to the Demo NX / Cheat PatchGuard README lane. (source: wiki/sources/descriptions/zzhouhe__PG1903.md) Educational demystification material such as [[demystifying-patchguard]] sits in the same lane for RE of [[patchguard]] internals. (source: wiki/sources/descriptions/zer0condition__Demystifying-PatchGuard.md)

## Related concepts

[[kernel-callbacks]] · [[byovd]] · [[hvci]] · [[cet-research]] · [[windbg-scripts]] · [[patchguard]] · [[pg1903]] · [[demystifying-patchguard]] · [[ntmemory]] · [[hv]] · [[ophion]] · [[checkhv-um]] · [[vt-debuuger]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[etw-explorer]] · [[openark]] · [[boom]] · [[zero-thread-kernel]] · [[dma]] · [[overviews/anti-cheat]]



## README map

Cheat PatchGuard/DSE/Windows Kernel Explorer/Vulnerable Driver; Anti Cheat Detection:Attach|Hide|Vulnerable Driver|Hacked Hypervisor; `Windows Security Features` (~9: CET/shadow stack, TPM PCR attestation of virt/IOMMU/Secure Boot/VBS/HVCI/DSE/blocklist); `Some Tricks` (~112) `> Windows Ring0`; adjacent `Windows Emulator` (~7) / WHP trap-driven guest research. (source: wiki/sources/README-categories.md)
