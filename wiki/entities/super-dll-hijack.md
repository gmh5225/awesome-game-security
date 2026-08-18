---
title: SuperDllHijack
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/anhkgg__SuperDllHijack.md
updated: 2026-08-18
confidence: medium
---

# SuperDllHijack

Generic Windows DLL hijacking helper for proxy-DLL style interception: C/C++ code and examples forward exports without manually recreating every original function signature. The approach renames the original module and supplies a replacement DLL whose `DllMain` invokes a helper routine to pass through behavior to the renamed library. (source: wiki/sources/descriptions/anhkgg__SuperDllHijack.md)

Useful for loader experimentation, red-team load-path research, and studying module-loading abuse in game-security environments. Sits in the Cheat → DLL Hijack lane beside catalog DBs [[windows-dll-hijacking]] and [[hijacklibs]], discovery tooling [[dllirant]], workflow automation [[impulsive-dll-hijack]], and export-stub generators such as [[dll-hijack-export-dumper]] (not a game-specific cheat).

## Links

- Repo: https://github.com/anhkgg/SuperDllHijack

## Related

[[windows-dll-hijacking]] · [[hijacklibs]] · [[dllirant]] · [[impulsive-dll-hijack]] · [[dll-hijack-export-dumper]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[injectors]]
