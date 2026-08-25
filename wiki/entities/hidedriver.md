---
title: HideDriver (ExpLife0011)
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ExpLife0011__HideDriver.md
updated: 2026-08-25
confidence: medium
---

# HideDriver (ExpLife0011)

**HideDriver** (ExpLife0011) is a **Windows x64 kernel driver-hiding proof of concept**. It uses **ETW-related symbol discovery** to locate **`MiProcessLoaderEntry`**, then removes **`DriverObject->DriverSection`** in a **[[patchguard]]-aware** way. A **separate cleanup thread** erases **driver-identifying artifacts** after load. Primary use case is **anti-cheat evasion research** and low-level study of **driver forensic footprints**. Listed with README tag `[Hide Driver By MiProcessLoaderEntry]`. (source: wiki/sources/descriptions/ExpLife0011__HideDriver.md)

Distinct from Flink/Blink unlink samples such as [[hide-driver]] (nbqofficial) — targets **loader-entry / `DriverSection` removal** rather than simple module-list unlink. Complements multi-artifact hide and trace-cleanup PoCs such as [[hide-driver-testing]], [[clear-driver-traces]], and [[drv-hide-and-camouflage]]. Same author lane as [[ntcomparesigninglevel-hook]] and [[keusermodecallback]].

## Links

- Repo: https://github.com/ExpLife0011/HideDriver

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[hide-driver]] · [[hide-driver-testing]] · [[clear-driver-traces]] · [[drv-hide-and-camouflage]] · [[patchguard]] · [[kernel-pool-scanning]] · [[ntcomparesigninglevel-hook]] · [[keusermodecallback]] · [[openark]]
