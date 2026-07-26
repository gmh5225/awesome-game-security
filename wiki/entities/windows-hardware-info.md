---
title: WindowsHardwareInfo
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/paradoxwastaken__WindowsHardwareInfo.md
updated: 2026-07-26
confidence: medium
---

# WindowsHardwareInfo

C++ CLI that queries Windows hardware identifiers via the **WMI (Windows Management Instrumentation)** service. Aimed at anti-cheat engineers and defensive researchers in the Detection:HWID lane who need a simple inventory of hardware info of interest. (source: wiki/sources/descriptions/paradoxwastaken__WindowsHardwareInfo.md)

Complements GPU/board fingerprint tooling such as [[nvidiaapi]], TPM EK ground-truth paths such as [[tpm-mmio]], and sits opposite offensive HWID spoofers such as [[hwidspoofer]] / [[spoofer-amidewin]].

## Links

- Repo: https://github.com/paradoxwastaken/WindowsHardwareInfo

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[nvidiaapi]] · [[tpm-mmio]] · [[hwidspoofer]] · [[spoofer-amidewin]]
