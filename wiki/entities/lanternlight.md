---
title: Lanternlight
kind: entity
topics: [anti-cheat, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/Remus3__Lanternlight.md
updated: 2026-08-21
confidence: medium
---

# Lanternlight

Python **Mistfall Hunter** companion and analysis project (Remus3) that studies PvPvE extraction ARPG gameplay from **outside the protected process**. Built for kernel-level anti-cheat constraints, it deliberately avoids injection, process memory reads, network interception, and asset extraction. Instead it derives state from the game's own **log files**, **UE5 GVAS save** parsing, and **passive screen capture**. The **Emberforge** module handles combat and build math with strict provenance rules—redacting Steam and session identifiers and omitting unmeasured stats rather than fabricating values. Targets players and researchers who need build planning and session analysis on a live anti-cheat title without risking a permanent account ban. (source: wiki/sources/descriptions/Remus3__Lanternlight.md)

Contrasts with RPM externals such as [[launcher-abuser]] and CV aimbots such as [[nuremx]] by staying entirely off the protected process. Complements UE5 **GVAS** save tooling such as [[palworld-save-tools]] for offline save manipulation, but focuses on live-title companion analysis under AC.

## Links

- Repo: https://github.com/Remus3/Lanternlight

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[palworld-save-tools]] · [[nuremx]] · [[unreal-object-model]] · [[easy-anti-cheat]]
