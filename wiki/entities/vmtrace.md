---
title: vmtrace
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/momo5502__vmtrace.md
updated: 2026-07-29
confidence: medium
---

# vmtrace

C++ library on the Windows Hypervisor Platform (WHP) API for **trap-driven guest execution**: host-backed guest physical memory, page-level R/W/X access traps, CPUID and syscall interception, and VM-exit handlers for single-step tracing. Uses **asmjit** for runtime code generation and exposes a clean interface to map guest memory, set permissions, and resume guest execution after each exit. (source: wiki/sources/descriptions/momo5502__vmtrace.md)

Lower-level WHP building block for RE/DBI workflows — composable with disassemblers and emulators — rather than a full PE loader like [[winvisor]]. Sits in the cheat / dynamic binary instrumentation lane next to trap-and-emulate and WHP-assisted tracing patterns in [[dynamic-binary-instrumentation]].

## Links

- Repo: https://github.com/momo5502/vmtrace

## Related

[[winvisor]] · [[dynamic-binary-instrumentation]] · [[cpp-veh-dbi]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
