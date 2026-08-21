---
title: ClearDriverTraces
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Sentient111__ClearDriverTraces.md
updated: 2026-08-21
confidence: medium
---

# ClearDriverTraces

Windows kernel driver for removing forensic traces left by loading other drivers. C++ kernel-mode routines target structures such as **MmUnloadedDrivers**, **PiDDBCacheTable**, and code-integrity hash caches via version-specific offsets and low-level kernel data structure manipulation. Primarily used in anti-cheat and driver forensics research to study what artifacts are created and how detection logic can track them. (source: wiki/sources/descriptions/Sentient111__ClearDriverTraces.md)

## Links

- Repo: https://github.com/Sentient111/ClearDriverTraces

## Related

[[hide-driver-testing]] · [[driver-read-write]] · [[nullmap]] · [[revert-mapper]] · [[hlunaaa-github-io]] · [[kernel-pool-scanning]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
