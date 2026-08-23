---
title: IAT Obfuscation
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/MahmoudZohdy__IAT-Obfuscation.md
updated: 2026-08-23
confidence: medium
---

# IAT Obfuscation

C++ **Windows PE import obfuscation** tool (MahmoudZohdy). Rewrites Import Address Table entries by swapping imported functions within the same DLL, making static API-sequence analysis harder. A companion TLS-based header restores correct import behavior at runtime before the program's main logic executes. Primary use: educational security research into import-hiding techniques and their impact on malware analysis workflows. (source: wiki/sources/descriptions/MahmoudZohdy__IAT-Obfuscation.md)

README lane: **IAT Obfuscation** — same-DLL IAT swap + TLS pre-main restore for static import-sequence obfuscation study.

Complements decoy-IAT approaches such as [[call-obfuscator]], post-compile PE obfuscators such as [[alcatraz]], and title-specific IAT repair tooling such as [[overwatch-iat-fixer]] and [[wow-iat-fix]]. Same author as [[process-injection-techniques]].

## Links

- Repo: https://github.com/MahmoudZohdy/IAT-Obfuscation

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[call-obfuscator]] · [[alcatraz]] · [[process-injection-techniques]] · [[overwatch-iat-fixer]] · [[wow-iat-fix]]
