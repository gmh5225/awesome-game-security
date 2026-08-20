---
title: NotifyRoutineHijackThread
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/UCFoxi__NotifyRoutineHijackThread.md
updated: 2026-08-20
confidence: medium
---

# NotifyRoutineHijackThread

Compact Visual Studio C++ kernel proof of concept (UCFoxi) demonstrating **notify-routine hijacking via a dedicated thread**. Targets **`PspCreateThreadNotifyRoutine`** callback manipulation at low level: a minimal driver sample plus a short showcase for the technique flow. Intended for Windows kernel internals study and anti-cheat or EDR evasion research around [[kernel-callbacks]] blind spots. (source: wiki/sources/descriptions/UCFoxi__NotifyRoutineHijackThread.md)

Offensive notify-routine lane neighbors include selective unloaders such as [[ps-notif-routine-unloader]] and integrated callback tools such as [[rtoolz]] and [[bustercall]]; hide-callback codecave samples such as [[mapped-callback]] illustrate adjacent start-address obfuscation tactics.

## Links

- Repo: https://github.com/UCFoxi/NotifyRoutineHijackThread [Hijack PspCreateThreadNotifyRoutine]

## Related

[[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[ps-notif-routine-unloader]] · [[mapped-callback]] · [[bustercall]] · [[rtoolz]] · [[shared-flushfilebuffers-communication]]
