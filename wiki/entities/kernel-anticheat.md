---
title: Kernel Anticheat
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Vasieco__Kernel-Anticheat.md
updated: 2026-08-19
confidence: medium
---

# Kernel Anticheat

Windows **kernel anti-cheat prototype driver** from Vasieco that scans the host for suspicious cheating indicators via low-level integrity checks. Written in C/C++ with Visual Studio driver projects; aimed at anti-cheat research and experimentation with kernel-mode detection techniques — not a production anti-cheat product. (source: wiki/sources/descriptions/Vasieco__Kernel-Anticheat.md)

Complements multi-telemetry AC sandboxes such as [[kernel-anti-cheat]] and [[ac]], mapper-forensics concepts in [[kernel-pool-scanning]], and hypervisor-detection research in the Windows kernel overview.

## Detection checks

| Check | Target |
|-------|--------|
| **Unsigned / abnormal drivers** | Drivers that fail expected signing or load-path norms |
| **Physical memory handle abuse** | Suspicious `\Device\PhysicalMemory` or equivalent physmem access |
| **Hypervisor traces** | Below-OS or hacked-hypervisor presence indicators |
| **Big pool artifacts** | Large-pool allocations inconsistent with loaded modules |
| **Mapper traces** | Manual-map / driver-mapper load residue |
| **Suspicious system threads** | System threads with anomalous start addresses or context |

## Links

- Repo: https://github.com/Vasieco/Kernel-Anticheat

## Related

[[kernel-anti-cheat]] · [[ac]] · [[acdrv]] · [[kernel-pool-scanning]] · [[known-driver-mappers]] · [[byovd]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
