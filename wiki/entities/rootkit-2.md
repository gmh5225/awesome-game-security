---
title: Rootkit-2
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Rootkit-2.md
updated: 2026-08-10
confidence: medium
---

# Rootkit-2

Kernel proof-of-concept driver for **detecting hidden processes** by walking **CSRSS-maintained** data structures instead of trusting ordinary process-enumeration paths. The driver attaches to each `csrss.exe` instance, locates `CsrExecServerThread` inside `csrsrv.dll`, pattern-scans it to recover the `CSR_PROCESS` list head, then walks that linked list to resolve every client PID back to an **EPROCESS**. Printing recovered PIDs and image names demonstrates a secondary enumeration path that can still expose processes hidden from more obvious views (`ActiveProcessLinks` unlink, `PspCidTable` patches, `NtQuerySystemInformation` hooks). (source: wiki/sources/descriptions/gmh5225__Rootkit-2.md)

Useful for anti-cheat and kernel researchers studying hidden-process detection, CSRSS internals, and alternative enumeration strategies for rootkit triage. Offensive hide counterpart: [[blanket]]. Offline RAM forensics: [[volatility]] / [[volatility3]] (`psscan` vs `pslist` gaps). Live inspection: [[openark]], [[systeminformer]].

## Links

- Repo: https://github.com/gmh5225/Rootkit-2 [Using CsrRootProcess to detect hidden process]

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[blanket]] · [[openark]] · [[volatility]] · [[volatility3]] · [[stealth-sytem-thread-finder-be]] · [[system-thread-finder]]
