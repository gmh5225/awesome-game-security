---
title: Win32kHooker
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/GetRektBoy724__Win32kHooker.md
updated: 2026-08-25
confidence: medium
---

# Win32kHooker

Windows kernel driver that demonstrates how to locate and hook function dispatch paths inside **win32k.sys** on modern systems. Uses C++ with kernel APIs, process context attachment, syscall mapping, and runtime disassembly to resolve hook targets in session space. Targets architectural changes where key pointers moved from simple global `.data` sections into opaque session-state structures — README tags it as a **`.data` ptr swapper for newer win32k versions**. Primary use case: advanced kernel graphics-subsystem research for anti-cheat, defensive engineering, and reverse engineering experiments. (source: wiki/sources/descriptions/GetRektBoy724__Win32kHooker.md)

Sits in the win32k hook / data-pointer-swap lane beside [[dataptrswap-driver]], [[comm-data-pointer-swap]], [[kernel-eac-be-comm]], [[callmewin32kdriver]], and static [[win32k-file-collection]] corpora for build-to-build GUI-subsystem RE.

## Links

- Repo: https://github.com/GetRektBoy724/Win32kHooker

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[dataptrswap-driver]] · [[comm-data-pointer-swap]] · [[kernel-eac-be-comm]] · [[callmewin32kdriver]] · [[win32k-file-collection]] · [[win32k-file-collection2]] · [[driver-communication-list]]
