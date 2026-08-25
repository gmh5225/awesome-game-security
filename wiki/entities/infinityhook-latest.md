---
title: InfinityHook Latest
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Oxygen1a1__InfinityHook_latest.md
updated: 2026-08-22
confidence: medium
---

# InfinityHook Latest

Windows kernel **ETW hooking** implementation that adapts InfinityHook-style syscall interception to newer system builds. Leverages ETW tracing paths and **HalPrivateDispatchTable** callbacks to redirect syscall handling without directly patching `Nt*` routines. Implemented in C/C++ as a Visual Studio kernel driver project with detailed reverse-engineering notes on PMC counter setup and trace configuration. Aimed at advanced anti-cheat bypass research and low-level Windows security experimentation. (source: wiki/sources/descriptions/Oxygen1a1__InfinityHook_latest.md)

Complements the original [[infinityhook]] C library, C++ wrappers such as [[etwhook-infinityhookclass]], and evolved frameworks such as [[infinityhook-promax]] and [[infinityhook-pro]] in the ETW-backed syscall interception lane.

## Links

- Repo: https://github.com/Oxygen1a1/InfinityHook_latest (README tag: ETW Hook WIN11)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-threat-intelligence]] · [[infinityhook]] · [[etwhook-infinityhookclass]] · [[infinityhook-promax]] · [[infinityhook-pro]] · [[patchguard]] · [[etw-syscall]] · [[etw-syscall-monitor]]
