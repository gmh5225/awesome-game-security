---
title: HyperHide
kind: entity
topics: [reverse-engineering, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/Air14__HyperHide.md
updated: 2026-09-03
confidence: medium
---

# HyperHide

Open-source **hypervisor-based anti-anti-debug plugin** for **x64dbg** and **x32dbg**. Uses a **kernel driver** with **Intel VT-x/EPT** to hook and sanitize many debugger-detection surfaces — **PEB** values, thread and process flags, and numerous **Nt\*** API query results — on **64-bit Windows** while preserving practical attach-and-trace workflows. Widely applicable to reverse engineering and game-security research against heavily protected binaries. (source: wiki/sources/descriptions/Air14__HyperHide.md)

Sits in the VT-x stealth-debug lane beside [[hyperdbg]] and [[vt-debuger]]; complements SSDT-tamper hide drivers such as [[titanhide]] and usermode ScyllaHide-class plugins such as [[scyllahide-for-ida9.0rc]]. Defensive samples such as [[scyllahidedetector2]] and [[antidbg-baka]] explicitly target HyperHide-class hides. Same author lane as [[kdbgdecryptor]] (Air14 kernel debugging utilities).

## Links

- Repo: https://github.com/Air14/HyperHide [VT debuger]

## Related

[[x64dbg]] · [[hyperdbg]] · [[vt-debuger]] · [[titanhide]] · [[scyllahide-for-ida9.0rc]] · [[anti-anti-debugger-driver]] · [[scyllahidedetector2]] · [[kdbgdecryptor]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
