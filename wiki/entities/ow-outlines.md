---
title: Ow-Outlines
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__Ow-Outlines.md
updated: 2026-08-11
confidence: medium
---

# Ow-Outlines

Internal Overwatch DLL (gmh5225) that enables enemy **glow/outline ESP** by patching a fixed offset (`GlowESP` at `0xE22510`) relative to the `Overwatch.exe` module base. Injected as a DLL into the game process; resolves the base via `GetModuleHandleA("Overwatch.exe")`, uses a **VEH** (Vectored Exception Handler) mechanism from `USEVEH.h`, and writes glow configuration values directly into the game's outline rendering data structures. README tag: `[Shows Players through walls]`. Useful for game security researchers studying internal memory manipulation for visual ESP and engine-native outline rendering exploitation in Overwatch. (source: wiki/sources/descriptions/gmh5225__Ow-Outlines.md)

Contrasts with external glow ESP such as [[cs-2-glow]] (out-of-process memory reads) and Present-hook overlays; complements Blizzard/Overwatch tooling such as [[overwatch-iat-fixer]] (protected-binary IAT repair) and multi-title Overwatch research such as [[meowsense]].

## Links

- Repo: https://github.com/gmh5225/Ow-Outlines

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overwatch-iat-fixer]] · [[meowsense]] · [[cs-2-glow]] · [[pine]]
