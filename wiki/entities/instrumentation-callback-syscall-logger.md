---
title: InstrumentationCallbackSyscallLogger
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/x86matthew__InstrumentationCallbackSyscallLogger.md
updated: 2026-07-18
confidence: medium
---

# InstrumentationCallbackSyscallLogger

Windows Instrumentation Callback research sample: the callback runs on every return from a kernel syscall, so user-mode code can inspect each call before normal execution resumes. (source: wiki/sources/descriptions/x86matthew__InstrumentationCallbackSyscallLogger.md)

Aimed at anti-cheat engineers and defensive researchers studying Ring3 / instrumentation-callback telemetry (complementary to static SSN extractors such as [[ntsleuth]]).

## Links

- Repo: https://github.com/x86matthew/InstrumentationCallbackSyscallLogger

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[ntsleuth]] · [[kernel-callbacks]]
