---
title: SigThief
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/secretsquirrel__SigThief.md
updated: 2026-07-23
confidence: medium
---

# SigThief

Steals Authenticode signatures from PE files by transplanting certificate data (e.g. `certTable`) onto other binaries. Useful for studying AV vendors that trust certain CAs without full signature validation, or that only check whether a certificate table is populated. Aimed at Some Tricks / Windows Ring3 research rather than as a shipping anti-cheat product. (source: wiki/sources/descriptions/secretsquirrel__SigThief.md)

Adjacent to PE triage viewers such as [[totalpe2]] and leaked-cert / DSE abuse research such as [[pastdse]]: here the focus is user-mode PE signature copy for weak trust-check study, not driver signing or clock-skew DSE bypass.

## Links

- Repo: https://github.com/secretsquirrel/SigThief

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[totalpe2]] · [[pastdse]] · [[asctool]]
