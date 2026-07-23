---
title: Hooking-via-InstrumentationCallback
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/secrary__Hooking-via-InstrumentationCallback.md
updated: 2026-07-23
confidence: medium
---

# Hooking-via-InstrumentationCallback

Windows C/C++ PoC that hooks syscall returns via Instrumentation Callback (`NtSetInformationProcess` / `ProcessInstrumentationCallback`). The callback runs on each kernel-to-user transition, so results can be inspected or modified without patching ntdll stubs. (source: wiki/sources/descriptions/secrary__Hooking-via-InstrumentationCallback.md)

Aimed at researchers studying alternative Ring3 hooking and AC/EDR evasion vs telemetry samples such as [[instrumentation-callback-syscall-logger]].

## Links

- Repo: https://github.com/secrary/Hooking-via-InstrumentationCallback

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[instrumentation-callback-syscall-logger]] · [[anticheat-poc]] · [[ntsleuth]]
