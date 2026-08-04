---
title: syscall-detect
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/jackullrich__syscall-detect.md
updated: 2026-08-04
confidence: medium
---

# syscall-detect

Windows proof-of-concept for detecting direct and indirect syscall invocations from user mode. Uses an Instrumentation Callback or thread stack inspection to tell whether a syscall originated from `ntdll` (expected) or a custom stub (suspicious), flagging syscall hooking evasion. The C implementation demonstrates heuristics that anti-cheat and EDR products can adopt for user-mode integrity monitoring. (source: wiki/sources/descriptions/jackullrich__syscall-detect.md)

Complements syscall loggers such as [[instrumentation-callback-syscall-logger]] and [[etw-syscall-monitor]] by focusing on origin validation rather than full telemetry capture. Offensive direct-syscall helpers such as [[syscalls-cpp]] illustrate the evasion surface this PoC targets.

## Links

- Repo: https://github.com/jackullrich/syscall-detect

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[instrumentation-callback-syscall-logger]] · [[etw-syscall-monitor]] · [[hidden-syscall-monitoring]] · [[syscalls-cpp]] · [[hooking-via-instrumentation-callback]]
