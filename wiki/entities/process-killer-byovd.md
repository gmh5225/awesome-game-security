---
title: Process Killer BYOVD
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__ProcessKiller-BYOVD.md
updated: 2026-08-10
confidence: medium
---

# Process Killer BYOVD

Windows BYOVD tool that terminates protected processes—anti-cheat services, EDR agents, and antivirus—that resist standard user-mode termination APIs because of kernel-level protections. It loads the signed vulnerable driver **`viragt64.sys`** to gain kernel access and uses that primitive to forcefully kill target processes. Aimed at red-team operators and security researchers studying BYOVD-based process termination. (source: wiki/sources/descriptions/gmh5225__ProcessKiller-BYOVD.md)

## Links

- Repo: https://github.com/gmh5225/ProcessKiller-BYOVD

## Related

[[byovd]] · [[terminator]] · [[watchdog-killer]] · [[av-edr-killer]] · [[phantomkiller]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
