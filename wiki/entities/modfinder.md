---
title: ModFinder
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Nou4r__ModFinder.md
updated: 2026-08-22
confidence: medium
---

# ModFinder

Windows **C++ utility** from **Nou4r** that locates **manually mapped modules** in process memory during runtime investigations. Enumerates mapped memory regions and applies **DOS-header / PE heuristics** to flag suspicious injections, including cases where parts of optional headers are stripped. Native Visual Studio project layout with practical focus on **x86 process analysis**; primary use case is anti-cheat and malware-oriented **memory forensics**. (source: wiki/sources/descriptions/Nou4r__ModFinder.md)

Complements working-set page-fault detectors such as [[faultline]], hidden-module scanners such as [[hidden-module-detector]], and live injection engines such as [[pe-sieve]] / [[xmalhunter]]. Sits opposite offensive manual-map injectors such as [[modexmap]] and [[simple-manual-map-injector]] in the Mapped Dll research lane.

## Detection approach

| Signal | Method |
|--------|--------|
| **Unlisted modules** | Walk mapped regions outside PEB module lists |
| **PE fingerprints** | Match DOS-header (`MZ`) patterns in executable mappings |
| **Header tampering** | Heuristics for stripped or partial optional headers |

## Links

- Repo: https://github.com/Nou4r/ModFinder (README tag: Mapped Dll)

## Related

[[faultline]] · [[hidden-module-detector]] · [[dll-thread-injection-detector]] · [[pe-sieve]] · [[xmalhunter]] · [[modexmap]] · [[simple-manual-map-injector]] · [[present-injector]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
