---
title: MAJESTY-technologies
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Ahora57__MAJESTY-technologies.md
updated: 2026-09-03
confidence: medium
---

# MAJESTY-technologies

Experimental **Windows kernel driver** focused on **anti-debugging and anti-analysis** protections at Ring0. Uses low-level C/C++ techniques including **DKOM-style structure manipulation**, **instrumentation callback checks**, **hardware breakpoint checks**, and **process/thread flag hardening**. Also explores **anti-hypervisor timing and anomaly checks** while documenting planned kernel-user communication features. Intended for **anti-cheat and protection research** studying kernel-level detection and debugger resistance. (source: wiki/sources/descriptions/Ahora57__MAJESTY-technologies.md)

Same author lane as offensive anti-anti-debug PoC [[racecondition]]; defensive counterpart to tutorial hide drivers such as [[anti-anti-debugger-driver]] and hypervisor-based hides such as [[hyperhide]]; complements kernel debugger-detection PoCs such as [[anti-kernel-debug-poc]].

## Technique

- DKOM-style kernel structure manipulation
- Instrumentation callback and hardware breakpoint checks
- Process/thread flag hardening
- Anti-hypervisor timing and anomaly probes (experimental)

## Links

- Repo: https://github.com/Ahora57/MAJESTY-technologies

## Related

[[racecondition]] · [[anti-kernel-debug-poc]] · [[anti-anti-debugger-driver]] · [[titanhide]] · [[hyperhide]] · [[makin]] · [[showstopper]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
