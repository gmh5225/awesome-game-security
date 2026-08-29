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

C++17 **header-only Windows kernel library** (Th3Spl) that resolves system APIs at runtime without leaving direct PE import table entries. Locates `ntoskrnl.exe` by scanning backward from the LSTAR MSR, walks `PsLoadedModuleList`, and resolves exports through PE header parsing similar to `MmGetSystemRoutineAddress`. Template-based calls with optional hash-map caching support variadic functions across loaded kernel modules; custom memory routines avoid compiler-generated imports. Sample KMDF driver demonstrates usage against `ntoskrnl` and modules such as `ndis.sys`. (source: wiki/sources/descriptions/Th3Spl__NoImportz.md)

Aimed at manually mapped or import-free kernel code that needs to reduce visibility to anti-cheat and security software inspecting driver IATs. Listed under Anti Cheat → Lazy Importer beside `lazy_importer`, `kli`, `zeroimport`, and `rs-ldr`.

## Links

- Repo: https://github.com/Th3Spl/NoImportz

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[lazy-importer]] · [[zeroimport]] · [[kli]]
