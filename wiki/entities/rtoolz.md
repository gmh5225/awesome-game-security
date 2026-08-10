---
title: RToolZ
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__RToolZ.md
updated: 2026-08-10
confidence: medium
---

# RToolZ

Windows system utility with **rootkit-like** process, module, and [[kernel-callbacks]] management through a kernel driver backend. Capabilities include hiding and unhiding processes, enumerating kernel callbacks, removing notification routines, and manipulating process protection levels—aimed at kernel researchers studying system-manipulation tools and rootkit techniques rather than turnkey AC bypass. (source: wiki/sources/descriptions/gmh5225__RToolZ.md)

README tags the project with **`ProcExp152.sys`** (Process Explorer–family signed driver lane). Offensive hide counterpart: [[blanket]]. Defensive callback/process inspection: [[openark]], [[winobjex64]]. Callback/ETW blinders in the same research lane: [[telemetry-sourcerer]], [[bustercall]]. Hidden-process detection: [[rootkit-2]].

## Links

- Repo: https://github.com/gmh5225/RToolZ [ProcExp152.sys]

## Related

[[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[blanket]] · [[rootkit-2]] · [[openark]] · [[winobjex64]] · [[telemetry-sourcerer]] · [[bustercall]]
