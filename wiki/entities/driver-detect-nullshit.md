---
title: Driver-Detect-nullshit
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-Detect-nullshit.md
updated: 2026-08-13
confidence: medium
---

# Driver-Detect-nullshit

Compact Windows kernel detector for a common **manually mapped driver hook** pattern: exported routines in core modules replaced with simple absolute-jump stubs (`mov rax, imm64 ; jmp rax`) whose targets fall **outside the owning image**. (source: wiki/sources/descriptions/gmh5225__Driver-Detect-nullshit.md)

The archived README calls it a simple **Null driver detector**. The code walks export tables of modules such as `win32kfull.sys`, `win32kbase.sys`, `dxgkrnl.sys`, and `ntoskrnl.exe`, flagging crude export-hook trampolines often used to redirect syscall-related functions during driver mapping or covert communication setup. It is not a full integrity framework — it focuses on one inline-hook signature rather than broad code-hash or callback enumeration.

Mainly useful for anti-cheat engineers and defensive kernel researchers studying lightweight detection of export redirection in GUI-subsystem and core kernel images.

## Links

- Repo: https://github.com/gmh5225/Driver-Detect-nullshit

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[driver-driver-no-image]] · [[nulldriver-cheat]] · [[kernel-cheat-for-directx3d]] · [[driver-kdtour]] · [[windows-kernel-pagehook]] · [[hook-buster]] · [[hookhunter]] · [[driver-watchowl]] · [[research-rigor]]
