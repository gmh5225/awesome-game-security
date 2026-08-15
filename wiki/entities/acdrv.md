---
title: AcDrv
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__AcDrv.md
updated: 2026-08-15
confidence: medium
---

# AcDrv

Windows kernel driver aimed at anti-cheat or security research. Implements kernel-level monitoring through process callback registration, module load tracking, memory access interception, and system call monitoring via a custom driver interface — for researchers building or studying anti-cheat driver components. (source: wiki/sources/descriptions/gmh5225__AcDrv.md)

Complements ETW-backed syscall hook samples such as [[etwhook-infinityhookclass]] and [[etw-syscall]], multi-telemetry AC prototypes such as [[kernel-anti-cheat]], and ThreatIntel consumers such as [[tietwagent]] in the same kernel monitoring / ETW Hook lane.

## Links

- Repo: https://github.com/gmh5225/AcDrv (README tag: ETW Hook)

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[etw-threat-intelligence]] · [[kernel-callbacks]] · [[etwhook-infinityhookclass]] · [[etw-syscall]] · [[kernel-anti-cheat]]
