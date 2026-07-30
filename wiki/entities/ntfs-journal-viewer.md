---
title: NTFS Journal Viewer
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/mgeeky__ntfs-journal-viewer.md
updated: 2026-07-30
confidence: medium
---

# NTFS Journal Viewer

C NTFS change-journal viewer in the Anti Cheat → Information System & Forensics lane. Aimed at anti-cheat engineers and defensive researchers inspecting `$UsnJrnl` / USN change-journal activity on Windows volumes. (source: wiki/sources/descriptions/mgeeky__ntfs-journal-viewer.md)

Complements broader NTFS inspectors such as [[ntfstool]], USN↔MFT correlators such as [[ntfs-linker]], focused change-journal tooling such as [[usn]], and recovery/carving tools such as [[file-recovery-tool]] when the research target is journal visibility rather than full-volume layout or deleted-file reassembly.

## Links

- Repo: https://github.com/mgeeky/ntfs-journal-viewer

## Related

[[ntfstool]] · [[ntfs-linker]] · [[usn]] · [[file-recovery-tool]] · [[dfirtriage]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
