---
title: Ebyte-Syscalls
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/EvilBytecode__Ebyte-Syscalls.md
updated: 2026-08-25
confidence: medium
---

# Ebyte-Syscalls

**Ebyte-Syscalls** (EvilBytecode) is a **header-only C++** library for **direct and indirect Windows syscalls** without standard API imports. It resolves **syscall numbers (SSN)** at runtime by walking **PEB loader data** and parsing **ntdll export tables**, and supports **indirect syscall trampolines** for EDR / user-mode hook evasion. README also documents **VEH-based function call obfuscation** — guard pages, **INT3** breakpoints, and byte switching without allocating executable memory or inline assembly stubs. Primary audience: offensive security researchers and anti-cheat analysts studying syscall-level API hook bypass and detection. (source: wiki/sources/descriptions/EvilBytecode__Ebyte-Syscalls.md)

Complements compile-time direct-syscall libraries such as [[syscalls-cpp]] and [[inline-syscall]], runtime indirect-syscall samples such as [[doom-syscalls]], and syscall-origin detectors such as [[syscall-detect]]. Same-author VEH research such as [[ghostveh]] overlaps on exception-driven call obfuscation.

## Links

- Repo: https://github.com/EvilBytecode/Ebyte-Syscalls

## Related

[[syscalls-cpp]] · [[inline-syscall]] · [[doom-syscalls]] · [[syscall-detect]] · [[ntsleuth]] · [[known-dll-unhook]] · [[ghostveh]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
