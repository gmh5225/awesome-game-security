---
title: windows-rapl-driver
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/hubblo-org__windows-rapl-driver.md
updated: 2026-08-05
confidence: medium
---

# windows-rapl-driver

Windows **kernel-mode driver** (`WindowsKernelModeDriver10.0`) that reads **RAPL** (Running Average Power Limit) energy metrics from a **bare-metal** host via CPU MSRs. Targets anti-cheat engineers and defensive security researchers in the Detection:HWID lane who need kernel-visible package/DRAM power counters as a hardware telemetry signal distinct from usermode sensor stacks or WMI inventory. (source: wiki/sources/descriptions/hubblo-org__windows-rapl-driver.md)

Complements usermode hardware monitors such as [[openhardwaremonitor]] and WMI inventory CLIs such as [[windows-hardware-info]]; sits beside other low-level CPU telemetry research such as [[apic]].

## Links

- Repo: https://github.com/hubblo-org/windows-rapl-driver

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[windows-hardware-info]] · [[openhardwaremonitor]] · [[hwinfo]] · [[apic]]
