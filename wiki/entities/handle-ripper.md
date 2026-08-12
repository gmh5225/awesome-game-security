---
title: Handle-Ripper
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Handle-Ripper.md
updated: 2026-08-12
confidence: medium
---

# Handle-Ripper

Small **user-mode handle-hijacking** proof of concept (gmh5225) that demonstrates stealing and reusing a target handle from another process. The sample calls `NtQuerySystemInformation` with `SystemHandleInformation`, scans the returned handle table for a chosen object pointer, opens the owning process with `PROCESS_DUP_HANDLE`, and uses `DuplicateHandle` to copy that handle into the current process. The README emphasizes the attack model and `DuplicateHandle` parameters, so the code reads as a minimal teaching PoC for stolen-handle reuse rather than a general-purpose framework. (source: wiki/sources/descriptions/gmh5225__Handle-Ripper.md)

Useful for Windows security researchers studying **handle-table enumeration**, **cross-process handle duplication**, and the mechanics behind handle hijacking — a building block for higher-level techniques such as [[lsass-dump-that-lsass]] handle theft and [[dsark64]] handle-donor abuse.

README category: DuplicateHandle.

## Links

- Repo: https://github.com/gmh5225/Handle-Ripper

## Related

[[lsass-dump-that-lsass]] · [[libelevate]] · [[van1338]] · [[dsark64]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
