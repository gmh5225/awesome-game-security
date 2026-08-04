---
title: CountHook
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/illegal-instruction-co__CountHook.md
updated: 2026-08-04
confidence: medium
---

# CountHook

Working-set–oriented offensive sample that **bypasses memory checks**, with emphasis on **count**-based integrity signals used by page-protection / working-set scanners. README lane: Cheat → Bypass Page Protection (`WorkingSet`). Aimed at game-security researchers and reverse engineers studying cheat-side evasion of usermode memory-integrity monitors. (source: wiki/sources/descriptions/illegal-instruction-co__CountHook.md)

Complements defensive working-set page-fault monitors such as [[faultline]] (`InitializeProcessForWsWatch` / `GetWsChangesEx` / `QueryWorkingSet`) and related in-memory evasion PoCs such as [[shellcode-fluctuation]] on the offensive page-protection lane.

## Links

- Repo: https://github.com/illegal-instruction-co/CountHook

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[faultline]] · [[shellcode-fluctuation]] · [[voidmaw]] · [[no-access-protection]] · [[processhacker-mcp]]
