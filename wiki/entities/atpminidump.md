---
title: ATPMiniDump
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/b4rtik__ATPMiniDump.md
updated: 2026-08-18
confidence: medium
---

# ATPMiniDump

C/C++ research project focused on the **aTPMiniDump callback** — user-mode (Ring 3) instrumentation around Windows minidump generation for memory analysis. Aimed at anti-cheat engineers and defensive security researchers studying how security products hook or observe `MiniDumpWriteDump` / DbgHelp callback paths to detect credential dumping and related tamper attempts. (source: wiki/sources/descriptions/b4rtik__ATPMiniDump.md)

Complements offline minidump parse tooling such as [[minidump]] / [[minidumpreader]] / [[libmdmp]], offensive LSASS dump PoCs such as [[lsass-dump-that-lsass]], and post-dump credential forensics such as [[kvcforensic]].

## Links

- Repo: https://github.com/b4rtik/ATPMiniDump

## Related

[[minidump]] · [[minidumpreader]] · [[libmdmp]] · [[lsass-dump-that-lsass]] · [[kvcforensic]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
