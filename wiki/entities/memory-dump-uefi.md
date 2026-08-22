---
title: Memory-Dump-UEFI
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/NoInitRD__Memory-Dump-UEFI.md
updated: 2026-08-22
confidence: medium
---

# Memory-Dump-UEFI

**UEFI application** for dumping **physical RAM** from a **live-boot environment**. Written in **C** with standard UEFI build tooling; designed to run from **USB media** alongside a **UEFI shell**. The repository ships scripts, build artifacts, and documentation for collecting full memory images on modern systems—aimed at **forensic acquisition** and **low-level security research** where **offline memory capture** is required without relying on a running OS kernel. (source: wiki/sources/descriptions/NoInitRD__Memory-Dump-UEFI.md)

Complements OS-side acquirers such as [[dumpit-mirror]] and [[tool-diy-system-memory-dump]], and firmware DXE packages such as [[offline-crash-dump-uefi]], by capturing raw physical memory from a **pre-OS UEFI boot** context.

## Links

- Repo: https://github.com/NoInitRD/Memory-Dump-UEFI

## Related

[[offline-crash-dump-uefi]] · [[dumpit-mirror]] · [[tool-diy-system-memory-dump]] · [[simpleuefi]] · [[volatility]] · [[volatility3]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
