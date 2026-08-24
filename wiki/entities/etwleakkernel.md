---
title: EtwLeakKernel
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Idov31__EtwLeakKernel.md
updated: 2026-08-24
confidence: medium
---

# EtwLeakKernel

Windows **proof-of-concept** (Idov31) that **leaks kernel memory addresses through ETW stack traces**. It starts an ETW consumer session, **requests stack data from providers**, and **parses event output** to recover **kernel pointers**. Implemented in **C++** for Windows and requires **Administrator** privileges to start consuming provider events. Intended for **exploitation research** and studying **kernel address exposure paths** via telemetry consumers—not a bypass or AC evasion tool. (source: wiki/sources/descriptions/Idov31__EtwLeakKernel.md)

Complements schema-oriented ETW tooling such as [[etw-explorer]] and syscall-logging consumers such as [[etw-syscall-monitor]] on the consumer-side research lane documented in [[etw-threat-intelligence]]. Same author lane as [[novahypervisor]] and [[idov31-venom]].

## Links

- Repo: https://github.com/Idov31/EtwLeakKernel [Leaking kernel addresses from ETW consumers. Requires Administrator privileges]

## Related

[[etw-threat-intelligence]] · [[etw-explorer]] · [[etw-syscall-monitor]] · [[novahypervisor]] · [[idov31-venom]] · [[overviews/windows-kernel]]
