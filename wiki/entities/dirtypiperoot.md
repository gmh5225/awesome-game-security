---
title: DirtyPipeRoot
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/tiann__DirtyPipeRoot.md
updated: 2026-07-20
confidence: medium
---

# DirtyPipeRoot

Android app that exploits Dirty Pipe (CVE-2022-0847) for one-click **temporary root** on Pixel 6 devices with vulnerable kernels. Bundles a vulnerability checker and a native C exploit that overwrites read-only files via Linux pipe page-cache corruption. (source: wiki/sources/descriptions/tiann__DirtyPipeRoot.md)

Useful for mobile game-security research on the Cheat Android Kernel CVE / Root lane: device-scoped LPE packaging, temporary (non-persistent) root vs Magisk/[[kernelsu]] frameworks, and how pipe page-cache bugs widen privilege windows for further instrumentation.

## Links

- Repo: https://github.com/tiann/DirtyPipeRoot
- CVE: CVE-2022-0847

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[kernelsu]] · [[cheese]] · [[cve-2026-43499-popsicle]] · [[magisk]]
