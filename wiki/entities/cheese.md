---
title: cheese
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/zhuowei__cheese.md
updated: 2026-07-17
confidence: medium
---

# cheese

Root exploit for Meta Quest 3 and Quest 3S VR headsets (firmware v79 and below) using CVE-2025-21479, a Qualcomm Adreno GPU vulnerability. Achieves temporary root and installs Magisk without modifying the boot partition. Builds on Project Zero's Adrenaline research and Freedreno GPU documentation. (source: wiki/sources/descriptions/zhuowei__cheese.md)

Relevant to mobile game-security research on Android-class VR platforms: Magisk root paths without permanent boot changes, GPU-driver privilege escalation, and how headset firmware lag widens the exploit window.

## Links

- Repo: https://github.com/zhuowei/cheese
- CVE: CVE-2025-21479

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[frida]]
