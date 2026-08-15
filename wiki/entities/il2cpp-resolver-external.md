---
title: IL2CPP_Resolver_External
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/extremeblackliu__IL2CPP_Resolver_External.md
updated: 2026-08-15
confidence: medium
---

# IL2CPP_Resolver_External

External [[il2cpp]] runtime resolver for Unity titles (extremeblackliu; C++; cheat / game engine explorer:Unity). Reads IL2CPP metadata from outside the game process—parsing `global-metadata.dat` and IL2CPP binary structures via cross-process memory access—to resolve class names, method addresses, field offsets, and type information without code injection. (source: wiki/sources/descriptions/extremeblackliu__IL2CPP_Resolver_External.md)

Targets game hackers building external cheats on IL2CPP-based Unity games. Complements broader external Unity introspection such as [[unity202x-externalresolve]], Mono-only readers such as [[mono-external-lib]], and in-process resolver lanes such as [[il2cpp-resolver]] when the goal is IL2CPP-specific metadata resolution from a separate process.

## Links

- Repo: https://github.com/extremeblackliu/IL2CPP_Resolver_External

## Related

[[il2cpp]] · [[il2cpp-resolver]] · [[unity202x-externalresolve]] · [[mono-external-lib]] · [[taskbarhero-bot]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
