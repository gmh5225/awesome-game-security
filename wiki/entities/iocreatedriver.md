---
title: IoCreateDriver
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Th3Spl__IoCreateDriver.md
updated: 2026-08-20
confidence: medium
---

# IoCreateDriver

Custom **IoCreateDriver** implementation for Windows kernel experimentation. Written in **C/C++** for Visual Studio and WDK workflows, with notes for manual-mapping setups and driver entry-point adjustments. Highlights techniques intended to avoid standard driver-load visibility paths, including bypassing common logging points. (source: wiki/sources/descriptions/Th3Spl__IoCreateDriver.md)

Aimed at low-level Windows internals and **anti-cheat evasion research** — complements manual-map mappers such as [[umap]] and [[kdmapper]], load-artifact forensics (PiDDBCache, MmUnloadedDrivers), and other Th3Spl pre-OS tooling such as [[simpleuefi]].

## Links

- Repo: https://github.com/Th3Spl/IoCreateDriver

## Related

[[simpleuefi]] · [[umap]] · [[kdmapper]] · [[map-file-in-system-space]] · [[known-driver-mappers]] · [[kernel-pool-scanning]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
