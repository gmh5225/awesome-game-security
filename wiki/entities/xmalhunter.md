---
title: xMalHunter
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/push0ebp__xMalHunter.md
updated: 2026-07-25
confidence: medium
---

# xMalHunter

Malware / injection detection tool that links **[[pe-sieve]]** and **libpeconv** to scan running Windows processes (32-bit and 64-bit) for in-memory artifacts: injected code, inline hooks, and hollowed modules. README lane: Detect malicious materials. Useful for malware analysts and anti-cheat researchers studying runtime code-injection detection and process integrity verification. Complements hook-integrity research such as [[hook-buster]] and manual-map / working-set monitors such as [[faultline]]. (source: wiki/sources/descriptions/push0ebp__xMalHunter.md)

## Links

- Repo: https://github.com/push0ebp/xMalHunter

## Related

[[pe-sieve]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[hook-buster]] · [[faultline]] · [[injectors]]
