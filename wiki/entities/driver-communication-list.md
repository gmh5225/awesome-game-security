---
title: Driver-Communication-List
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-Communication-List.md
updated: 2026-08-13
confidence: medium
---

# Driver-Communication-List

Compact reference list of **user-mode to kernel-mode call paths** for studying how Windows graphics and UI entry points flow into lower-level kernel components. The archived README documents concrete chains such as `win32u.dll` resolving through `win32k.sys` and `win32base.sys` before reaching targets in `dxgkrnl.sys` — a mapping notebook rather than a traditional code project. (source: wiki/sources/descriptions/gmh5225__Driver-Communication-List.md)

The value is in the **call-chain examples themselves**: quick breadcrumbs for tracing communication paths that can later be followed in a debugger or disassembler. Mainly useful for Windows kernel and reverse-engineering researchers starting syscall-path and driver-communication-surface investigations.

## Links

- Repo: https://github.com/gmh5225/Driver-Communication-List

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[win32k-file-collection]] · [[win32k-file-collection2]] · [[ntsleuth]] · [[ntuserinjectmouseinput-syscall]] · [[driver-detect-nullshit]] · [[nulldriver-cheat]] · [[kernel-cheat-for-directx3d]]
