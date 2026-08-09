---
title: ezDrvBAK
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__ezDrvBAK.md
updated: 2026-08-09
confidence: medium
---

# ezDrvBAK

Windows kernel **driver backup and restore** utility from gmh5225. Centers on driver development workflows: snapshot installed or in-development `.sys` images and roll back to a known-good copy after load, mapping, or AC stress tests. (source: wiki/sources/descriptions/gmh5225__ezDrvBAK.md)

Useful for anti-cheat engineers and defensive security researchers who need repeatable driver-store baselines when studying load telemetry, PiDDB/MmUnloadedDrivers forensics, or BYOVD lab hygiene without manual file copying.

## Links

- Repo: https://github.com/gmh5225/ezDrvBAK

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[nullmap]] · [[revert-mapper]] · [[kernel-pool-scanning]] · [[byovd]]
