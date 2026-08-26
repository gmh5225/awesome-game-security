---
title: NtDOOM
kind: entity
topics: [windows-kernel, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/NSG650__NtDOOM.md
updated: 2026-08-26
confidence: medium
---

# NtDOOM

Windows kernel port that runs **DOOM** entirely from a **kernel driver** context. C/C++ driver code adapts a [[pure-doom]] base with substantial NT internals work: **win32k-side syscall handling**, **thread context spoofing**, and **kernel-side graphics and input** to drive gameplay logic. Research demo for extreme **kernel GUI** and **syscall experimentation**—not practical game development. (source: wiki/sources/descriptions/NSG650__NtDOOM.md)

Extends the same win32k GUI-subsystem and hook-free Ring0 draw research lane as [[kernel-drawing]], [[krnl-gdi-render]], and [[callmewin32kdriver]]—but pushes further by running a full game loop from Ring0.

## Links

- Repo: https://github.com/NSG650/NtDOOM (README: Doom running in the NT kernel)

## Related

[[pure-doom]] · [[kernel-drawing]] · [[krnl-gdi-render]] · [[callmewin32kdriver]] · [[win32k-file-collection]] · [[driver-communication-list]] · [[ntuserinjectmouseinput-syscall]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
