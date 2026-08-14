---
title: BYOVD Lab
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__BYOVD.md
updated: 2026-08-14
confidence: medium
---

# BYOVD Lab

Curated **educational BYOVD lab** from gmh5225: proof-of-concepts showing how multiple signed vulnerable drivers can be abused to terminate or disable AV and EDR components. Subprojects include dedicated kill routines for **`viragt64.sys`**, TfSysMon, ksapi64, BdApiUtil, and **`wsftprm.sys`**. The Viragt64 branch documents that its PoC was published after similar driver abuse started appearing in real-world campaigns—useful operational context for mapping public PoCs to drivers later seen in the wild. (source: wiki/sources/descriptions/gmh5225__BYOVD.md)

## Subprojects (indexed)

- **Viragt64-Killer** — `viragt64.sys` process-kill lane; overlaps standalone [[process-killer-byovd]] and README entry for [Viragt64-Killer](https://github.com/gmh5225/BYOVD/tree/main/Viragt64-Killer).
- **wsftprm.sys** — same backend family as [[av-edr-killer]] (IOCTL `0x22201C` PID kill).

## Links

- Repo: https://github.com/gmh5225/BYOVD
- Viragt64-Killer: https://github.com/gmh5225/BYOVD/tree/main/Viragt64-Killer

## Related

[[concepts/byovd]] · [[process-killer-byovd]] · [[av-edr-killer]] · [[terminator]] · [[watchdog-killer]] · [[blackout]] · [[win-driver-exp]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
