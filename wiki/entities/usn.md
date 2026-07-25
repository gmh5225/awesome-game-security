---
title: USN
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/rbmm__USN.md
updated: 2026-07-25
confidence: medium
---

# USN

C++ / C/C++ repository focused on NTFS USN (Update Sequence Number / change journal) work in the Anti Cheat → Information System & Forensics lane. Aimed at anti-cheat engineers and defensive researchers inspecting filesystem change-journal activity. (source: wiki/sources/descriptions/rbmm__USN.md)

Sits alongside broader NTFS inspectors such as [[ntfstool]], USN↔MFT correlators such as [[ntfs-linker]], and recovery/carving tools such as [[file-recovery-tool]] when the research target is change-journal visibility rather than full-volume layout or deleted-file reassembly.

## Links

- Repo: https://github.com/rbmm/USN

## Related

[[ntfstool]] · [[ntfs-linker]] · [[file-recovery-tool]] · [[dfirtriage]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
