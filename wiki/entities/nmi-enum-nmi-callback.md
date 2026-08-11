---
title: NMI EnumNmiCallback
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__NMI-EnumNmiCallback.md
updated: 2026-08-11
confidence: medium
---

# NMI EnumNmiCallback

C/C++ Windows kernel proof of concept focused on **enumerating registered NMI (Non-Maskable Interrupt) callbacks** — the `KeRegisterNmiCallback` surface anti-cheat and security software use for cross-processor debugger detection, hidden-thread inspection, and other Ring0 integrity checks. Aimed at game-security researchers and reverse engineers studying offensive kernel techniques in the cheat / Windows kernel explorer lane. (source: wiki/sources/descriptions/gmh5225__NMI-EnumNmiCallback.md)

Complements defensive NMI callback research such as [[nmi-callback]], register/trigger PoCs such as [[nmi-nmi-callback]], disable PoCs such as [[nmi-callback-blocker2]], and sits beside broader [[kernel-callbacks]] enumeration tooling such as [[openark]], [[winobjex64]], and [[rtoolz]].

## Links

- Repo: https://github.com/gmh5225/NMI-EnumNmiCallback [Enumerate NMI]

## Related

[[nmi-callback]] · [[nmi-nmi-callback]] · [[nmi-callback-blocker2]] · [[kernel-callbacks]] · [[openark]] · [[winobjex64]] · [[rtoolz]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
