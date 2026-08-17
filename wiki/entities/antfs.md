---
title: ANTfs
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/ch3rn0byl__ANTfs.md
updated: 2026-08-17
confidence: medium
---

# ANTfs

Anti-forensics NTFS tool with dual user-mode and kernel-mode components: the console application recovers deleted files by parsing MFT entries into a target directory, while the WDK kernel driver overwrites file records and file-content clusters so recovery is impractical. Visual Studio 2019 solution (user app + driver). Useful for studying secure file deletion and NTFS anti-forensic techniques at the filesystem-driver level — the offensive counterpart to recovery tooling in the Delete File / IS forensics lane. (source: wiki/sources/descriptions/ch3rn0byl__ANTfs.md)

## Links

- Repo: https://github.com/ch3rn0byl/ANTfs

## Related

[[file-recovery-tool]] · [[ntfstool]] · [[ntfs-linker]] · [[ntfs-journal-viewer]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
