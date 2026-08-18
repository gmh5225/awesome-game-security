---
title: WinRing0
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/ashleyhung__WinRing0.md
updated: 2026-08-18
confidence: medium
---

# WinRing0

Windows **C++ sample** that uses the **WinRing0** driver and user-mode API to read low-level **CPU telemetry**, especially **per-core temperatures**. It accesses **CPUID** and **MSR** data through bundled kernel-driver and library components, logs results to a local record file, and ships headers, binaries, and a simple console program for monitoring under **administrator** privileges. Primary use case: hardware monitoring and low-level Windows systems programming practice—not an AC bypass or BYOVD framework. (source: wiki/sources/descriptions/ashleyhung__WinRing0.md)

Sits in the same CPU/MSR telemetry lane as [[windows-rapl-driver]] and usermode sensor stacks such as [[openhardwaremonitor]]; contrasts with MSR-exposure exploit PoCs such as [[openhardwaremonitor-poc]].

## Links

- Repo: https://github.com/ashleyhung/WinRing0

## Related

[[overviews/windows-kernel]] · [[windows-rapl-driver]] · [[openhardwaremonitor]] · [[openhardwaremonitor-poc]] · [[apic]]
