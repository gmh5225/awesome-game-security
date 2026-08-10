---
title: StealthSytemThreadFinderBE
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__StealthSytemThreadFinderBE.md
updated: 2026-08-10
confidence: medium
---

# StealthSytemThreadFinderBE

Tool for finding **hidden system threads** that [[battleye]]’s anti-cheat cannot detect. Goes beyond standard API enumeration with kernel-internal techniques such as **PspCidTable walking**, **scheduler queue scanning**, and **cross-referencing thread lists** to locate stealth threads spawned by manually mapped drivers. Aimed at AC researchers studying thread hiding and detection gaps relative to BE’s thread visibility. (source: wiki/sources/descriptions/gmh5225__StealthSytemThreadFinderBE.md)

Complements BE-derived heuristics in [[system-thread-finder]] (`NtQuerySystemInformation` + start-address vs loaded-driver image checks) and evasion PoCs such as [[zero-thread-kernel]] that avoid creating visible system threads.

## Links

- Repo: https://github.com/gmh5225/StealthSytemThreadFinderBE

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[battleye]] · [[system-thread-finder]] · [[zero-thread-kernel]] · [[dll-thread-injection-detector]] · [[hidden-module-detector]]
