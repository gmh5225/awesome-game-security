---
title: NMICallbackBlocker2
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__NMICallbackBlocker2.md
updated: 2026-08-11
confidence: medium
---

# NMICallbackBlocker2

C++ Windows kernel proof of concept focused on **disabling NMI (Non-Maskable Interrupt) callbacks** — the `KeRegisterNmiCallback` surface anti-cheat and security software use for cross-processor debugger detection, hidden-thread inspection, and other Ring0 integrity checks. Aimed at game-security researchers and reverse engineers studying offensive kernel techniques in the cheat / Windows kernel explorer lane. (source: wiki/sources/descriptions/gmh5225__NMICallbackBlocker2.md)

Complements defensive NMI callback research such as [[nmi-callback]], register/trigger PoCs such as [[nmi-nmi-callback]], enumeration PoCs such as [[nmi-enum-nmi-callback]], and sits beside broader [[kernel-callbacks]] manipulation tooling such as [[ps-notif-routine-unloader]] and [[rtoolz]].

## Links

- Repo: https://github.com/gmh5225/NMICallbackBlocker2 [Disable NMI]

## Related

[[nmi-callback]] · [[nmi-nmi-callback]] · [[nmi-enum-nmi-callback]] · [[kernel-callbacks]] · [[ps-notif-routine-unloader]] · [[rtoolz]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
