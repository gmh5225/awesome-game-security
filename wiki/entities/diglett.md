---
title: Diglett
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Rwkeith__Diglett.md
updated: 2026-08-21
confidence: medium
---

# Diglett

Windows **kernel-mode stealth proof of concept** (Rwkeith) focused on **thread-related hiding**: concealing system threads and altering **thread entry-address visibility** characteristics. The repository ships both **driver** and **client** components that demonstrate low-level control and kernel–user communication patterns. Mainly useful for anti-cheat evasion research and for defenders studying kernel-thread detection blind spots. (source: wiki/sources/descriptions/Rwkeith__Diglett.md)

README tag: **Hide Kernel Thread**. Offensive hide lane adjacent to [[driver-hide-kernel-thread-iocancelirp]], [[zero-thread-kernel]], [[covert-thread]], and [[driver-systemthread-from-pspcidtable-src]]; defensive counterparts include [[nomad]], [[system-thread-finder]], [[unkover]], and [[kernel-anti-cheat]].

## Links

- Repo: https://github.com/Rwkeith/Diglett [Hide Kernel Thread]

## Related

[[nomad]] · [[driver-hide-kernel-thread-iocancelirp]] · [[zero-thread-kernel]] · [[system-thread-finder]] · [[unkover]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
