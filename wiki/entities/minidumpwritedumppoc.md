---
title: MiniDumpWriteDumpPoC
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/Adepts-Of-0xCC__MiniDumpWriteDumpPoC.md
updated: 2026-09-03
confidence: medium
---

# MiniDumpWriteDumpPoC

C++ proof of concept that **hooks `MiniDumpWriteDump`** to intercept dump data **before it is written to disk**. Auxiliary **Python** scripts receive and decrypt transferred dump content. The workflow can optionally **encrypt** the captured buffer and **exfiltrate** it over a socket to a remote host, demonstrating how dump pipelines can be modified in memory. Intended for security research on **credential dumping tradecraft**, **detection engineering**, and **defensive validation**. (source: wiki/sources/descriptions/Adepts-Of-0xCC__MiniDumpWriteDumpPoC.md)

Complements defensive MiniDump callback instrumentation such as [[atpminidump]], user-mode LSASS acquisition PoCs such as [[lsass-dump-that-lsass]], and offline minidump parse tooling such as [[minidump]] / [[minidumpreader]].

README category: Dump Memory.

## Links

- Repo: https://github.com/Adepts-Of-0xCC/MiniDumpWriteDumpPoC

## Related

[[atpminidump]] · [[lsass-dump-that-lsass]] · [[minidump]] · [[minidumpreader]] · [[kvcforensic]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
