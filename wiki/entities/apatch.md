---
title: APatch
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/bmax121__APatch.md
updated: 2026-08-17
confidence: medium
---

# APatch

Android root framework that **patches the Android kernel and system** via the [[kernelpatch]] boot-image patch path on stock GKI devices — no custom kernel source required. **SuperKey** grants privileges above conventional root (`su`). Listed under Cheat / Android root for game-security researchers and reverse engineers studying offensive cheat and Android-root techniques. (source: wiki/sources/descriptions/bmax121__APatch.md)

KernelPatch Module (**KPM**) collections such as [[apatch-kpm]], [[kpm-memreader]], and [[mkpms]] extend APatch at kernel scope — same module lane referenced in title RE such as [[honor-of-kings-re-research]] (`acepeek`). Module-ecosystem peers include [[move-certificate]], [[florida-zygisk]], [[root-socket-kit]], [[rescuex]], and [[baize]] (Magisk/KernelSU/APatch-compatible).

## Links

- Repo: https://github.com/bmax121/APatch

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelpatch]] · [[apatch-kpm]] · [[kernelsu]] · [[magisk]] · [[kpm-memreader]] · [[mkpms]] · [[honor-of-kings-re-research]] · [[mobile-anti-cheat]]
