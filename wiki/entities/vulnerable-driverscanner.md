---
title: VulnerableDriverScanner
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Sentient111__VulnerableDriverScanner.md
updated: 2026-08-21
confidence: medium
---

# VulnerableDriverScanner

Windows driver triage utility that scans folders for potentially risky kernel drivers. Implemented as a C++ console application that parses PE imports and flags binaries containing selected driver-related APIs. Detection logic is intentionally simple—indicative imports rather than full behavioral analysis—useful for preliminary vulnerable-driver hunting and kernel attack-surface assessment in security research workflows. (source: wiki/sources/descriptions/Sentient111__VulnerableDriverScanner.md)

## Links

- Repo: https://github.com/Sentient111/VulnerableDriverScanner

## Related

[[byovd]] · [[vulnerable-driver-scanner]] · [[driver-risk-scout]] · [[loldrivers]] · [[ms-vulnerable-driver-list]] · [[byovdfinder]] · [[overviews/windows-kernel]]
