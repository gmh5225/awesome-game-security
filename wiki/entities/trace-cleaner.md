---
title: TraceCleaner
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/BadPlayer555__TraceCleaner.md
updated: 2026-08-31
confidence: medium
---

# TraceCleaner

Minimal Windows kernel driver example for removing common **driver trace artifacts** after manual mapping. C++ kernel-mode code clears entries from **MmUnloadedDrivers** and **PiDDBCacheTable** — structures frequently examined in forensic and anti-cheat contexts. Intended for execution through manual-mapping workflows; primary use case is educational research on kernel trace hygiene and anti-cheat detection surfaces. (source: wiki/sources/descriptions/BadPlayer555__TraceCleaner.md)

## Links

- Repo: https://github.com/BadPlayer555/TraceCleaner

## Related

[[clear-driver-traces]] · [[driver-read-write]] · [[hide-driver-testing]] · [[nullmap]] · [[revert-mapper]] · [[kernel-pool-scanning]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
