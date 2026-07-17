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
updated: 2026-07-17
confidence: high
---

# Windows Kernel

Kernel internals that matter for game protection and low-level research: object/process/image callbacks, APC/attach, driver load forensics (PiDDBCache, MmUnloadedDrivers, pool), DSE/[[patchguard]]/[[hvci]], and [[byovd]] paths. (source: wiki/sources/skills/windows-kernel.md)

## Key sub-areas

- **Structures:** EPROCESS/ETHREAD, MMVAD, DRIVER_OBJECT, IRP; SSDT/IDT; pool tables
- **[[kernel-callbacks]]:** process/thread/image notify, ObRegisterCallbacks, Cm/Flt
- **Trust features:** DSE, PatchGuard, VBS/HVCI, Secure Boot
- **[[byovd]]:** signed vulnerable drivers → kernel R/W → unsigned load / blind AC
- **Trusted-process mappers:** extend a high-trust process (e.g. lsass) and map unsigned driver code in that context to skip normal load telemetry — research ref [[lsass-extend-mapper]] (source: wiki/sources/descriptions/zorftw__lsass-extend-mapper.md)
- **Pool / Segment Heap:** HeapKey-aware scanning for hidden modules and shellcode; post-map cleanup research such as [[revert-mapper]] (free mapping + strip pool tags / refs after unsigned-driver entry) (source: wiki/sources/descriptions/zorftw__revert-mapper.md)
- **ETW:** provider/event schema discovery (manifest + TraceLogging) via tools such as [[etw-explorer]]; ThreatIntel and related providers are common AC/EDR telemetry surfaces (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md)
- **Hypervisor defense:** EPT-protected callback/ETW/AC pages; WHP research tracing; hacked-hypervisor stress/test tooling such as [[vt-debuuger]] (source: wiki/sources/descriptions/zxd1994__vt-debuuger.md)
- **EFI:** pre-kernel mappers that skip normal driver-load telemetry

Version-specific PatchGuard research (e.g. [[pg1903]] on Win10 1903 via context-page NX manipulation) illustrates how PG bypass studies map to the Demo NX / Cheat PatchGuard README lane. (source: wiki/sources/descriptions/zzhouhe__PG1903.md)

## Related concepts

[[kernel-callbacks]] · [[byovd]] · [[hvci]] · [[patchguard]] · [[pg1903]] · [[vt-debuuger]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[etw-explorer]] · [[dma]] · [[overviews/anti-cheat]]

## README map

Cheat PatchGuard/DSE/Windows Kernel Explorer/Vulnerable Driver; Anti Cheat detection:attach/hide/vulnerable driver/hacked hypervisor; `Windows Security Features` (CET/shadow stack, TPM/IOMMU/HVCI attestation samples); `Some Tricks > Windows Ring0`; adjacent `Windows Emulator` / WHP research. (source: wiki/sources/README-categories.md)
