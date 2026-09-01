---
title: Anti-AntiDebuggerDriver
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/AyinSama__Anti-AntiDebuggerDriver.md
updated: 2026-09-01
confidence: medium
---

# Anti-AntiDebuggerDriver

Tutorial **Windows kernel driver** in C++ focused on **neutralizing common anti-debugging checks** at Ring0. Hooks multiple native system-call paths related to **process, thread, handle, and system-information queries**, with low-level hook utilities and disassembly helpers to redirect anti-debug probes before they reach user-mode debuggers. Aimed at reverse-engineering education and protected-software analysis—not a production anti-cheat bypass product. (source: wiki/sources/descriptions/AyinSama__Anti-AntiDebuggerDriver.md)

Complements user-mode bypass tooling such as [[steam-anti-anti-debug]] and ScyllaHide-class hides such as [[scyllahide-for-ida9.0rc]]; pairs with defensive kernel anti-debug PoCs such as [[anti-kernel-debug-poc]] and SSDT-tamper hide drivers such as [[titanhide]] on the detection vs bypass axis.

## Links

- Repo: https://github.com/AyinSama/Anti-AntiDebuggerDriver (README tag: ETW Hook)

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[titanhide]] · [[scyllahide-for-ida9.0rc]] · [[steam-anti-anti-debug]] · [[anti-kernel-debug-poc]] · [[makin]] · [[showstopper]] · [[windows-kernel-debugging-guide]]
