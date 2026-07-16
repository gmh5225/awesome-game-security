---
title: Windows Kernel
kind: overview
topics: [windows-kernel]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/README-categories.md
updated: 2026-07-16
confidence: high
---

# Windows Kernel

Kernel internals that matter for game protection and low-level research: object/process/image callbacks, APC/attach, driver load forensics (PiDDBCache, MmUnloadedDrivers, pool), DSE/[[patchguard]]/[[hvci]], and [[byovd]] paths. (source: wiki/sources/skills/windows-kernel.md)

## Key sub-areas

- **Structures:** EPROCESS/ETHREAD, MMVAD, DRIVER_OBJECT, IRP; SSDT/IDT; pool tables
- **[[kernel-callbacks]]:** process/thread/image notify, ObRegisterCallbacks, Cm/Flt
- **Trust features:** DSE, PatchGuard, VBS/HVCI, Secure Boot
- **[[byovd]]:** signed vulnerable drivers → kernel R/W → unsigned load / blind AC
- **Pool / Segment Heap:** HeapKey-aware scanning for hidden modules and shellcode
- **Hypervisor defense:** EPT-protected callback/ETW/AC pages; WHP research tracing
- **EFI:** pre-kernel mappers that skip normal driver-load telemetry

## Related concepts

[[kernel-callbacks]] · [[byovd]] · [[hvci]] · [[patchguard]] · [[dma]] · [[overviews/anti-cheat]]

## README map

Cheat PatchGuard/DSE/Windows Kernel Explorer/Vulnerable Driver; Anti Cheat Ring0 callbacks and detection:attach/hide/vulnerable driver; `Windows Security Features`; `Some Tricks > Windows Ring0`. (source: wiki/sources/README-categories.md)
