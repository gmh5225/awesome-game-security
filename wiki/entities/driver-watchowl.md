---
title: Driver-WatchOwl
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-WatchOwl.md
updated: 2026-08-13
confidence: medium
---

# Driver-WatchOwl

Defensive Windows kernel driver that watches user-mode **image loads** and **thread creation**, then uses **stack-trace inspection** to flag suspicious mapping activity. (source: wiki/sources/descriptions/gmh5225__Driver-WatchOwl.md)

The driver registers `PsSetLoadImageNotifyRoutine` and `PsSetCreateThreadNotifyRoutine`, resolves expected user-mode frames such as `NtMapViewOfSection` and `RtlUserThreadStart` from `csrss.exe`, and validates whether image-load callbacks originated from legitimate module text ranges. When the observed stack does not match the expected mapping path, it logs the event and highlights lower-signing-level images — a compact **callback-based injection detection** sample rather than an offensive hook set. README lane: **ImageNotify+Stack Trace**. Useful for anti-cheat engineers and defensive kernel researchers studying stack-based validation of image mapping and suspicious user-mode code injection paths.

Complements kernel DLL thread injection detectors such as [[dll-thread-injection-detector]], multi-telemetry AC prototypes such as [[kernel-anti-cheat]], and the [[kernel-callbacks]] load-image notify surface.

## Links

- Repo: https://github.com/gmh5225/Driver-WatchOwl

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[kernel-callbacks]] · [[dll-thread-injection-detector]] · [[hidden-module-detector]] · [[kernel-anti-cheat]] · [[tietwagent]] · [[ghost]]
