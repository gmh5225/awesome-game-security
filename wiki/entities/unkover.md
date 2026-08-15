---
title: unKover
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/eversinc33__unKover.md
updated: 2026-08-15
confidence: medium
---

# unKover

Windows **kernel-mode hidden-thread and rootkit-artifact detector** (eversinc33). The C driver enumerates system threads through multiple independent paths—**scheduler lists**, **PspCidTable walks**, and **stack scanning**—then cross-references the results to surface threads that are concealed from standard API enumeration. It targets **anti-cheat and rootkit thread-hiding techniques**, including stealth threads from manually mapped drivers, and uses **NMI/APC**-based inspection to help detect mapped-driver artifacts. Aimed at anti-cheat developers and kernel forensics researchers studying stealth system threads. (source: wiki/sources/descriptions/eversinc33__unKover.md)

Complements BE-style heuristics in [[system-thread-finder]] and [[stealth-sytem-thread-finder-be]], KTHREAD tamper experiments in [[hidden-thread-finder]], and defensive NMI stack-walk research in [[kernel-anti-cheat]] and [[nmi-nmi-callback]].

## Links

- Repo: https://github.com/eversinc33/unKover

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[system-thread-finder]] · [[stealth-sytem-thread-finder-be]] · [[hidden-thread-finder]] · [[kernel-anti-cheat]] · [[nmi-nmi-callback]] · [[rootkit-2]] · [[zero-thread-kernel]]
