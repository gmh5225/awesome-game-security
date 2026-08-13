---
title: KasperskyHook
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__KasperskyHook.md
updated: 2026-08-12
confidence: medium
---

# KasperskyHook

System-call hooking framework (gmh5225; README `[Kaspersky]`) that **subverts the syscall path via Kaspersky's hypervisor driver `klhk.sys`**. It loads `klhk.sys` plus a custom companion driver, then exploits Kaspersky's **`IA32_LSTAR` modification** — redirecting system calls through Kaspersky's own dispatch table — to intercept and replace the kernel syscall handler. Useful for studying **third-party AV hypervisor syscall redirection**, `MSR_LSTAR` abuse, and covert kernel instrumentation that piggybacks on an already-installed security product rather than deploying a standalone hook driver. (source: wiki/sources/descriptions/gmh5225__KasperskyHook.md)

## Links

- Repo: https://github.com/gmh5225/KasperskyHook

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[evil-kaspersky]] · [[etwti-syscall-hook]] · [[syscall-detect]] · [[hypervisor-detection]] · [[kli]]
