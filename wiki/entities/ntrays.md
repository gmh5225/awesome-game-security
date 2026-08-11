---
title: NtRays
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__NtRays.md
updated: 2026-08-11
confidence: medium
---

# NtRays

IDA Pro plugin that enhances Hex-Rays decompiler output for Windows kernel code by resolving NT kernel type definitions and structure references. Annotates **NTSTATUS** codes, **IOCTL** definitions, kernel object types, and **EPROCESS** / **ETHREAD** field accesses with proper names and types. Aimed at reverse engineers analyzing Windows kernel drivers and **ntoskrnl** in IDA Pro. (source: wiki/sources/descriptions/gmh5225__NtRays.md)

Hex-Rays decompiler enrichment only—not a debugger, symbol server, or automated structure-recovery engine. Complements [[ida-kmdf]] (WDF driver annotation), [[ida-bitfields]] (bitfield flag visualization), [[symless]] (automated type recovery), and [[ntoskrnlwalker]] / [[ntkernelwalkerlib]] (offset and symbol resolution outside IDA).

## Links

- Repo: https://github.com/gmh5225/NtRays

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ida-kmdf]] · [[ida-bitfields]] · [[ntoskrnlwalker]] · [[ntkernelwalkerlib]] · [[symless]]
