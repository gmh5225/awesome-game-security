---
title: xnuspy
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/jsherman212__xnuspy.md
updated: 2026-08-02
confidence: medium
---

# xnuspy

iOS XNU kernel function hooking framework for checkra1n-jailbreakable (checkm8 A8–A11) devices; 4K (A12+) hardware is explicitly unsupported. Aimed at game-security researchers and reverse engineers studying offensive kernel hooking in the Cheat / iOS memory explorer lane—installing patches or trampolines at kernel symbols after obtaining kernel read/write via the checkra1n ecosystem. (source: wiki/sources/descriptions/jsherman212__xnuspy.md)

Complements XNU exploit study [[xnu-1day-practice]] and checkm8 jailbreak trees [[palera1n]]; contrasts with userland inject [[opainject]] and Logos/substrate-style hooks when the research question is kernel-level interception.

## Links

- Repo: https://github.com/jsherman212/xnuspy

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[xnu-1day-practice]] · [[palera1n]] · [[opainject]] · [[oob-entry]]
