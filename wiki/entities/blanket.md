---
title: Blanket
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/kitty8904__blanket.md
updated: 2026-08-13
confidence: medium
---

# Blanket

Windows process-hiding tool for kernel researchers studying rootkit-style concealment and its detection. Unlinks the target process from **ActiveProcessLinks**, patches **PspCidTable** entries, and hooks **NtQuerySystemInformation** so the process disappears from Task Manager and other enumeration APIs. (source: wiki/sources/descriptions/kitty8904__blanket.md)

README category: Hide Kernel Thread. Offensive hide lane adjacent to [[hide-driver]] (driver-list unlink), [[hide-file]] (kernel file hide), and [[driver-systemthread-from-pspcidtable-src]] (gmh5225; `ExRemoveHandleTable` + direct PspCidTable handle/CID manipulation; build-specific offset tables) (source: wiki/sources/descriptions/gmh5225__Driver-Systemthread-from-PspCidTable-src.md); defensive counterparts include [[openark]], [[volatility]] / [[volatility3]] (offline `psscan` vs live `pslist` gaps), and [[systeminformer]].

## Links

- Repo: https://github.com/kitty8904/blanket

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[hide-driver]] · [[hide-file]] · [[driver-systemthread-from-pspcidtable-src]] · [[openark]] · [[volatility]] · [[systeminformer]]
