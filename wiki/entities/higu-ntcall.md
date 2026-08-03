---
title: HIGU_ntcall
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/jnastarot__HIGU_ntcall.md
updated: 2026-08-03
confidence: medium
---

# HIGU_ntcall

Direct system-call invocation tooling from jnastarot, listed under **Some Tricks → Windows Ring3** with README tag `[Direct System Calls]`. Curated descriptions position it for low-level Windows, Linux, and mobile researchers studying Ring3 syscall paths rather than ntdll stub hooks. (source: wiki/sources/descriptions/jnastarot__HIGU_ntcall.md)

ENUM-backed functions are supported, but most crash during parameter conversion at call time—treat ENUM coverage as experimental when building research harnesses.

Complements SSN extraction via [[ntsleuth]], compile-time stub libraries such as [[syscalls-cpp]], and syscall-return telemetry such as [[instrumentation-callback-syscall-logger]]. Listed beside other jnastarot tooling such as [[anti-cheat]], [[ice9]], [[furikuri]], and [[shibari]].

## Links

- Repo: https://github.com/jnastarot/HIGU_ntcall

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[syscalls-cpp]] · [[ntsleuth]] · [[instrumentation-callback-syscall-logger]] · [[anti-cheat]] · [[ice9]]
