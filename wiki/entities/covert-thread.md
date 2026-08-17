---
title: CovertThread (brew02)
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/brew02__CovertThread.md
updated: 2026-08-17
confidence: medium
---

# CovertThread (brew02)

**CovertThread** (brew02/CovertThread) is a Windows kernel driver that creates **transparent system threads** nearly invisible to system introspection. It removes a loaded module from the **system page tables**, sets up a fully controlled custom address space with its own **interrupt descriptor table (IDT)**, and blocks **per-thread inspection via non-maskable interrupts (NMIs)**. The driver can spawn threads from outside or inside the custom address space with **direct function execution**—no macros or wrapper calls required. Aimed at kernel security researchers studying covert thread execution, page-table manipulation, and anti-forensic techniques in Windows drivers. (source: wiki/sources/descriptions/brew02__CovertThread.md)

Complements thread-evasion PoCs such as [[zero-thread-kernel]] and [[driver-hide-kernel-thread-iocancelirp]], page-table tooling such as [[page-table-injector]], [[executor]], and [[pteditor]], and defensive NMI/APC thread forensics such as [[hidden-thread-finder]], [[kernel-anti-cheat]], and [[unkover]].

## Links

- Repo: https://github.com/brew02/CovertThread (README tag: Creating covert system threads on Windows by leveraging the page tables and IDT)

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[zero-thread-kernel]] · [[page-table-injector]] · [[executor]] · [[pteditor]] · [[hidden-thread-finder]] · [[stealth-sytem-thread-finder-be]] · [[fast-pf-hook]] · [[ki-user-exception-dispatcher-hook]] · [[mount-system-partition]]
