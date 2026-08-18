---
title: KslDump
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/andreisss__KslDump.md
updated: 2026-08-18
confidence: medium
---

# KslDump

PPL-protected **LSASS** credential extractor that uses only **Microsoft-signed components** already on the system. It abuses a vulnerable legacy on-disk Microsoft Defender **`KslD.sys`** driver: IOCTL **`0x222044`** sub-commands expose arbitrary kernel memory read via **`MmCopyMemory`** and CPU control-register disclosure for **KASLR** defeat. The attack chain repoints the Defender service to the old unpatched driver binary left on disk—**no external driver load** required. Aimed at researchers studying vendor-shipped vulnerable-driver [[byovd]] chains and **PPL bypass** for protected-process memory access. (source: wiki/sources/descriptions/andreisss__KslDump.md)

Adjacent to [[kslkatz]] in the Defender `KslD.sys` credential-extraction lane; differs by focusing on full PPL LSASS dump via legacy on-disk driver reuse rather than WDigest/LSA secret parsing alone.

## Links

- Repo: https://github.com/andreisss/KslDump

## Related

[[byovd]] · [[kslkatz]] · [[pplkiller]] · [[kvc]] · [[lsass-dump-that-lsass]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
