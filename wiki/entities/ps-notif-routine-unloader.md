---
title: PsNotifRoutineUnloader
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__PsNotifRoutineUnloader.md
updated: 2026-08-10
confidence: medium
---

# PsNotifRoutineUnloader

Windows kernel tool that **removes process, thread, and image-load notification callbacks** registered by anti-cheat and security drivers. It enumerates the `PsSetCreateProcessNotifyRoutine` callback array and selectively unloads entries belonging to chosen drivers—blinding those drivers to process-creation (and related) events. Aimed at kernel researchers studying [[kernel-callbacks]] manipulation for anti-cheat evasion and defensive callback protection. (source: wiki/sources/descriptions/gmh5225__PsNotifRoutineUnloader.md)

README tags the project with **`RTCore64.sys`** (MSI Afterburner white-signed BYOVD lane). Related offensive callback removal: [[rtoolz]], [[bustercall]], [[edrsandblast]]. Reference catalog: [[kernel-callback-functions-list]]. Same RTCore64 mapper research lane: [[rtcore64-vulnerability]].

## Links

- Repo: https://github.com/gmh5225/PsNotifRoutineUnloader [RTCore64.sys]

## Related

[[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[rtoolz]] · [[bustercall]] · [[edrsandblast]] · [[kernel-callback-functions-list]] · [[rtcore64-vulnerability]]
