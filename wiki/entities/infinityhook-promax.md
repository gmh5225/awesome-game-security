---
title: InfinityHook Pro Max
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/ThomasonZhao__InfinityHookProMax.md
updated: 2026-08-20
confidence: medium
---

# InfinityHook Pro Max

Windows kernel hooking framework derived from earlier [[infinityhook]] variants. Implemented in C++ as a driver-oriented codebase with low-level hook management and instruction-disassembly components. Emphasizes broader compatibility and stability across multiple Windows versions, with testing in virtualized environments. Primary use cases include kernel security research, anti-cheat experimentation, and system monitoring. (source: wiki/sources/descriptions/ThomasonZhao__InfinityHookProMax.md)

Complements the original [[infinityhook]] C library, C++ wrappers such as [[etwhook-infinityhookclass]], and newer-build ports such as [[infinityhook-latest]] and [[infinityhook-pro]] in the ETW-backed syscall interception lane; integrates with HVCI-aware research stacks such as [[goodmans-kernel]] that embed InfinityHook trampolines.

## Links

- Repo: https://github.com/ThomasonZhao/InfinityHookProMax (README tag: ETW Hook WIN11)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-threat-intelligence]] · [[infinityhook]] · [[etwhook-infinityhookclass]] · [[infinityhook-latest]] · [[infinityhook-pro]] · [[patchguard]] · [[etw-syscall]] · [[etw-syscall-monitor]]
