---
title: Anti miHoYo JCC Obfuscate
kind: entity
topics: [reverse-engineering, game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/DNLINYJ__Anti_miHoYo_Jcc_Obfuscate.md
updated: 2026-08-26
confidence: medium
---

# Anti miHoYo JCC Obfuscate

[[x64dbg]] plugin that assists with undoing **JCC and jump-based control-flow obfuscation** in protected Unity game code paths. Monitors specific decryption routine ranges, tracks dynamic jump behavior, and patches instructions to reconstruct more readable execution flow during live debugging sessions. Implemented in C++ with the x64dbg plugin SDK; includes logic tailored to known game build offsets. Intended for game reverse engineering and anti-obfuscation research; author marks the project as no longer maintained. (source: wiki/sources/descriptions/DNLINYJ__Anti_miHoYo_Jcc_Obfuscate.md)

Runtime in-debugger JCC patching complements static Genshin CFG tooling such as [[genshinjumpfixer2]] and [[misc]] (CFG decode) — useful when obfuscated Unity IL2CPP/native paths resist clean static lift but can be stepped under a debugger.

## Links

- Repo: https://github.com/DNLINYJ/Anti_miHoYo_Jcc_Obfuscate

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[x64dbg]] · [[control-flow-flattening]] · [[codecleaner]] · [[genshinjumpfixer2]] · [[il2cpp]]
