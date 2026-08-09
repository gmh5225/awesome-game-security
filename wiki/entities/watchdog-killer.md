---
title: WatchDogKiller
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__WatchDogKiller.md
updated: 2026-08-09
confidence: medium
---

# WatchDogKiller

Focused EDR/AV terminator PoC that weaponizes the WatchDog Anti-Malware **`amsdk.sys`** or **`wamsdk.sys`** BYOVD flaw. The tool opens `\\.\amsdk` or the guard device GUID, optionally bypasses authorization by registering its own PID via `IOCTL_REGISTER_PROCESS` (`0x80002010`), then submits `IOCTL_TERMINATE_PROCESS` (`0x80002048`) with a target PID and wait flag. README ties the technique to Silver Fox tradecraft research; the tested WatchDog build was reportedly still absent from common vulnerable-driver and HVCI blocklists at publication. (source: wiki/sources/descriptions/gmh5225__WatchDogKiller.md)

## Links

- Repo: https://github.com/gmh5225/WatchDogKiller

## Related

[[byovd]] · [[av-edr-killer]] · [[phantomkiller]] · [[zam64-zemina]] · [[windows-kernel-exploits]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
