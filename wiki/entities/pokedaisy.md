---
title: PokeDaisy
kind: entity
topics: [game-hacking, reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/lidor30__pokedaisy.md
updated: 2026-11-12
confidence: medium
---

# PokeDaisy

Companion overlay for Pokémon Game Boy, GBA, and related titles inside emulators: live party, battle, bag, map, Pokédex, and guide UI while the game runs. (source: wiki/sources/descriptions/lidor30__pokedaisy.md)

Main stack: Kotlin / Jetpack Compose Android app with a portable C core over JNI, plus a Nintendo 3DS homebrew build on libmGBA and headless simulation/fixture tests. ROMs and hacks are keyed by SHA-1 and art fingerprints; runtime state comes from emulated WRAM and save layouts per title, in-ROM tables via pret-style decomp knowledge, and mGBA-format cheats with dedicated save-verification logic. Targets players, ROM researchers, and reverse engineers who need accurate Gen 1–3 Pokémon runtime and save visibility during emulation.

## Links

- Repo: https://github.com/lidor30/pokedaisy (README: Android GB/GBC/GBA/DS Pokémon player with live companion for party, bag, map, battle state)

## Related

[[kevboy]] · [[feather-gb]] · [[bizhawk]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]]
