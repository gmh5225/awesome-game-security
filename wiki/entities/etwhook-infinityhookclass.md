---
title: ETWHOOK-InfinityHookClass
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__ETWHOOK-InfinityHookClass.md
updated: 2026-08-13
confidence: medium
---

# ETWHOOK-InfinityHookClass

C++ wrapper class around the **InfinityHook** ETW-based system-call hooking technique. Exposes a clean object-oriented interface for intercepting Windows syscalls by manipulating ETW tracing infrastructure—without patching the SSDT. Aimed at kernel researchers studying ETW-backed syscall hook surfaces adjacent to anti-cheat and EDR telemetry. (source: wiki/sources/descriptions/gmh5225__ETWHOOK-InfinityHookClass.md)

Complements ETW syscall modding samples such as [[etw-syscall]], passive EtwTi loggers such as [[etw-syscall-monitor]], and Instrumentation Callback hook PoCs such as [[etwti-syscall-hook]] by packaging InfinityHook as reusable C++ rather than raw technique code.

## Links

- Repo: https://github.com/gmh5225/ETWHOOK-InfinityHookClass

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-threat-intelligence]] · [[etw-syscall]] · [[etw-syscall-monitor]] · [[etwti-syscall-hook]] · [[instrumentation-callback-syscall-logger]] · [[hidden-syscall-monitoring]] · [[syscall-detect]]
