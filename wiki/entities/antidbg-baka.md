---
title: Baka (antidbg-Baka)
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__antidbg-Baka.md
updated: 2026-08-09
confidence: medium
---

# Baka (antidbg-Baka)

Windows **anti-debugging library** (C/C++) implementing multiple debugger-detection primitives: PEB flags, `NtQueryInformationProcess`, hardware breakpoints, timing checks, exception-based detection, and parent-process validation. Includes checks aimed at detecting ScyllaHide, HyperHide, and TitanHide hide plugins. Provides integratable anti-debug building blocks for software protection and security research on bypass methods. (source: wiki/sources/descriptions/gmh5225__antidbg-Baka.md)

Complements technique catalogs such as [[makin]] and [[anti-debugging]], hide-detection samples such as [[scyllahidedetector2]], and kernel hide drivers such as [[titanhide]].

## Links

- Repo: https://github.com/gmh5225/antidbg-Baka

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[makin]] · [[anti-debugging]] · [[scyllahidedetector2]] · [[titanhide]] · [[wubbaboomark]] · [[x64dbg]]
