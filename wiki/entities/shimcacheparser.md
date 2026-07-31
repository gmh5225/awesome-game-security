---
title: ShimCacheParser
kind: entity
topics: [reverse-engineering, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/mandiant__ShimCacheParser.md
updated: 2026-07-31
confidence: medium
---

# ShimCacheParser

Python parser for Application Compatibility Shim Cache (AppCompatCache) entries in offline Windows registry hives. Reads ShimCache data from the SYSTEM hive, extracts file paths, timestamps, and execution flags across Windows XP through Windows 10, and exports CSV or timeline output for DFIR program-execution history reconstruction. (source: wiki/sources/descriptions/mandiant__ShimCacheParser.md)

Complements live triage collectors such as [[dfirtriage]] and kernel load-artifact forensics (PiDDBCache, MmUnloadedDrivers) when investigating what ran on a host before deeper memory or disk analysis.

## Links

- Repo: https://github.com/mandiant/ShimCacheParser

## Related

[[dfirtriage]] · [[volatility3]] · [[kernel-pool-scanning]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
