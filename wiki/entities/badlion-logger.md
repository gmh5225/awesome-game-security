---
title: badlion-logger
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/KiFilterFiberContext__BadlionLogger.md
updated: 2026-08-23
confidence: medium
---

# badlion-logger

Proof-of-concept **kernel logger** for observing a game **anti-cheat driver** at runtime. Applies **IAT hooks** during **image-load callbacks** to monitor behavior in a black-box manner, specifically against a **VMProtect-virtualized** target module. Implementation is mainly **C++**, focused on kernel callback handling and instrumentation rather than production robustness. Intended for anti-cheat research and educational study of driver-level monitoring techniques. (source: wiki/sources/descriptions/KiFilterFiberContext__BadlionLogger.md)

Complements user-mode IAT trace tooling such as [[kn-win32-api-monitor]] and defensive hook analysis such as [[nt-unhooker]], but operates from the kernel **load-image notify** path documented in [[kernel-callbacks]].

## Links

- Repo: https://github.com/KiFilterFiberContext/BadlionLogger

## Related

[[kernel-callbacks]] · [[windows-software-policy]] · [[kn-win32-api-monitor]] · [[nt-unhooker]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
