---
title: CEDetector
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/weak1337__CEDetector.md
updated: 2026-07-18
confidence: medium
---

# CEDetector

User-mode detection sample that identifies running **Cheat Engine** instances via known window classes, process names, driver presence, and debug artifacts (`FindWindow`, `CreateToolhelp32Snapshot`, service enumeration). The `ce_detection` module stacks multiple vectors so CE remains detectable after rename or with anti-detection features enabled. Useful for anti-cheat developers studying CE fingerprints and researchers validating CE stealth configs. (source: wiki/sources/descriptions/weak1337__CEDetector.md)

Complements CE-facing memory protection such as [[no-access-protection]] (`PAGE_NOACCESS` + VEH vs external scanners) under the same Cheat Engine research lane.

## Links

- Repo: https://github.com/weak1337/CEDetector

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[no-access-protection]]
