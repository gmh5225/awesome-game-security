---
title: PsImageNotifyRoutineSpamFilter
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Staatsgeheim__PsImageNotifyRoutineSpamFilter.md
updated: 2026-08-20
confidence: medium
---

# PsImageNotifyRoutineSpamFilter

Windows kernel utility that **filters noisy `PsImageNotifyRoutine` callback events** so load-image notify handlers see fewer spurious firings. (source: wiki/sources/descriptions/Staatsgeheim__PsImageNotifyRoutineSpamFilter.md)

The implementation uses **`RtlWalkFrameChain` stack walking** to distinguish meaningful image-load notifications from common background noise sources. Written in C for 64-bit Windows driver development, it demonstrates practical **callback hygiene** for kernel monitoring pipelines, anti-cheat telemetry collection, and cleaner driver-side event analysis. README lane: **ImageNotify Callback With RtlWalkFrameChain**.

Complements defensive stack-trace validators such as [[driver-watchowl]], callback enumeration via [[windbg-extensions]], and the broader [[kernel-callbacks]] load-image notify surface. Contrasts with offensive notify-routine removal tools such as [[ps-notif-routine-unloader]].

## Links

- Repo: https://github.com/Staatsgeheim/PsImageNotifyRoutineSpamFilter

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[kernel-callbacks]] · [[driver-watchowl]] · [[windbg-extensions]] · [[ps-notif-routine-unloader]] · [[stack-spoofing]]
