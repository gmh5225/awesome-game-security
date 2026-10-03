---
title: Hell Is Us Mod (hiumod)
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/myso-kr__hell-is-us-mod.md
  - wiki/sources/README-categories.md
updated: 2026-10-03
confidence: medium
---

# Hell Is Us Mod (hiumod)

External **Hell Is Us** PC companion by myso-kr that attaches to the running game process and reads or writes **Unreal Engine** memory in place—no on-disk file modifications. Adds a live minimap, quest tracker, story guide, vault/puzzle answers, collectible checklists, and optional single-player cheats via a graphical overlay. Written in **Rust**; locates game state by scanning for engine structures (name pool, `GEngine`) and follows **UObject** reflection to resolve player attributes by name instead of fixed offsets. Includes diagnostic CLI commands and a C# survey tool built on **CUE4Parse** for guide data. (source: wiki/sources/descriptions/myso-kr__hell-is-us-mod.md)

Useful for studying external process attachment and UE memory introspection on offline single-player titles—contrasts with injection-based internals and with log-only companions such as [[lanternlight]].

## Links

- Repo: https://github.com/myso-kr/hell-is-us-mod

## Related

[[unreal-object-model]] · [[zircon-ue-dumper]] · [[lanternlight]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
