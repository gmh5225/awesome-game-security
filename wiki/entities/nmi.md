---
title: Nmi (ekknod)
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/ekknod__Nmi.md
updated: 2026-08-16
confidence: medium
---

# Nmi (ekknod)

C/C++ Windows kernel research focused on **blocking NMI (Non-Maskable Interrupt) interrupts** — the cross-processor delivery path anti-cheat systems use for NMI callback stack walks, hidden-thread inspection, and other Ring0 integrity checks. Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / Windows kernel explorer lane. (source: wiki/sources/descriptions/ekknod__Nmi.md)

Complements other NMI disable PoCs such as [[nmi-callback-blocker2]] and [[disable-nmi-callbacks]]; register/trigger research such as [[nmi-nmi-callback]]; enumeration such as [[nmi-enum-nmi-callback]]; and defensive NMI callback study such as [[nmi-callback]] within the [[kernel-callbacks]] lane.

## Links

- Repo: https://github.com/ekknod/Nmi [Blocking NMI interrupts]

## Related

[[nmi-callback-blocker2]] · [[disable-nmi-callbacks]] · [[nmi-nmi-callback]] · [[nmi-enum-nmi-callback]] · [[nmi-callback]] · [[kernel-callbacks]] · [[kernel-anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
