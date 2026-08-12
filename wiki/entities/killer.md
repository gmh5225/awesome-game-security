---
title: Killer
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Killer.md
updated: 2026-08-12
confidence: medium
---

# Killer

Kernel-mode process terminator for targets that resist normal user-mode APIs — anti-cheat services, EDR agents, and other kernel-protected processes. Loads a kernel driver and forcefully ends processes by manipulating kernel process structures rather than relying on standard `TerminateProcess` paths. Aimed at red-team operators and security researchers studying driver-backed process termination. Companion exercise repo [Killer-Exercice](https://github.com/gmh5225/Killer-Exercice) is positioned as a red-team reverse-and-exploit lab for a valid BYOVD killer reportedly not HVCI-blocklisted and absent from common LOLdriver catalogs at publication. (source: wiki/sources/descriptions/gmh5225__Killer.md)

## Links

- Repo: https://github.com/gmh5225/Killer
- Exercise: https://github.com/gmh5225/Killer-Exercice

## Related

[[byovd]] · [[process-killer-byovd]] · [[terminator]] · [[watchdog-killer]] · [[pplkiller]] · [[av-edr-killer]] · [[phantomkiller]] · [[loldrivers]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
