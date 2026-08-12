---
title: Killer-Exercice
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Killer-Exercice.md
updated: 2026-08-12
confidence: medium
---

# Killer-Exercice

Red-team reverse-and-exploit exercise for kernel-mode process termination against protected targets — anti-cheat services, EDR agents, and other kernel-hardened processes. Demonstrates multiple killing techniques including handle-table manipulation, APC injection, and direct `EPROCESS` modification rather than standard user-mode `TerminateProcess` paths. Positioned as a valid BYOVD killer reportedly not HVCI-blocklisted and absent from common LOLdriver catalogs at publication; companion to [[killer]]. (source: wiki/sources/descriptions/gmh5225__Killer-Exercice.md)

## Links

- Repo: https://github.com/gmh5225/Killer-Exercice
- Parent tool: https://github.com/gmh5225/Killer

## Related

[[killer]] · [[byovd]] · [[process-killer-byovd]] · [[terminator]] · [[watchdog-killer]] · [[pplkiller]] · [[loldrivers]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
