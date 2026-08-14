---
title: Blackout
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Blackout.md
updated: 2026-08-14
confidence: medium
---

# Blackout

Kernel-mode BYOVD tool that loads the signed GMER anti-rootkit driver **`gmer64.sys`** (sourced from [[loldrivers]]) and issues IOCTL calls to disable or terminate EDR and AV processes by PID. Includes continuous Windows Defender suppression to prevent the service from restarting after kill—overlapping the AV-control research lane with tools such as [[windefctl]]. Aimed at red-team operators and security researchers studying LOLdriver-based security-product termination. (source: wiki/sources/descriptions/gmh5225__Blackout.md)

## Links

- Repo: https://github.com/gmh5225/Blackout

## Related

[[byovd]] · [[loldrivers]] · [[terminator]] · [[av-edr-killer]] · [[watchdog-killer]] · [[process-killer-byovd]] · [[windefctl]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
