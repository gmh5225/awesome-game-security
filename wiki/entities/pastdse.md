---
title: PastDSE
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/utoni__PastDSE.md
updated: 2026-07-19
confidence: medium
---

# PastDSE

Windows Driver Signature Enforcement (DSE) bypass research tool that temporarily rolls the system clock back before a certificate revocation window, signs a driver with leaked VeriSign certificates, then restores the date. Includes a kernel component (BlackBone PE load/reloc), a user-mode controller, and certificate material for studying leaked-cert / clock-skew DSE abuse. (source: wiki/sources/descriptions/utoni__PastDSE.md)

Adjacent to CI/`g_CiOptions` controllers such as [[kvc]] and early-boot DSE/HVCI research such as [[bootbypass]]: here the focus is certificate + wall-clock abuse rather than patching CI callbacks or boot-manager checks.

## Links

- Repo: https://github.com/utoni/PastDSE

## Related

[[kvc]] · [[bootbypass]] · [[kernel-research-kit]] · [[byovd]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
