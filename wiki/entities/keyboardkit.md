---
title: KeyboardKit
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/wesmar__KeyboardKit.md
updated: 2026-07-18
confidence: medium
---

# KeyboardKit

Educational Windows kernel-mode keylogger / rootkit research sample: a keyboard filter driver intercepts keyboard IRPs, a user-mode component ships logs over UDP, and persistence is demonstrated via ExplorerFrame DLL hijacking (plus privilege-escalation / stealth patterns for offensive and defensive study). (source: wiki/sources/descriptions/wesmar__KeyboardKit.md)

Useful threat-model reference for kernel input-filter / IRP-hook surfaces that anti-cheat and EDR stacks monitor, and for Cheat → DLL Hijack persistence adjacent to catalogs such as [[hijacklibs]] / [[windows-dll-hijacking]]. Same-author kernel utilities: [[kvc]], [[vaultguard]], [[windefctl]].

## Links

- Repo: https://github.com/wesmar/KeyboardKit

## Related

[[hijacklibs]] · [[windows-dll-hijacking]] · [[kvc]] · [[vaultguard]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
