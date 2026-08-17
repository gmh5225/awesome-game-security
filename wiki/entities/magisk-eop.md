---
title: MagiskEoP
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/canyie__MagiskEoP.md
updated: 2026-08-17
confidence: medium
---

# MagiskEoP

Proof-of-concept **Android privilege escalation** that demonstrates a vulnerability in Magisk's **`su` daemon**. Exploits a race condition or logic flaw in Magisk's root-access granting mechanism to escalate from an **unprivileged app to root without user approval**. Java/C implementation documents the vulnerability and attack vector for Android security researchers studying [[magisk]] internals and root-management security. (source: wiki/sources/descriptions/canyie__MagiskEoP.md)

Sits in the Cheat / Magisk / exploit lane opposite defensive Magisk probes such as [[magisk-killer]] and [[magiskdetector]], and beside canyie's other Magisk-adjacent work ([[riru-momo-hider]], [[canyie-pine]]).

## Links

- Repo: https://github.com/canyie/MagiskEoP

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[mobile-anti-cheat]] · [[magisk]] · [[magisk-killer]] · [[magiskdetector]] · [[riru-momo-hider]] · [[canyie-pine]]
