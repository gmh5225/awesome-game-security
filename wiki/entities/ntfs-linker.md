---
title: ntfs-linker
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/strozfriedberg__ntfs-linker.md
updated: 2026-07-21
confidence: medium
---

# ntfs-linker

C++ NTFS forensic correlator: parses `$MFT`, `$UsnJrnl`, and `$LogFile`, then links change-journal entries to MFT records to rebuild filesystem activity timelines—full paths plus create / modify / rename / delete events. Aimed at digital forensics analysts investigating NTFS volume activity. (source: wiki/sources/descriptions/strozfriedberg__ntfs-linker.md)

Complements structure/encryption inspectors such as [[ntfstool]] and recovery/carving tools such as [[file-recovery-tool]] when the goal is USN↔MFT timeline correlation rather than volume layout or deleted-file reassembly.

## Links

- Repo: https://github.com/strozfriedberg/ntfs-linker

## Related

[[ntfstool]] · [[file-recovery-tool]] · [[dfirtriage]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
