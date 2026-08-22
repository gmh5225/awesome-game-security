---
title: KnownDllUnhook
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/ORCx41__KnownDllUnhook.md
updated: 2026-08-22
confidence: medium
---

# KnownDllUnhook

Windows API **unhooking** utility that restores module **`.text`** sections from clean images in the **`\KnownDlls`** namespace. Iterates loaded DLLs, maps trusted copies from KnownDlls, replaces hooked executable code, and restores original memory protections. Critical memory and mapping operations use **low-level native syscalls** rather than potentially hooked Win32/NT APIs. Intended for security research on **EDR** or **anti-cheat** hook detection and evasion behavior. (source: wiki/sources/descriptions/ORCx41__KnownDllUnhook.md)

Complements clean-reference NTDLL restore tooling such as [[nt-unhooker]], BYOVD blind-and-unhook stacks such as [[edrsandblast]], modular anti-analysis kits with system DLL unhooking such as [[dynamizer]], and KnownDlls-oriented injection research such as [[injection]].

## Links

- Repo: https://github.com/ORCx41/KnownDllUnhook

## Related

[[nt-unhooker]] · [[edrsandblast]] · [[dynamizer]] · [[injection]] · [[syscall-detect]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
