---
title: PoGo Gotta Catch Em All
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/BennyWaitWhat__PoGo-Gotta-Catch-Em-All.md
  - wiki/sources/README-categories.md
updated: 2026-11-04
confidence: medium
---

# PoGo Gotta Catch Em All

Rooted **Android** toolkit for **Pokémon GO** that drives the live **Unity IL2CPP** client through **Frida** gadget instrumentation rather than forging server requests. **AutoCatcher** runs in Termux for wild/lure/incense encounters, stop spins, and research rewards; **pogo_extract** reads bag and game-master state, ranks PvP stat products, runs cull/reconciliation engines, and gates in-game tag sync behind an **11-audit** byte-exact verification suite. (source: wiki/sources/descriptions/BennyWaitWhat__PoGo-Gotta-Catch-Em-All.md)

Useful for mobile client instrumentation, IL2CPP introspection, and operational constraints on rooted hardware in the cheat / `game:pokemongo` lane. Complements static dump tooling such as [[pokemongo-dumper]] and generic [[il2cpp]] / [[frida]] mobile workflows on [[overviews/mobile-security]].

## Links

- Repo: https://github.com/BennyWaitWhat/PoGo-Gotta-Catch-Em-All

## Related

[[pokemongo-dumper]] · [[il2cpp]] · [[frida]] · [[frida-il2cpp-datacollector]] · [[terraria-android-modding]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
