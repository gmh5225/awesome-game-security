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

Educational Windows **user-mode anti-cheat daemon** (HEEAAP; C++/Visual Studio) that launches a target game process suspended, attaches protection before resume, and polls for tampering. Reference implementation for **early-process attachment** and basic anti-debug enforcement on Windows — aimed at game developers and security researchers studying out-of-process monitoring before first instruction. (source: wiki/sources/descriptions/HEEAAP__Sentinel-Anti-Cheat.md)

## Detection

- Remote debuggers via `NtQueryInformationProcess` and related process queries
- Hardware breakpoints in debug registers (thread context inspection)
- Software breakpoints (`INT 3`) in executable code sections (`ReadProcessMemory`)

## Response

Configurable policies: log the event, suspend the target via `NtSuspendProcess`, or terminate outright. A TaskDialog splash screen covers startup while a polling monitor loop runs.

Complements educational usermode samples such as [[basic-anti-cheat]], [[mandragora]], and [[peregrine-anticheat]]; distinct from the multi-tier OSS skeleton [[sentinelac]]. Pairs with anti-debug study harnesses such as [[showstopper]] and [[anti-debug]] for validation workflows.

## Links

- Repo: https://github.com/HEEAAP/Sentinel-Anti-Cheat

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[basic-anti-cheat]] · [[mandragora]] · [[peregrine-anticheat]] · [[sentinelac]] · [[showstopper]] · [[anti-debug]]
