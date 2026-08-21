---
title: Nomad
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Rwkeith__Nomad.md
updated: 2026-08-21
confidence: medium
---

# Nomad

Windows **kernel anti-cheat-style detector** (Rwkeith) for finding **manually mapped drivers** and **suspicious kernel threads**. Written in C++ as a driver-oriented codebase focused on low-level telemetry; aimed at anti-cheat engineering and kernel security research against stealthy cheat implants. (source: wiki/sources/descriptions/Rwkeith__Nomad.md)

Complements multi-heuristic AC prototypes such as [[kernel-anticheat]] and [[kernel-anti-cheat]], hidden-thread scanners such as [[unkover]], NMI stack-walk research such as [[nmi-callback-handler]], and [[kernel-pool-scanning]] big-pool forensics.

## Detection heuristics

| Check | Target |
|-------|--------|
| **Thread stack walking** | Return frames outside loaded module images |
| **Thread entry-point validation** | System threads with anomalous start addresses |
| **Big pool scanning** | Large-pool allocations with abnormal references |
| **IOCTL hook detection** | Signals of dispatch-table or IOCTL-path tampering |

## Links

- Repo: https://github.com/Rwkeith/Nomad [Mapped Driver]

## Related

[[kernel-anticheat]] · [[kernel-anti-cheat]] · [[unkover]] · [[nmi-callback-handler]] · [[kernel-pool-scanning]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
