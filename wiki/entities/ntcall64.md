---
title: NtCall64
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/hfiref0x__NtCall64.md
updated: 2026-09-11
confidence: medium
---

# NtCall64

**NtCall64** (hfiref0x) is a Windows NT **x64 system call fuzzer** that stress-tests kernel service tables on 64-bit Windows 7 and later. Written primarily in C with minimal assembly, it extends the classic NtCall approach to fuzz **ntoskrnl** syscalls and optionally the **win32k Shadow SSDT**, generating randomized parameters with optional heuristics and configurable pass counts per call. INI-file blacklists skip dangerous services; operators can target individual syscall IDs, log parameters to a file or serial port, and run elevated as **LocalSystem** for deeper coverage. The tool targets kernel security researchers and reverse engineers hunting Windows driver and syscall vulnerabilities, stability bugs, and privilege-escalation issues, and has been used to discover flaws in both win32k and ntoskrnl handlers. (source: wiki/sources/descriptions/hfiref0x__NtCall64.md)

Complements static SSN reference work such as [[syscall-tables]] and per-build extractors such as [[ntsleuth]] in the same service-table lane; pairs with Application Verifier DynFault injection such as [[vfdynf]] and Go kernel/AC analysis workbenches such as [[kernforge]] for stress and unit-test harness research. Same author ecosystem as [[kdu]], [[upgdsed]], and [[winobjex64]].

## Links

- Repo: https://github.com/hfiref0x/ntcall64

## Related

[[syscall-tables]] · [[ntsleuth]] · [[vfdynf]] · [[kernforge]] · [[anti-cheat-emulator]] · [[higu-ntcall]] · [[inline-syscall]] · [[syscall-detect]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
