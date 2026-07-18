---
title: BYOVD
kind: concept
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/xct__windows-kernel-exploits.md
  - wiki/sources/descriptions/xM0kht4r__VEN0m-Ransomware.md
  - wiki/sources/descriptions/xM0kht4r__AV-EDR-Killer.md
updated: 2026-07-18
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

Educational kernel-exploit reference material such as [[windows-kernel-exploits]] sits in the same cheat / vulnerable-driver documentation lane. (source: wiki/sources/descriptions/xct__windows-kernel-exploits.md)

Concrete AV/EDR-evasion research such as [[ven0m-ransomware]] abuses `iMFForceDelete.sys` from IObit Malware Fighter (v12.1.0) rather than a classic ZwTerminateProcess-style killer driver. (source: wiki/sources/descriptions/xM0kht4r__VEN0m-Ransomware.md)

Process-terminate style killers such as [[av-edr-killer]] target `wsftprm.sys` via IOCTL `0x22201C` (1036-byte buffer; first DWORD = target PID). (source: wiki/sources/descriptions/xM0kht4r__AV-EDR-Killer.md)

## Related

[[kernel-callbacks]] · [[hvci]] · [[patchguard]] · [[windows-kernel-exploits]] · [[ven0m-ransomware]] · [[av-edr-killer]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
