---
title: ShadowStackWalk
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gabriellandau__ShadowStackWalk.md
updated: 2026-08-15
confidence: medium
---

# ShadowStackWalk

Defensive stack-walk implementation that uses Intel CET shadow-stack data (HSP) alongside conventional `CaptureStackBackTrace` / `StackWalk64` paths to detect **thread stack spoofing**. When CET is enabled, the shadow stack holds hardware-enforced return addresses; comparing shadow-stack contents against the visible call stack exposes spoofed frames that pass naive unwind walks. Aimed at anti-cheat engineers and defensive security researchers in the `Detection:Spoof Stack` lane. (source: wiki/sources/descriptions/gabriellandau__ShadowStackWalk.md)

Complements query-oriented CET PoCs such as [[query-shadow-stack]] and KM shadow-stack analysis such as [[windows-kernel-shadow-stack]] when modeling hardware-backed return-address integrity checks against offensive [[stack-spoofing]] techniques.

## Links

- Repo: https://github.com/gabriellandau/ShadowStackWalk

## Related

[[stack-spoofing]] · [[query-shadow-stack]] · [[cet-research]] · [[cet-win10]] · [[windows-kernel-shadow-stack]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
