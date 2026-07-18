---
title: NTSleuth
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/xaitax__NTSleuth.md
updated: 2026-07-18
confidence: medium
---

# NTSleuth

Windows syscall number extractor: parses `ntdll` / `win32u` with PDB symbol resolution and instruction disassembly to dump complete syscall tables, emitting JSON and C header outputs for security research. (source: wiki/sources/descriptions/xaitax__NTSleuth.md)

Useful when building or auditing direct-syscall stubs, tracking SSN drift across Windows builds, or mapping usermode stubs before deeper SSDT / kernel-path analysis—not a runtime hooker.

## Links

- Repo: https://github.com/xaitax/NTSleuth

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[totalpe2]] · [[openark]]
