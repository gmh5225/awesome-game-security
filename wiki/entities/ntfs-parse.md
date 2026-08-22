---
title: ntfs-parse
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/NTFSparse__ntfs_parse.md
updated: 2026-08-22
confidence: medium
---

# ntfs-parse

Python forensic NTFS parser suite that links artifacts across `$MFT`, `$LogFile`, and `$UsnJrnl`. Provides command-line tools for record export, transaction parsing, data extraction, and combined proof-of-concept timeline analysis. Modular parsers, helper scripts, and structured output formats (parsed text, CSV). Intended for digital forensics and file-system research rather than game cheating or anti-cheat bypass work. (source: wiki/sources/descriptions/NTFSparse__ntfs_parse.md)

Complements C++ correlators such as [[ntfs-linker]] and volume inspectors such as [[ntfstool]] when the goal is Python-based cross-artifact NTFS parsing with exportable structured output.

## Links

- Repo: https://github.com/NTFSparse/ntfs_parse

## Related

[[ntfs-linker]] · [[ntfstool]] · [[ntfs-journal-viewer]] · [[file-recovery-tool]] · [[dfirtriage]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
