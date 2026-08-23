---
title: cormem.sys-vulnerable-driver
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/KeServiceDescriptorTable__cormem.sys-vulnerable-driver.md
updated: 2026-08-23
confidence: medium
---

# cormem.sys-vulnerable-driver

Provides the **`cormem.sys`** vulnerable Windows kernel driver binary for security research. The driver exposes **memory read and write primitives** that can be exploited for kernel-level access, making it a candidate for [[byovd]] (Bring Your Own Vulnerable Driver) attack research. Mainly useful for kernel security researchers and anti-cheat analysts studying vulnerable-driver exploitation and detection techniques. (source: wiki/sources/descriptions/KeServiceDescriptorTable__cormem.sys-vulnerable-driver.md)

Sits beside the broader KeServiceDescriptorTable curated corpus [[vulnerable-drivers]] as a focused single-driver distribution rather than a multi-vendor collection.

## Links

- Repo: https://github.com/KeServiceDescriptorTable/cormem.sys-vulnerable-driver
- README tag: `[cormem.sys]`

## Related

[[byovd]] · [[vulnerable-drivers]] · [[loldrivers]] · [[ms-vulnerable-driver-list]] · [[drivers-and-shit]] · [[vulnerable-driver-scanner]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
