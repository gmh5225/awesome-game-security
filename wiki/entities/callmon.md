---
title: CallMon
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/DownWithUp__CallMon.md
updated: 2026-08-26
confidence: medium
---

# CallMon

Windows system-call monitoring tool pairing a kernel driver with a user-mode GUI. Registers **PsAltSystemCallHandlers** to intercept syscalls from selected processes and forwards trap-frame and stack data through a named pipe for live inspection. Ships with a C implementation and an optional Rust driver variant for experimentation. Primary use cases are kernel telemetry, syscall behavior analysis, and anti-cheat research on process-level API monitoring. (source: wiki/sources/descriptions/DownWithUp__CallMon.md)

Complements user-mode EtwTi syscall loggers such as [[etw-syscall-monitor]] and Instrumentation Callback loggers such as [[instrumentation-callback-syscall-logger]] by hooking at the kernel **AltSystemCallHandlers** path instead of ETW or Ring3 callbacks. Defensive analysts can pair its per-process syscall traces with origin checks such as [[syscall-detect]] when studying custom syscall stubs vs expected `ntdll` paths.

## Links

- Repo: https://github.com/DownWithUp/CallMon

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-syscall-monitor]] · [[instrumentation-callback-syscall-logger]] · [[hidden-syscall-monitoring]] · [[kernelmon]] · [[syscall-detect]] · [[etwti-syscall-hook]]
