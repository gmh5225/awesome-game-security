---
title: IntaktoFT
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/IntaktoFT__IntaktoFT.md
  - wiki/sources/README-categories.md
updated: 2026-11-25
confidence: medium
---

# IntaktoFT

Free, open-source Android runtime application self-protection (RASP) library: Kotlin SDK plus native C++ checks for repackaged or tampered installs and live instrumentation such as [[frida]] hooks and common mod frameworks. Native probes cover app integrity, memory-resident agents, GOT/PLT integrity, opcode trampolines, and related signals; each rolls up to **CLEAN**, **DETECTED**, or **INCONCLUSIVE** results delivered to app code without forced process exit and without shipping device data to a vendor backend. (source: wiki/sources/descriptions/IntaktoFT__IntaktoFT.md)

## Integration

Gradle + JitPack dependency; automatic checks at startup. Optional Unity C# package targets Android games. Apache 2.0. Aimed at indie developers and game studios needing client-side anti-mod and anti-cheat style protection against off-the-shelf cheating and repackaging tools.

## Architecture

Kotlin API surface over CMake/NDK native integrity and instrumentation detection—same evidence classes as [[blackhex]] and [[rootect]] (GOT/PLT, trampolines, hook agents) but policy emphasizes callback tri-state reporting over vendor kill-switch telemetry.

## Related

[[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[blackhex]] · [[mobshield-android]] · [[rootect]] · [[frida]]

## Links

- Repo: https://github.com/IntaktoFT/IntaktoFT