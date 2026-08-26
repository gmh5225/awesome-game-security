---
title: instrumentation_callbacks
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Deputation__instrumentation_callbacks.md
updated: 2026-08-26
confidence: medium
---

# instrumentation_callbacks

Windows Instrumentation Callback demonstration for process-level syscall and exception interception. The C++ and assembly codebase uses a TLS-based design to reduce callback recursion when the handler issues additional syscalls, and shows how to monitor syscall origins for both analysis and abuse-oriented scenarios. Primary audience is reverse engineers and anti-cheat researchers exploring undocumented Windows internals for telemetry and runtime control. (source: wiki/sources/descriptions/Deputation__instrumentation_callbacks.md)

Complements syscall-return loggers such as [[instrumentation-callback-syscall-logger]] and hooking PoCs such as [[hooking-via-instrumentation-callback]] by emphasizing TLS recursion control and combined syscall/exception interception. Pairs with kernel **PsAltSystemCallHandlers** monitors such as [[callmon]] and origin validators such as [[syscall-detect]] when comparing Ring3 callback telemetry vs kernel syscall paths.

## Links

- Repo: https://github.com/Deputation/instrumentation_callbacks

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[instrumentation-callback-syscall-logger]] · [[hooking-via-instrumentation-callback]] · [[syscall-detect]] · [[callmon]] · [[nasty-alignment]] · [[beservice-intcallbacks]]
