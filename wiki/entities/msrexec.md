---
title: msrexec
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/backengineering__msrexec.md
updated: 2026-08-18
confidence: medium
---

# msrexec

C++ library that **escalates arbitrary MSR (Model Specific Register) write primitives to full kernel code execution** on Windows. Overwrites **`IA32_LSTAR`** to redirect the syscall-handler entry point, then runs controlled kernel shellcode from user mode. Integrates with [[vdm]] (Voyager Driver Manager) and **bluepill** backends to obtain the initial MSR-write capability. Aimed at low-level security researchers studying MSR-based kernel exploitation and privilege escalation. (source: wiki/sources/descriptions/backengineering__msrexec.md)

Sits in the MSR-exposure / [[byovd]] lane beside raw MSR IOCTL PoCs such as [[openhardwaremonitor-poc]] and syscall-path redirection research such as [[kaspersky-hook]] (`IA32_LSTAR` dispatch-table abuse).

## Links

- Repo: https://github.com/backengineering/msrexec

## Related

[[byovd]] · [[vdm]] · [[openhardwaremonitor-poc]] · [[kaspersky-hook]] · [[kdmapper]] · [[voyager]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
