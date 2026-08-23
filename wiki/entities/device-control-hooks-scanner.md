---
title: device-control-hooks-scanner
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Luchinkin__device-control-hooks-scanner.md
updated: 2026-08-23
confidence: medium
---

# device-control-hooks-scanner

Windows **kernel-mode scanner** (C++ **KMDF** driver) that audits **`IRP_MJ_DEVICE_CONTROL`** dispatch handlers for suspicious hooks. It walks the **`\Driver` object directory** to enumerate loaded driver objects, checks whether each device-control dispatch pointer stays within the owning driver image bounds, and attempts **module resolution** when pointers fall outside that range. Intended for **kernel integrity auditing** and low-level **driver hook detection** research. (source: wiki/sources/descriptions/Luchinkin__device-control-hooks-scanner.md)

README lane: **device-control-hooks-scanner**.

Complements broader hook-scanning suites such as [[slauc91-anticheat]] (SSDT/IDT/IRP/MSR checks) and GUI anti-rootkit toolkits such as [[openark]]. Offensive `IRP_MJ_DEVICE_CONTROL` hijack samples such as [[driver-read-write]] and [[hwid-kernel-spoofer]] illustrate the dispatch-table tampering this scanner targets. IRP monitoring frameworks such as [[cfb]] log IOCTL traffic rather than validating dispatch pointer integrity.

## Links

- Repo: https://github.com/Luchinkin/device-control-hooks-scanner (README tag: device-control-hooks-scanner)

## Related

[[slauc91-anticheat]] · [[openark]] · [[driver-read-write]] · [[driver-detect-nullshit]] · [[cfb]] · [[hwid-kernel-spoofer]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
