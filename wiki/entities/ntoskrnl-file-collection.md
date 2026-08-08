---
title: ntoskrnl-file-collection
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__ntoskrnl_file_collection.md
updated: 2026-08-08
confidence: medium
---

# ntoskrnl-file-collection

Archive of **ntoskrnl** binaries spanning multiple Windows builds. A reference corpus for comparative analysis and version-diff workflows—not a turnkey analyzer—aimed at kernel reverse engineers studying ntoskrnl changes across OS builds. (source: wiki/sources/descriptions/gmh5225__ntoskrnl_file_collection.md)

Pair with symbol-walking tools such as [[ntoskrnlwalker]] and [[ntkernelwalkerlib]] for target-build offset/gadget resolution, and with sibling GUI-subsystem corpora [[win32k-file-collection]] / [[win32k-file-collection2]] when diffing kernel attack surface beyond the executive image.

## Links

- Repo: https://github.com/gmh5225/ntoskrnl_file_collection

## Related

[[ntoskrnlwalker]] · [[ntkernelwalkerlib]] · [[win32k-file-collection]] · [[win32k-file-collection2]] · [[pdblister]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
