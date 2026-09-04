---
title: arm64-silent-syscall-hook
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/3intermute__arm64_silent_syscall_hook.md
updated: 2026-09-04
confidence: medium
---

# arm64-silent-syscall-hook

**Silent ARM64 Linux syscall hooking** demonstration (3intermute) that patches the kernel **SVC / exception-handler path** instead of modifying **`sys_call_table`** entries directly. Selected syscall numbers are redirected through alternate logic to reduce common table-tamper detection indicators. Implemented in low-level C with **manual function splicing** and **trampoline-style patching** around exception-handler code paths. Intended for kernel security researchers studying **stealth rootkit** techniques and improving **syscall hook detection** methods on ARM64 Linux — including Android GKI kernels that share the same AArch64 syscall dispatch surface. (source: wiki/sources/descriptions/3intermute__arm64_silent_syscall_hook.md)

README category: ARM64 Patching exception handler.

Complements inline-hook scaffolds such as [[android-kernel-inline-hook-framework]] and [[kernel-hook-framework]], ftrace-based syscall interceptors such as [[kasumi]], and defensive integrity monitors such as [[ksentinel]] and [[rootkit]].

## Links

- Repo: https://github.com/3intermute/arm64_silent_syscall_hook (ARM64 Patching exception handler)

## Related

[[android-kernel-inline-hook-framework]] · [[kernel-hook-framework]] · [[kasumi]] · [[android-kernel-hacking-toolkit]] · [[ksentinel]] · [[rootkit]] · [[venom]] · [[modreveal]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
