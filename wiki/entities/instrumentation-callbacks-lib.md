---
title: InstrumentationCallbacks
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/1027565__InstrumentationCallbacks.md
updated: 2026-09-05
confidence: medium
---

# InstrumentationCallbacks

User-mode proof-of-concept library that extends undocumented Windows **Instrumentation Callback** (`ProcessInstrumentationCallback`) handling from Ring3. The callback fires on kernel-to-user transitions, enabling interception of system calls, APC delivery, exceptions, user-mode callbacks, and new-thread initialization events. Implemented in C++ and assembly with minimal dependencies centered on NTDLL; targets x86-64. Primary use cases are low-level Windows internals research, debugging experiments, and EDR-related telemetry studies. (source: wiki/sources/descriptions/1027565__InstrumentationCallbacks.md)

Broader transition coverage than syscall-only loggers such as [[instrumentation-callback-syscall-logger]]; complements TLS recursion-mitigation demos such as [[instrumentation-callbacks]] (Deputation) and return-hook PoCs such as [[hooking-via-instrumentation-callback]]. Pairs with defensive origin validators such as [[syscall-detect]] and ETW TI–adjacent samples such as [[etwti-syscall-hook]] when comparing Ring3 callback telemetry vs AC instrumentation expectations.

## Links

- Repo: https://github.com/1027565/InstrumentationCallbacks

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[instrumentation-callbacks]] · [[instrumentation-callback-syscall-logger]] · [[hooking-via-instrumentation-callback]] · [[syscall-detect]] · [[etwti-syscall-hook]] · [[nasty-alignment]] · [[beservice-intcallbacks]]
