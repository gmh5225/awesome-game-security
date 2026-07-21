---
title: anti-emulator
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/strazzere__anti-emulator.md
updated: 2026-07-21
confidence: medium
---

# anti-emulator

Android emulator detection library (Java) that scores common emulator artifacts: QEMU-specific system properties, generic hardware identifiers, operator names, build fingerprints, sensor availability, and filesystem signatures. Exposes a simple API returning per-heuristic results so apps can tell physical device vs emulated environment. Aimed at Android security researchers and developers implementing emulator detection for anti-cheat, anti-fraud, or DRM. (source: wiki/sources/descriptions/strazzere__anti-emulator.md)

README lane: `[Android Anti-Emulator]` — sits with mobile RASP / VE probes such as [[droidshield]], [[conbeerlib]], and `Detection:Virtual Environments` refs like [[anticuckoo]] / [[awesome-anti-virtualization]].

## Links

- Repo: https://github.com/strazzere/anti-emulator

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[droidshield]] · [[conbeerlib]] · [[anticuckoo]] · [[awesome-anti-virtualization]]
