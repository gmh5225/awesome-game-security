---
title: OpenHardwareMonitor
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/openhardwaremonitor__openhardwaremonitor.md
updated: 2026-07-26
confidence: medium
---

# OpenHardwareMonitor

Open-source **hardware monitoring** project (primarily C# / JavaScript) listed under Anti Cheat → Detection:HWID. Exposes CPU/GPU/sensor and related machine-identity signals that defensive HWID pipelines inventory; the stack includes kernel/driver paths used to read hardware sensors. Aimed at anti-cheat engineers studying how monitor libraries surface identifiers and telemetry. (source: wiki/sources/descriptions/openhardwaremonitor__openhardwaremonitor.md)

Complements WMI inventory CLIs such as [[windows-hardware-info]], GPU/board fingerprint tooling such as [[nvidiaapi]], and sits opposite offensive HWID spoofers such as [[hwidspoofer]] / [[spoofer-amidewin]].

## Links

- Repo: https://github.com/openhardwaremonitor/openhardwaremonitor

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[windows-hardware-info]] · [[nvidiaapi]] · [[tpm-mmio]] · [[hwidspoofer]]
