---
title: ntoskrnl-viewer
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/IcEy-999__Ntoskrnl_Viewer.md
updated: 2026-08-24
confidence: medium
---

# ntoskrnl-viewer

**Windows kernel memory viewer** that uses symbols to inspect **ntoskrnl** data from a **custom driver** and **user-mode client** (IcEy-999). Provides **WinDbg-like commands** — `db`, `dw`, `dd`, `dq`, `d`, and `x` — to read memory by **symbol or address**, including **exported and unexported kernel symbols**. Built with C/C++ components across ring-0 and ring-3 modules; targets **x64** systems. Useful for **kernel reverse engineering**, **troubleshooting**, and **low-level Windows internals** study. (source: wiki/sources/descriptions/IcEy-999__Ntoskrnl_Viewer.md)

Complements offline symbol/offset resolution via [[ntoskrnlwalker]] and [[ntkernelwalkerlib]], static struct browsers such as [[bb]] / [[bb-viewer]], and full attach-based debugging via WinDbg — this tool focuses on **live kernel memory inspection** through a dedicated driver channel rather than parsing a local `ntoskrnl.exe` image alone.

## Links

- Repo: https://github.com/IcEy-999/Ntoskrnl_Viewer

## Related

[[ntoskrnlwalker]] · [[ntkernelwalkerlib]] · [[ntoskrnl-file-collection]] · [[mssymbolscollection]] · [[cfgdump]] · [[windbg-js-scripts]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
