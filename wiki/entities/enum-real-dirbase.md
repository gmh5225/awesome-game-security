---
title: enum_real_dirbase
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Rythorndoran__enum_real_dirbase.md
updated: 2026-08-21
confidence: medium
---

# enum_real_dirbase

**enum_real_dirbase** (Rythorndoran) is a Windows kernel-mode driver proof of concept for enumerating real process directory base values (CR3) from physical memory structures. Written in C++ for the Windows Driver Kit, it implements low-level paging helpers, kernel pattern scanning, and PFN database traversal—initializing self-referencing page table bases, resolving `MmPfnDatabase` at runtime, and walking physical ranges to recover process context data. Primary use: kernel anti-cheat research, memory forensics experiments, and studying how hidden or protected address spaces are tracked. README category: cheat / Find real dirbase. (source: wiki/sources/descriptions/Rythorndoran__enum_real_dirbase.md)

Distinct from EAC-focused CR3 shuffle samples such as [[eac-cr3-shuffle]]—this PoC emphasizes **PFN-backed physical enumeration of directory bases** rather than observing AC-specific CR3 rotation. Complements cross-process translate libraries such as [[ntmemory]] and CR3 bypass teaching samples such as [[eac-cr3-bypass]].

## Links

- Repo: https://github.com/Rythorndoran/enum_real_dirbase

## Related

[[eac-cr3-shuffle]] · [[eac-cr3-bypass]] · [[ntmemory]] · [[meme-rw]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
