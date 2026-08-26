---
title: InfinityHookPro Main
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/DearXiaoGui__InfinityHookPro-main.md
updated: 2026-08-26
confidence: medium
---

# InfinityHookPro Main

Windows kernel hooking project derived from **InfinityHook** with added support for **physical machines** (not VM-only). Targets Windows 7 through Windows 11 with low-level driver code for syscall interception via **ETW** or **CKCL**-related paths, **SSDT** context handling, and kernel pattern-scanning helpers. Implemented in C/C++ with callback-based interception for monitoring or modifying system-call dispatch flow. Primary audience: kernel security researchers studying anti-cheat telemetry, syscall monitoring, and hook detection or bypass behavior. (source: wiki/sources/descriptions/DearXiaoGui__InfinityHookPro-main.md)

Sits in the same ETW-backed syscall interception lineage as [[infinityhook]], [[infinityhook-pro]], [[infinityhook-promax]], and [[infinityhook-latest]]; complements passive EtwTi loggers such as [[etw-syscall-monitor]] and Instrumentation Callback research such as [[instrumentation-callbacks]].

## Links

- Repo: https://github.com/DearXiaoGui/InfinityHookPro-main (README tag: ETW Hook WIN11)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-threat-intelligence]] · [[infinityhook]] · [[infinityhook-pro]] · [[infinityhook-promax]] · [[infinityhook-latest]] · [[etwhook-infinityhookclass]] · [[patchguard]] · [[etw-syscall]] · [[etw-syscall-monitor]] · [[syscall-detect]]
