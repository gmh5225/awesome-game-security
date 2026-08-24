---
title: Hidden
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/JKornev__hidden.md
updated: 2026-08-24
confidence: medium
---

# Hidden

Windows **kernel driver** with a **user-mode interface** for concealing selected system artifacts (JKornev). The C/C++ project hides **files**, **directories**, **registry keys**, and **processes**, and can **protect chosen processes from interference**. A **CLI** and **library** configure rules and exceptions; **WDK build scripts** support driver development. Targets **reverse-engineering labs** and **security research** scenarios that need **controlled environment masking**—not production anti-cheat evasion. (source: wiki/sources/descriptions/JKornev__hidden.md)

Offensive hide lane adjacent to process-hide samples such as [[blanket]], file-hide PoCs such as [[hide-file]], and multi-surface minifilter hide such as [[memfilter-fn-driver]]. Defensive counterparts include [[rootkit-2]], [[openark]], and [[volatility]] / [[volatility3]] offline enumeration gaps.

## Links

- Repo: https://github.com/JKornev/hidden

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[blanket]] · [[hide-file]] · [[memfilter-fn-driver]] · [[rootkit-2]] · [[openark]] · [[volatility]] · [[volatility3]]
