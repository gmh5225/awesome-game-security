---
title: cheat-engine-undetectable
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/NulledNah__cheat-engine-undetectable.md
updated: 2026-08-22
confidence: medium
---

# cheat-engine-undetectable

**Modified Cheat Engine build** (NulledNah/cheat-engine-undetectable) that layers multi-tier anti-cheat evasion for academic cybersecurity research and reverse-engineering education. Written primarily in **Free Pascal (Lazarus)** with **PowerShell** build and post-processing scripts that clone upstream [[cheat-engine]], apply patches, and produce a stealth-compiled binary. (source: wiki/sources/descriptions/NulledNah__cheat-engine-undetectable.md)

**Tier 1 (user-mode)** techniques include surface obfuscation, **direct NT syscall stubs** to bypass hooked `ntdll` routines, and **PE metadata mutation** such as Rich Header stripping and section renaming. **Tier 2 (kernel bridge)** detects common anti-cheat engines and, when a signed vulnerable driver is available, performs **CR3-based page-table memory access**, **ObCallback bypass**, and **process hiding** without opening target handles. Hypervisor-level DMA bypass is documented but not implemented. The repository targets researchers studying anti-cheat architecture, Windows kernel internals, and evasion methods rather than production game cheating.

Contrasts with title-specific CE bypass forks such as [[ce-easyanticheat-bypass]], out-of-band DMA CE paths ([[cheat-engine-ceserver-pcileech]], [[cheat-engine-dma-plugin]]), and defensive CE artifact detectors ([[detection-cheat-engine]], [[detection-cheat-engine-ring0]], [[cedetector]]) that map the same detection surfaces from the defender side.

## Links

- Repo: https://github.com/NulledNah/cheat-engine-undetectable

## Related

[[cheat-engine]] · [[ce-easyanticheat-bypass]] · [[detection-cheat-engine]] · [[detection-cheat-engine-ring0]] · [[dbk64-vulnerability-driver]] · [[byovd]] · [[syscall-detect]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
