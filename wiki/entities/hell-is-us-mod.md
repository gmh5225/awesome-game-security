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

External **Hell Is Us** PC companion (**hiumod**, myso-kr) that attaches to the running game process and reads or writes **Unreal Engine** memory in place—no on-disk file modifications. (source: wiki/sources/descriptions/myso-kr__hell-is-us-mod.md)

## Capabilities

- Live minimap, quest tracker, story guide, vault/puzzle answers, and collectible checklists via graphical overlay
- Optional single-player cheats while the game runs
- Diagnostic CLI commands for runtime inspection
- C# survey tool built on **CUE4Parse** for guide-data extraction

## Architecture

Written in **Rust**. Locates game state by scanning for engine structures such as the name pool and `GEngine`, then follows **UObject** reflection to resolve player attributes **by name** instead of hard-coded offsets—reducing breakage when layout shifts between builds. (source: wiki/sources/descriptions/myso-kr__hell-is-us-mod.md)

## Use cases

Serves players who want enhanced navigation and completion aids on offline single-player titles, and developers studying external process attachment and UE memory introspection without injection or disk mods. Contrasts with injection-based internals and with log-only companions such as [[lanternlight]].

## Positioning

Listed under **Cheat** as an external UE companion beside RPM externals such as [[launcher-abuser]] and anti-cheat-safe log/save companions such as [[lanternlight]]. The name-based reflection path on [[unreal-object-model]] globals complements SDK dumpers such as [[zircon-ue-dumper]] when the goal is live overlay state rather than header generation.

## Links

- Repo: https://github.com/myso-kr/hell-is-us-mod

## Related

[[unreal-object-model]] · [[zircon-ue-dumper]] · [[lanternlight]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
