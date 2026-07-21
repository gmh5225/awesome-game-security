---
title: NTFSTool
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/thewhiteninja__ntfstool.md
updated: 2026-07-21
confidence: medium
---

# NTFSTool

NTFS volume forensics tool: reads partition metadata (MBR, partition table, VBR), Master File Table, BitLocker-encrypted volumes, EFS-encrypted files, USN journal, and related NTFS structures. Aimed at anti-cheat engineers and defensive researchers in the Information System & Forensics lane. (source: wiki/sources/descriptions/thewhiteninja__ntfstool.md)

Complements recovery-oriented disk tools such as [[file-recovery-tool]] when inspecting live or imaged NTFS state (encryption, journals, MFT) rather than only deleted-file carving. For USN↔MFT timeline correlation, see [[ntfs-linker]].

## Links

- Repo: https://github.com/thewhiteninja/ntfstool

## Related

[[file-recovery-tool]] · [[ntfs-linker]] · [[dfirtriage]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
