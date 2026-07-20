---
title: CVEAC-2020
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/thesecretclub__CVEAC-2020.md
updated: 2026-07-20
confidence: medium
---

# CVEAC-2020

Proof-of-concept Windows kernel driver (C++ / WDK) that exploits a vulnerability in Easy Anti-Cheat’s kernel module. Includes EAC-specific analysis, kernel module enumeration, PE parsing, hook installation, and NMD assembly for runtime code manipulation—useful for researchers studying EAC driver integrity and AC bypass surfaces, not a product. Listed under README Integrity Checks. (source: wiki/sources/descriptions/thesecretclub__CVEAC-2020.md)

## Links

- Repo: https://github.com/thesecretclub/CVEAC-2020

## Related

[[easy-anti-cheat]] · [[eac-overlay]] · [[kernel-callbacks]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
