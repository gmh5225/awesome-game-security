---
title: Ow-Anti-Flag
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/dword64__Ow-Anti-Flag.md
updated: 2026-08-16
confidence: medium
---

# Ow-Anti-Flag

**Ow-Anti-Flag** (dword64) is a modern C++ console application that attempts to prevent Blizzard **chainbans** by clearing common directories and registry keys used to **flag** a device—whether from prior cheat use or from malware disguised as Overwatch cheats. Listed in the cheat / HWID lane; aimed at game security researchers and reverse engineers studying offensive persistence and artifact cleanup around hardware bans rather than kernel serial spoofing. (source: wiki/sources/descriptions/dword64__Ow-Anti-Flag.md)

Sits beside other dword64 Overwatch samples such as [[ow-fov]] (FOV changer) and broader client telemetry cleanup such as [[hwid-steam-spyware-terminator]] (Steam hardware fingerprint blocking). Contrasts with kernel HWID spoofers like [[hwid-spoofer]] that rewrite disk/NIC/SMBIOS identifiers instead of scrubbing flag artifacts left on disk or in the registry.

## Links

- Repo: https://github.com/dword64/Ow-Anti-Flag

## Related

[[ow-fov]] · [[ow-outlines]] · [[ow2-wardenrekter]] · [[hwid-steam-spyware-terminator]] · [[hwid-spoofer]] · [[overwatch-1-cheat-source]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
