---
title: DriverBuddyReloaded
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__DriverBuddyReloaded.md
updated: 2026-08-13
confidence: medium
---

# DriverBuddyReloaded

IDA Pro plugin for reverse engineering Windows kernel drivers. Automates identification of IOCTL dispatch routines, IRP handler functions, and known vulnerable driver patterns, and annotates common Windows driver development structures in the disassembly. (source: wiki/sources/descriptions/gmh5225__DriverBuddyReloaded.md)

Complements WDF-specific annotation via [[ida-kmdf]], NT type enrichment via [[ntrays]], and export-based static review via [[cognitor]] — focused on interactive `.sys` RE inside IDA rather than live attach or batch rule engines.

## Links

- Repo: https://github.com/gmh5225/DriverBuddyReloaded

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ida-kmdf]] · [[ida-bitfields]] · [[ntrays]] · [[cognitor]] · [[cfb]] · [[easyanticheat-reversing]]
