---
title: NoImportz
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Th3Spl__NoImportz.md
  - wiki/sources/README-categories.md
updated: 2026-08-29
confidence: medium
---

# NoImportz

C++17 **header-only Windows kernel library** (Th3Spl) that resolves system APIs at runtime without leaving direct PE import table entries. Aimed at manually mapped or import-free kernel code that needs to reduce visibility to anti-cheat and security software inspecting driver IATs. Listed under Anti Cheat → Lazy Importer beside [[lazy-importer]], [[kli]], [[zeroimport]], and [[rs-ldr]]. (source: wiki/sources/descriptions/Th3Spl__NoImportz.md)

## Mechanism

- **Kernel base locate:** scan backward from the **LSTAR MSR** to find `ntoskrnl.exe` in memory.
- **Module walk:** traverse `PsLoadedModuleList` to reach target kernel modules (not only ntoskrnl).
- **Export resolve:** parse PE headers and export directories similar to `MmGetSystemRoutineAddress`.
- **Call surface:** template-based variadic interface with optional hash-map caching for repeated resolves.
- **Import hygiene:** custom memory routines avoid compiler-generated imports that would repopulate the IAT.
- **Sample:** included **KMDF driver** demonstrates resolving APIs from `ntoskrnl` and other modules such as `ndis.sys`.

Complements compile-time kernel lazy-import headers ([[kli]], [[kli-ex]]) and manual-map injectors such as [[kernelmode-manual-mapping-through-iat]] — NoImportz targets runtime resolution when the driver image must ship with no static import table footprint. Same author lane as UEFI/firmware tools [[perfectsmbios]] and [[simpleuefi]].

Defensive analysts should treat sparse or empty driver IATs combined with LSTAR-relative ntoskrnl discovery and `PsLoadedModuleList` export walks as potential zero-IAT lazy-import usage.

## Links

- Repo: https://github.com/Th3Spl/NoImportz

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[lazy-importer]] · [[kli]] · [[kli-ex]] · [[zeroimport]] · [[kernelmode-manual-mapping-through-iat]] · [[perfectsmbios]]
