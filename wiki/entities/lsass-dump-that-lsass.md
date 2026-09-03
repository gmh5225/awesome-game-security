---
title: LSASS-DumpThatLSASS
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__LSASS-DumpThatLSASS.md
updated: 2026-08-12
confidence: medium
---

# LSASS-DumpThatLSASS

User-mode **LSASS dumping** proof of concept that combines **handle theft** with an unhooked copy of DbgHelp and a lightly obfuscated dump path. The tool enumerates `SystemHandleInformation`, duplicates candidate process handles, filters by full image path containing `lsass.exe`, writes the dump via `MiniDumpWriteDump` through a fresh `DbgHelp.dll` loaded from disk (avoiding possibly hooked exports), then encrypts the resulting file on disk. (source: wiki/sources/descriptions/gmh5225__LSASS-DumpThatLSASS.md)

Useful for Windows security researchers studying handle-based dump acquisition, user-mode hook evasion around `MiniDumpWriteDump`, and tradeoffs of recycled privileged handles — complementary to in-memory dump-pipeline hook PoCs such as [[minidumpwritedumppoc]], user-mode LSASS handle-reuse bypass demos such as [[lsass-usermode-bypass]], kernel [[byovd]] LSASS readers such as [[kslkatz]], and trusted-process mapping research such as [[lsass-extend-mapper]].

README category: Elevating Handle.

## Links

- Repo: https://github.com/gmh5225/LSASS-DumpThatLSASS

## Related

[[libelevate]] · [[kslkatz]] · [[kvcforensic]] · [[minidump]] · [[lsass-extend-mapper]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
