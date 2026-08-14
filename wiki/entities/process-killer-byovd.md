---
title: Process Killer BYOVD
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__ProcessKiller-BYOVD.md
  - wiki/sources/descriptions/gmh5225__BYOVD.md
updated: 2026-08-14
confidence: medium
---

# Process Killer BYOVD

Windows BYOVD tool that terminates protected processes—anti-cheat services, EDR agents, and antivirus—that resist standard user-mode termination APIs because of kernel-level protections. It loads the signed vulnerable driver **`viragt64.sys`** to gain kernel access and uses that primitive to forcefully kill target processes. Also indexed as the **Viragt64-Killer** subproject inside the gmh5225 [[entities/byovd|BYOVD Lab]] collection. Aimed at red-team operators and security researchers studying BYOVD-based process termination. (source: wiki/sources/descriptions/gmh5225__ProcessKiller-BYOVD.md) (source: wiki/sources/descriptions/gmh5225__BYOVD.md)

## Links

- Repo: https://github.com/gmh5225/ProcessKiller-BYOVD

## Related

[[concepts/byovd]] · [[entities/byovd|BYOVD Lab]] · [[terminator]] · [[watchdog-killer]] · [[av-edr-killer]] · [[phantomkiller]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
