---
title: IDA KMDF
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/thalium__ida_kmdf.md
updated: 2026-07-20
confidence: medium
---

# IDA KMDF

IDA Pro Python plugin for reversing Windows Kernel-Mode Driver Framework (KMDF / WDF) drivers. Identifies and annotates KMDF framework structures, callback registrations, I/O queue configurations, and device-initialization patterns; applies KMDF type definitions and names framework function calls so WDF driver binaries are easier to navigate in IDA. Aimed at reverse engineers analyzing KMDF-based Windows kernel drivers (including AC / game-protection driver RE). (source: wiki/sources/descriptions/thalium__ida_kmdf.md)

Not a debugger or unpacker—scoped to IDA-side KMDF structure and call annotation.

## Links

- Repo: https://github.com/thalium/ida_kmdf

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[symless]] · [[kace]] · [[wdutf]] · [[openark]]
