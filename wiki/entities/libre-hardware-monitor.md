---
title: Libre Hardware Monitor
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/LibreHardwareMonitor__LibreHardwareMonitor.md
updated: 2026-08-23
confidence: medium
---

# Libre Hardware Monitor

Open-source **hardware telemetry** project providing a Windows desktop monitor and a reusable **.NET library** (primarily **C#**). Reads temperatures, fan speeds, voltages, loads, and clock data from CPUs, GPUs, storage devices, and other components; ships WinForms UI code and library APIs for integration into other applications. Primary use case is system diagnostics and sensor collection; often useful for **game performance monitoring** or **environment-aware security tooling**. (source: wiki/sources/descriptions/LibreHardwareMonitor__LibreHardwareMonitor.md)

Actively maintained successor/fork lineage to [[openhardwaremonitor]] in the usermode sensor-stack lane; BYOVD research on the legacy **`OpenHardwareMonitorLib.sys`** backend remains documented by [[openhardwaremonitor-poc]] rather than this repo's library surface.

Complements WMI inventory CLIs such as [[windows-hardware-info]], cross-platform inventory via [[hwinfo]], and low-level CPU telemetry samples such as [[winring0]] and [[windows-rapl-driver]].

## Links

- Repo: https://github.com/LibreHardwareMonitor/LibreHardwareMonitor

## Related

[[openhardwaremonitor]] · [[openhardwaremonitor-poc]] · [[windows-hardware-info]] · [[hwinfo]] · [[winring0]] · [[windows-rapl-driver]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
