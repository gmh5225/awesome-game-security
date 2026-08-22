---
title: InfinityHook
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/everdox__InfinityHook.md
updated: 2026-08-15
confidence: medium
---

# InfinityHook

Original Windows kernel hooking library in C that intercepts system calls by manipulating **ETW (Event Tracing for Windows)** internal function pointers. Patches the ETW syscall trace callback pointer inside the kernel to redirect control flow, enabling transparent syscall interception without modifying the SSDT or inline patching `ntoskrnl`. The technique survives PatchGuard checks because it operates through a legitimate ETW code path. Aimed at kernel researchers studying stealthy syscall hooking, anti-cheat bypasses, and PatchGuard-compatible kernel instrumentation. (source: wiki/sources/descriptions/everdox__InfinityHook.md)

Downstream C++ wrappers such as [[etwhook-infinityhookclass]] and evolved frameworks such as [[infinityhook-promax]] and [[infinityhook-latest]] package the same ETW-backed hook surface for reuse; complements ETW syscall modding samples such as [[etw-syscall]], passive EtwTi loggers such as [[etw-syscall-monitor]], and Instrumentation Callback hook PoCs such as [[etwti-syscall-hook]].

## Links

- Repo: https://github.com/everdox/InfinityHook (README tag: ETW Hook)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[etw-threat-intelligence]] · [[patchguard]] · [[etwhook-infinityhookclass]] · [[infinityhook-promax]] · [[infinityhook-latest]] · [[etw-syscall]] · [[etw-syscall-monitor]] · [[etwti-syscall-hook]] · [[ermsb-meme]]
