---
title: PTView
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/VollRagm__PTView.md
updated: 2026-08-19
confidence: medium
---

# PTView

**PTView** (VollRagm/PTView) is a Windows utility for **live inspection of process page tables** via a kernel driver plus graphical client. C++ kernel-side components pair with a C# interface to browse page-table entries, dump physical pages, and inspect PTE metadata. The tool supports virtual-to-physical translation workflows and large-page awareness for deeper memory-mapping analysis. Primary use cases are low-level OS memory research, debugging, and anti-cheat-oriented kernel investigations. (source: wiki/sources/descriptions/VollRagm__PTView.md)

README tags the project as **Browse Page Tables on Windows**. Complements page-table editors such as [[pteditor]] and injection research such as [[page-table-injector]]; same author as large-page mapper [[lpmapper]].

## Links

- Repo: https://github.com/VollRagm/PTView (README tag: Browse Page Tables on Windows)

## Related

[[pteditor]] · [[page-table-injector]] · [[readphys]] · [[ntmemory]] · [[lpmapper]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
