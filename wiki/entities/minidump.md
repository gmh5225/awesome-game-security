---
title: minidump
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/skelsec__minidump.md
updated: 2026-08-21
confidence: medium
---

# minidump

Python library for parsing Windows minidump (`.dmp`) files without Windows or WinDbg. Extracts process memory, thread contexts, module lists, exception records, and system info from full and mini dump formats; usable programmatically for automated analysis or credential extraction from LSASS dumps. Aimed at IR, forensics, and pentest workflows on cross-platform hosts. (source: wiki/sources/descriptions/skelsec__minidump.md)

Complements Python dump tooling such as [[minidumpreader]], C/C++ format libraries such as [[libmdmp]], Ghidra-native dump loading via [[ghidra-minidump-loader]] (runtime module mapping, private memory/thread stacks, thread-view stack walking), Ring3 MiniDump callback research such as [[atpminidump]], Unicorn-based offline execution via [[dumpulator]] (reconstruct layout from `.dmp` streams; syscall stubs / PEB·TEB / API hooks), WinDbg-flavored `MEMORY.DMP` analysis via [[ephemera]], RAM-image frameworks [[volatility]] / [[volatility3]], and LSASS post-dump forensics such as [[kvcforensic]].

## Links

- Repo: https://github.com/skelsec/minidump

## Related

[[atpminidump]] · [[dumpulator]] · [[ghidra-minidump-loader]] · [[libmdmp]] · [[minidumpreader]] · [[ephemera]] · [[kvcforensic]] · [[volatility]] · [[volatility3]] · [[mcp-windbg]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
