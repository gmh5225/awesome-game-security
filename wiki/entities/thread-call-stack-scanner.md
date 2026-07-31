---
title: thread-call-stack-scanner
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/m417z__thread-call-stack-scanner.md
updated: 2026-07-31
confidence: medium
---

# thread-call-stack-scanner

Utility for **safely unloading DLLs that have been hooked into a process** by scanning thread call stacks before teardown. When dynamically loaded modules install inline or trampoline hooks, naive `FreeLibrary` can crash if any thread still has return addresses or frames pointing into the module image — this tool helps AC engineers and defensive researchers manage that lifecycle without process faults. (source: wiki/sources/descriptions/m417z__thread-call-stack-scanner.md)

Complements offensive hook libraries ([[polyhook]], [[detoursnt]]) and defensive hook-discovery tooling ([[hook-buster]], [[hookhunter]]) on the module-load/unload side rather than detection alone.

## Links

- Repo: https://github.com/m417z/thread-call-stack-scanner

## Related

[[hook-buster]] · [[hookhunter]] · [[polyhook]] · [[detoursnt]] · [[thread-stack-spoofer]] · [[stack-spoofing]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
