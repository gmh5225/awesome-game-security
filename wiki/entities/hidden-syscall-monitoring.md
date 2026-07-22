---
title: hidden_syscall_monitoring
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/ssnob__hidden_syscall_monitoring.md
updated: 2026-07-22
confidence: medium
---

# hidden_syscall_monitoring

C/C++ research sample that monitors hidden syscalls invoked from Call of Duty anticheat (hooking + memory analysis). Useful for RE of AC syscall telemetry and direct/hidden-syscall paths. (source: wiki/sources/descriptions/ssnob__hidden_syscall_monitoring.md)

Complements Ring3 Instrumentation Callback loggers such as [[instrumentation-callback-syscall-logger]] and Ricochet RE such as [[ricochet-deobfuscator]].

## Links

- Repo: https://github.com/ssnob/hidden_syscall_monitoring

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[instrumentation-callback-syscall-logger]] · [[ricochet-deobfuscator]] · [[ntsleuth]]
