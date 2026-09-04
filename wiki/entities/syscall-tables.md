---
title: SyscallTables
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/hfiref0x__SyscallTables.md
updated: 2026-09-04
confidence: medium
---

# SyscallTables

Comprehensive **Windows system call tables** mapping native API function names to syscall numbers across many OS builds and architectures. Includes pre-generated tables for **ntoskrnl**, **win32k**, and **IUM** services spanning Windows Vista through Windows 11 on **x86-64** and **ARM64**, with tools to extract tables from `ntdll` or `win32u` using the **Zydis** disassembler and compose combined HTML or Markdown reference output. **scg** (C table dumper) and **sstComposer** (C# table generator) ship with the repo; online HTML views cover NT5.2 through current Windows 11 builds. (source: wiki/sources/descriptions/hfiref0x__SyscallTables.md)

Aimed at reverse engineers and security researchers who implement **direct syscalls**, analyze kernel interaction, or study user-mode hooking and anti-cheat evasion techniques. Complements per-build SSN extractors such as [[ntsleuth]] and direct-invocation libraries such as [[inline-syscall]], [[syscalls-cpp]], and [[ebyte-syscalls]]. Same author ecosystem as [[kdu]], [[upgdsed]], and [[winobjex64]].

## Links

- Repo: https://github.com/hfiref0x/syscalltables

## Related

[[ntsleuth]] · [[inline-syscall]] · [[syscalls-cpp]] · [[ebyte-syscalls]] · [[syscall-detect]] · [[win32k-file-collection]] · [[driver-communication-list]] · [[kdu]] · [[upgdsed]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
