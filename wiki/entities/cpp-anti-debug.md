---
title: cpp-anti-debug
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/BaumFX__cpp-anti-debug.md
updated: 2026-08-31
confidence: medium
---

# cpp-anti-debug

Windows **C++ anti-debugging library** from BaumFX that aggregates many debugger-detection checks in one integratable package. Coverage spans **PEB and WinAPI-based probes**, **exception-driven tricks**, **timing measurements**, and **CPU/debug-register tests**. Ships both granular per-check functions and a combined **security-check entry point** for repeated runtime validation. Primary use case is anti-tamper prototyping and studying debugger-detection techniques rather than shipping as production anti-cheat. (source: wiki/sources/descriptions/BaumFX__cpp-anti-debug.md)

Complements broader technique catalogs such as [[al-khaser]] and [[antidbg-hackovert]], syscalled libraries such as [[antidbg]], modular anti-analysis kits such as [[dynamizer]], and anti-tamper frameworks such as [[anti-crack-system]].

## Links

- Repo: https://github.com/BaumFX/cpp-anti-debug

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[al-khaser]] · [[antidbg-hackovert]] · [[antidbg]] · [[makin]] · [[anti-debugging]] · [[showstopper]] · [[dynamizer]]
