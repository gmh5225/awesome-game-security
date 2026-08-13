---
title: Driver-Systemthread-from-PspCidTable-src
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-Systemthread-from-PspCidTable-src.md
updated: 2026-08-13
confidence: medium
---

# Driver-Systemthread-from-PspCidTable-src

Tutorial driver source for **hiding processes, threads, or handles** by manipulating Windows kernel **CID and handle tables**. (source: wiki/sources/descriptions/gmh5225__Driver-Systemthread-from-PspCidTable-src.md)

The sample implements two linked techniques: removing a target process handle table via **`ExRemoveHandleTable`**, and destroying process or thread handles in **`PspCidTable`** while zeroing selected **CID fields** to avoid immediate bug checks. It ships a large set of **build-specific offsets** for `EPROCESS`, `ETHREAD`, `PspCidTable`, and related routines — making it an offset-driven research reference rather than a portable library. Mainly useful for kernel researchers studying handle-table and CID-table manipulation to conceal system threads or processes on specific Windows builds.

README category: **Hide Process/Thread/Handle**. Offensive hide lane adjacent to [[blanket]] (ActiveProcessLinks + PspCidTable patch) and thread-stealth PoCs such as [[zero-thread-kernel]]; defensive counterparts include [[system-thread-finder]], [[stealth-sytem-thread-finder-be]], and [[rootkit-2]].

## Links

- Repo: https://github.com/gmh5225/Driver-Systemthread-from-PspCidTable-src

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[blanket]] · [[zero-thread-kernel]] · [[system-thread-finder]] · [[stealth-sytem-thread-finder-be]] · [[rootkit-2]] · [[research-rigor]]
