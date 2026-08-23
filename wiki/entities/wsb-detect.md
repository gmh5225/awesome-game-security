---
title: wsb-detect
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/LloydLabs__wsb-detect.md
updated: 2026-08-23
confidence: medium
---

# wsb-detect

C library and sample program for detecting whether code is running inside **Windows Sandbox**. Implements multiple fingerprinting checks—sandbox-specific processes, usernames, device paths, DNS suffixes, registry artifacts, and timing clues—and exposes modular detection functions that can be combined depending on false-positive tolerance. Primary use case: anti-analysis research and environment awareness for malware studies, red-team simulation, and defensive countermeasure testing. (source: wiki/sources/descriptions/LloydLabs__wsb-detect.md)

Complements broader sandbox/VM testers such as [[pafish]], [[al-khaser]], and [[anti-sandbox]], plus compact VM fingerprinting such as [[compact-vm-detector]].

## Links

- Repo: https://github.com/LloydLabs/wsb-detect (README tag: Windows Sandbox ("WSB"))

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[pafish]] · [[al-khaser]] · [[anti-sandbox]] · [[compact-vm-detector]] · [[vmaware]]
