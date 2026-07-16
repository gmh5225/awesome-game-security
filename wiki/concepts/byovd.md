---
title: BYOVD
kind: concept
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/skills/game-hacking.md
updated: 2026-07-16
confidence: high
---

# BYOVD

Bring Your Own Vulnerable Driver: load a legitimately signed but vulnerable driver to obtain kernel read/write (or other primitives), then disable protections, map unsigned code, or blind anti-cheat. (source: wiki/sources/skills/windows-kernel.md)

## Typical chain

1. Load signed vulnerable driver (e.g. historically abused families like Capcom, RTCore, iqvw64e, dbutil, …)
2. Trigger vulnerable IOCTL / bug for arbitrary R/W
3. Tamper with DSE, callbacks, ETW, or load a hostile mapper

## Mitigations

Microsoft vulnerable-driver blocklist, [[hvci]], AC driver allowlists ([[vanguard]]-style), PiDDBCache/MmUnloadedDrivers forensics, EPT-protected callback lists.

## Related

[[kernel-callbacks]] · [[hvci]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
