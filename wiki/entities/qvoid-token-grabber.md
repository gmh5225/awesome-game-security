---
title: Qvoid Token Grabber
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Enum0x539__Qvoid-Token-Grabber.md
updated: 2026-08-25
confidence: medium
---

# Qvoid Token Grabber

.NET-based Windows credential and token grabbing toolkit focused on Discord and browser data collection. Implements webhook-based exfiltration and bundles anti-analysis checks—anti-debugging, anti-VM, anti-sandbox, and anti-emulation—typical of information-stealer malware. Key capabilities include Discord token harvesting, browser cookie and password extraction, screenshot capture, Wi-Fi password collection, and clipboard hijacking. Primary use case is offensive security and malware-analysis research into information-stealer techniques and account-token abuse workflows common in gaming communities. (source: wiki/sources/descriptions/Enum0x539__Qvoid-Token-Grabber.md)

Complements Go post-ex credential collectors such as [[pillager]] and locked-file acquisition PoCs such as [[idontlikefilelocks]] when studying stealer tradecraft beside live DFIR triage such as [[dfirtriage]].

## Links

- Repo: https://github.com/Enum0x539/Qvoid-Token-Grabber

## Related

[[pillager]] · [[idontlikefilelocks]] · [[anti-sandbox]] · [[pafish]] · [[al-khaser]] · [[dfirtriage]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
