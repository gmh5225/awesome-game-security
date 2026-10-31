---
title: Anticheat Lab (senolbasyigit)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/senolbasyigit__anticheat-lab.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# Anticheat Lab (senolbasyigit)

**Anticheat-lab** (senolbasyigit/anticheat-lab) is a **Claude Code skill** and Python toolkit for tamper-testing your own game builds before release by scanning process memory for exposed values such as health, ammo, or currency, then documenting findings with server-side defense recommendations and regression tests. It implements a Cheat Engine-style workflow on Windows through scan, next-scan filtering, and read/write helpers backed by a **devbuild.json** SHA-256 guard that only permits work on verified developer executables you own. A separate RPA mode automates third-party Windows applications via exports, APIs, or UI Automation with **pywinauto** without reading their memory. Reference guides cover defense priorities from server authority and delta validation through telemetry and integrity signals, with client obfuscation as a secondary measure. (source: wiki/sources/descriptions/senolbasyigit__anticheat-lab.md)

## Distinction

Not to be confused with [[anticheat-lab]] (Ogonx)—six-month VM self-study on deliberately vulnerable multiplayer builds. This repo targets **pre-ship memory exposure audits** on owned dev binaries plus optional RPA automation.

## Links

- Repo: https://github.com/senolbasyigit/anticheat-lab

## Related

[[anticheat-lab]] · [[anticheat-qa]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
