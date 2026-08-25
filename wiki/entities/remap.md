---
title: Remap
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/EBalloon__Remap.md
updated: 2026-08-25
confidence: medium
---

# Remap

**Remap** (EBalloon) is a Windows **kernel page-remapping proof of concept** in C++. It copies virtual pages from a **protected process** into another process address space, demonstrating how that setup can enable cross-process **memory read/write** and **dumping** workflows. The repository documents supported **Windows 10** build ranges, operational caveats, and **crash-risk warnings** when cleanup is handled incorrectly. Primary use cases are **anti-cheat bypass** experimentation and low-level **process-memory research**. README category: cheat / Clone process. (source: wiki/sources/descriptions/EBalloon__Remap.md)

Sits in the protected-process access lane beside MDL/CR3 helpers such as [[meme-rw]] and dump-oriented tools such as [[ks-dumper]], but emphasizes **kernel VA remapping** into a surrogate process rather than direct vulnerable-driver RPM or PE rebuild paths.

## Links

- Repo: https://github.com/EBalloon/Remap

## Related

[[meme-rw]] · [[ks-dumper]] · [[ntmemory]] · [[driver-read-write]] · [[memmap]] · [[byovd]] · [[map-page]] · [[mm-copy-memory]] · [[super-people-sdk]] · [[veiled-experts-sdk]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
