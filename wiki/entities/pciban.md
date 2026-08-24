---
title: pciban
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/KDIo3__PCIBan.md
updated: 2026-08-24
confidence: medium
---

# pciban

**pciban** (KDIo3/PCIBan) is a **proof-of-concept** for collecting **hardware identifiers directly from PCI and AHCI devices**. It **brute-forces PCI enumeration** and identifies **storage-related controllers** without relying on higher-level operating system APIs. The goal is to reduce exposure to software hooks that may spoof or intercept conventional HWID queries. Primarily useful for **anti-cheat** and **low-level platform security research**, with an explicit experimental caveat. README category: cheat / [A PoC for requesting HWIDs directly from hardware]. (source: wiki/sources/descriptions/KDIo3__PCIBan.md)

Sits on the **defensive Detection:HWID** side—direct hardware reads that bypass usermode/kernel hook surfaces targeted by spoofers such as [[easy-hwid-spoofer]] and [[mutante]]. Complements SMBIOS-oriented inventory tools such as [[hwid-checker-mg]] and [[windows-hardware-info]], and RAID0 serial uncloaking research such as [[uncloaking-raid0-hwid-serials]].

## Links

- Repo: https://github.com/KDIo3/PCIBan

## Related

[[hwid-checker-mg]] · [[windows-hardware-info]] · [[uncloaking-raid0-hwid-serials]] · [[easy-hwid-spoofer]] · [[mutante]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
