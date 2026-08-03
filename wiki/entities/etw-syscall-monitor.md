---
title: Etw-SyscallMonitor
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/jdu2600__Etw-SyscallMonitor.md
updated: 2026-08-03
confidence: medium
---

# Etw-SyscallMonitor

Windows user-mode syscall monitoring tool that consumes **ETW Threat Intelligence** (EtwTi) events to log system-call activity in real time. Captures syscall numbers, parameters, calling process/thread context, and stack traces through the EtwTi provider — without kernel hooking or driver installation. The C implementation demonstrates syscall-based behavioral detection for security researchers and anti-cheat developers. (source: wiki/sources/descriptions/jdu2600__Etw-SyscallMonitor.md)

Complements Instrumentation Callback syscall loggers such as [[instrumentation-callback-syscall-logger]] and hook-based samples such as [[etwti-syscall-hook]] by using the EtwTi consumer path instead of patching ntdll or registering process instrumentation callbacks. Pairs with registration-tamper monitors such as [[etwti-fluctuation-monitor]] from the same author.

## Links

- Repo: https://github.com/jdu2600/Etw-SyscallMonitor

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-threat-intelligence]] · [[etwti-fluctuation-monitor]] · [[instrumentation-callback-syscall-logger]] · [[etwti-syscall-hook]] · [[hidden-syscall-monitoring]] · [[tietwagent]]
