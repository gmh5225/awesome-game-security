---
title: IDontLikeFileLocks
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/EvilBytecode__IDontLikeFileLocks.md
updated: 2026-08-25
confidence: medium
---

# IDontLikeFileLocks

**IDontLikeFileLocks** (EvilBytecode) is a **C++ research collection** for extracting data from files locked by other running processes. It demonstrates several techniques, including **stealing memory-mapped section handles**, **duplicating and closing remote handles**, and related lock-bypass workflows. Examples target scenarios such as reading browser databases without stopping the browser, highlighting low-noise file acquisition behavior. (source: wiki/sources/descriptions/EvilBytecode__IDontLikeFileLocks.md)

Primary use case is **authorized security research and forensics** focused on understanding file-lock evasion and info-stealer tradecraft — complementary to handle-hijack teaching PoCs such as [[handle-ripper]], defensive file-lock stress samples such as [[lockfile-poc]], and credential-harvest tooling studied in the same handle-theft lane.

README category: Dump locked files by stealing memory-mapped section handle.

## Links

- Repo: https://github.com/EvilBytecode/IDontLikeFileLocks

## Related

[[handle-ripper]] · [[lockfile-poc]] · [[dumpy]] · [[lsass-dump-that-lsass]] · [[forensia]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
