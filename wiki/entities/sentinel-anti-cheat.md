---
title: Sentinel Anti-Cheat
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/HEEAAP__Sentinel-Anti-Cheat.md
  - wiki/sources/README-categories.md
updated: 2026-08-28
confidence: medium
---

# Sentinel Anti-Cheat

Educational Windows **user-mode anti-cheat daemon** (HEEAAP; C++/Visual Studio) that launches a target game process suspended, attaches protection before resume, and polls for tampering. Uses Win32 APIs such as `NtQueryInformationProcess`, `ReadProcessMemory`, and thread-context inspection to detect remote debuggers, hardware breakpoints in debug registers, and software breakpoints (`INT 3`) in executable code sections. Configurable response policies log events, suspend via `NtSuspendProcess`, or terminate outright; a TaskDialog splash screen covers startup while the monitor loop runs. Reference implementation for early-process attachment and basic anti-debug enforcement on Windows. (source: wiki/sources/descriptions/HEEAAP__Sentinel-Anti-Cheat.md)

Complements educational usermode samples such as [[basic-anti-cheat]], [[mandragora]], and [[peregrine-anticheat]]; distinct from the multi-tier OSS skeleton [[sentinelac]].

## Links

- Repo: https://github.com/HEEAAP/Sentinel-Anti-Cheat

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[basic-anti-cheat]] · [[mandragora]] · [[peregrine-anticheat]] · [[sentinelac]] · [[anti-debug]]
