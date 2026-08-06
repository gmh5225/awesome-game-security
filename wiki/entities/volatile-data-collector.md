---
title: Volatile Data Collector
kind: entity
topics: [reverse-engineering, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gtworek__VolatileDataCollector.md
updated: 2026-08-06
confidence: medium
---

# Volatile Data Collector

Collection of lightweight **Windows C** utilities for gathering **volatile system state** during incident response. Each artifact type is a standalone program—handles, loaded kernel modules, user sessions, driver information, ICMP connections, and registry settings—so analysts can run only the collectors they need without a monolithic triage bundle. (source: wiki/sources/descriptions/gtworek__VolatileDataCollector.md)

Useful for forensic analysts and security researchers who need granular live host snapshots before offline memory or disk analysis ([[dumpit-mirror]], [[volatility3]]) or alongside scripted triage such as [[dfirtriage]].

## Links

- Repo: https://github.com/gtworek/VolatileDataCollector

## Related

[[dfirtriage]] · [[dumpit-mirror]] · [[volatility]] · [[volatility3]] · [[systeminformer]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
