---
title: Disable Windows Defender
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Disable-Windows-Defender-.md
updated: 2026-08-14
confidence: medium
---

# Disable Windows Defender

Tool that disables Windows Defender with integrated UAC bypass and SYSTEM privilege escalation. Manipulates privilege tokens and leverages COM-based UAC bypass techniques to gain elevated access, then disables real-time protection and Tamper Protection services. (source: wiki/sources/descriptions/gmh5225__Disable-Windows-Defender-.md)

Sits in the AV/EDR-control research lane beside registry/service toggles such as [[defender-control]] and kernel-driver escalation paths such as [[windefctl]] — here the emphasis is user-mode token manipulation plus COM UAC bypass rather than a dedicated kernel helper or GUI registry edits.

## Links

- Repo: https://github.com/gmh5225/Disable-Windows-Defender-

## Related

[[defender-control]] · [[windefctl]] · [[manipulating-token]] · [[cmdt]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
