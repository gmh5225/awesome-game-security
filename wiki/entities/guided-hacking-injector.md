---
title: GuidedHacking Injector
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/guided-hacking__GuidedHacking-Injector.md
updated: 2026-08-06
confidence: medium
---

# GuidedHacking Injector

Feature-rich **Windows DLL injector** from Guided Hacking with a C++ **Qt GUI** for the `Injection Testing` lane. Supports LoadLibrary, manual mapping, thread hijacking, `NtCreateThreadEx`, QueueUserAPC, and kernel-mode injection via a vulnerable driver. Optional DLL cloaking covers PEB unlinking, header erasure, import resolution, TLS callback execution, and exception-handler registration. Aimed at game-hacking learners and security researchers studying injection tradecraft and its detection surface. (source: wiki/sources/descriptions/guided-hacking__GuidedHacking-Injector.md)

Complements technique catalogs such as [[windows-process-injection]], focused manual-map samples such as [[modexmap]] and [[shtreeba]], kernel APC inject paths such as [[injdrv]] / [[kinject]], and the Broihon C++ inject library [[gh-injector-library]] (Ldr/manual-map loaders, multi-method execution, cloaking, .NET assembly load).

## Links

- Repo: https://github.com/guided-hacking/GuidedHacking-Injector

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[gh-injector-library]] · [[injectors]] · [[windows-process-injection]] · [[modexmap]] · [[shtreeba]] · [[intro-to-gamehacking]]
