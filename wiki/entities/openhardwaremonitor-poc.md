---
title: OpenHardwareMonitor-PoC
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__OpenHardwareMonitor-PoC.md
updated: 2026-08-11
confidence: medium
---

# OpenHardwareMonitor-PoC

Minimal proof-of-concept for a vulnerability in **`OpenHardwareMonitorLib.sys`**: opens the device and wraps IOCTLs **`0x9C402084`** and **`0x9C402088`** to read and write arbitrary MSRs from user mode via simple `read_msr` / `write_msr` helpers. Intentionally small — a focused demonstration of the exposed MSR primitive rather than a full exploitation framework. Useful for Windows security researchers studying vulnerable hardware-monitoring drivers, MSR exposure bugs, and user-mode access to privileged CPU controls. (source: wiki/sources/descriptions/gmh5225__OpenHardwareMonitor-PoC.md)

Same hardware-monitoring driver backend as [[openhardwaremonitor]]; sits in the [[byovd]] / legacy monitoring-tool lane beside [[speedfan-exploit]] and [[lenovo-cve-2025-8061]] (MSR-oriented OEM driver abuse).

## Links

- Repo: https://github.com/gmh5225/OpenHardwareMonitor-PoC

## Related

[[openhardwaremonitor]] · [[byovd]] · [[speedfan-exploit]] · [[lenovo-cve-2025-8061]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
