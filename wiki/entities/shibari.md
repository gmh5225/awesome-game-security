---
title: shibari
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jnastarot__shibari.md
updated: 2026-08-03
confidence: medium
---

# shibari

C++/C tool that **links multiple PE and PE+ executables into one** output image—useful for modding workflows that combine separate modules or payloads into a single on-disk binary. Listed in the Anti Cheat → Binary Packer lane for anti-cheat engineers and defensive researchers studying PE composition, multi-module clients, and binary packer / linker surfaces rather than shipping as an AC product. (source: wiki/sources/descriptions/jnastarot__shibari.md)

Complements compress/encrypt packers such as [[packer]] and [[x64-exe-packer]] by illustrating PE merge/link semantics—not a packer, unpacker, or debugger.

## Links

- Repo: https://github.com/jnastarot/shibari

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[petoy]] · [[packer]] · [[x64-exe-packer]] · [[totalpe2]]
