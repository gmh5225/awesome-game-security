---
title: MHA2 Remastered
kind: entity
topics: [reverse-engineering, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/Mag1cByt3s__mha2-remastered.md
  - wiki/sources/README-categories.md
updated: 2026-11-23
confidence: medium
---

# MHA2 Remastered

Native Linux remaster engine for *Moorhuhn Adventure 2* that statically recompiles the original 2005 Windows x86-32 PE executable into C and runs it through a clean-room Win32 and DirectX compatibility layer—no Wine or CPU emulator. (source: wiki/sources/descriptions/Mag1cByt3s__mha2-remastered.md)

## Stack

- **Lifter:** standalone Python tooling with Capstone disassembly; parses the PE binary, discovers functions and switch tables, and emits generated C.
- **Runtime:** C emulator for flat guest memory, x87 FPU behavior, and HLE for DirectDraw, DirectInput, DirectSound, and DirectShow-style video APIs behind an **OpenGL 3.3 Core** renderer (SDL2 + FFmpeg).
- **Asset / packaging:** companion Python tools unpack game archives, apply neural 4K upscaling for backgrounds and sprites, and produce portable Linux builds. (source: wiki/sources/descriptions/Mag1cByt3s__mha2-remastered.md)

README category: Cheat (clean-room x86-32→Linux x86_64 static recompiler plus OpenGL 3.3 remaster runtime; **BYO legal game copy**).

## Audience

Reverse engineers and preservation researchers studying static binary lifting, legacy Win32 game internals, and end-to-end commercial PE recompilation—not live anti-cheat or online multiplayer security work. (source: wiki/sources/descriptions/Mag1cByt3s__mha2-remastered.md)

## Links

- Repo: https://github.com/Mag1cByt3s/mha2-remastered

## Related

[[nfsu2recomp]] · [[sc2-android-recomp]] · [[levo]] · [[legacy-recreated]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]