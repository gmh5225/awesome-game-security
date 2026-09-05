---
title: NMI Stack Walk
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/1401199262__NMIStackWalk.md
updated: 2026-09-05
confidence: medium
---

# NMI Stack Walk

Windows kernel **proof of concept** (1401199262) for detecting **hidden no-module drivers** via **NMI-based stack walking**. It sends non-maskable interrupts to selected CPUs and performs stack backtraces inside an NMI callback to inspect suspicious execution paths. Implemented in C with a standard Visual Studio kernel-driver project layout; aimed at anti-rootkit and anti-cheat style detection research at kernel level. (source: wiki/sources/descriptions/1401199262__NMIStackWalk.md)

Complements NMI interrupted-RIP teaching drivers such as [[nmi-callback-handler]], multi-heuristic mapped-driver detectors such as [[nomad]] and [[kernel-anti-cheat]], and offensive NMI disable PoCs such as [[nmi]] within the [[kernel-callbacks]] lane.

## Links

- Repo: https://github.com/1401199262/NMIStackWalk [Mapped Driver by NMI Callback]

## Related

[[nmi-callback-handler]] · [[nomad]] · [[kernel-anti-cheat]] · [[ac]] · [[nmi]] · [[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
