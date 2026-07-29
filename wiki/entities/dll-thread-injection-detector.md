---
title: DLLThreadInjectionDetector
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/mq1n__DLLThreadInjectionDetector.md
updated: 2026-07-29
confidence: medium
---

# DLLThreadInjectionDetector

C/C++ **DLL thread injection detector** with **kernel-level** components — listed under **Anti Cheat → Detection:Injection** for anti-cheat engineers and defensive security researchers studying remote DLL loads and worker threads created by injection or manual-map loaders. (source: wiki/sources/descriptions/mq1n__DLLThreadInjectionDetector.md)

Same **mq1n** author lane as [[hidden-module-detector]] (Detection:Hide) and OSS AC reference [[no-mercy]]. Complements thread-enumeration heuristics such as [[system-thread-finder]] and offensive inject samples cataloged under [[windows-process-injection]].

## Links

- Repo: https://github.com/mq1n/DLLThreadInjectionDetector

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hidden-module-detector]] · [[no-mercy]] · [[system-thread-finder]] · [[windows-process-injection]] · [[injectors]] · [[injdrv]]
