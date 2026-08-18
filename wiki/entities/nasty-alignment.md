---
title: NastyAlignment
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/asamy__NastyAlignment.md
updated: 2026-08-18
confidence: medium
---

# NastyAlignment

Compact Windows proof-of-concept demonstrating alignment-check edge cases with process Instrumentation Callbacks. Combines C and x64 assembly to set AC-related flags, trigger unaligned memory access, and observe `STATUS_DATATYPE_MISALIGNMENT` exceptions via `NtSetInformationProcess` / `ProcessInstrumentationCallback` and custom exception handling—highlighting failure modes in callback code. (source: wiki/sources/descriptions/asamy__NastyAlignment.md)

Useful for low-level kernel and runtime instrumentation research; complements syscall-return Instrumentation Callback samples such as [[hooking-via-instrumentation-callback]] and [[instrumentation-callback-syscall-logger]].

## Links

- Repo: https://github.com/asamy/NastyAlignment

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hooking-via-instrumentation-callback]] · [[instrumentation-callback-syscall-logger]] · [[syscall-detect]] · [[anticheat-poc]]
