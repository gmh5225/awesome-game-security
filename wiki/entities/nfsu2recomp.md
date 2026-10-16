---
title: NFSU2Recomp
kind: entity
topics: [reverse-engineering, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/TalhaMudo__NFSU2Recomp.md
  - wiki/sources/README-categories.md
updated: 2026-10-16
confidence: medium
---

# NFSU2Recomp

Static recompilation project that turns the 32-bit x86 Windows executable of *Need for Speed: Underground 2* into a native ARM64 macOS application without Wine, runtime emulation, or a JIT. (source: wiki/sources/descriptions/TalhaMudo__NFSU2Recomp.md)

## Stack

- **Lifter:** Python tooling lifts guest machine code ahead of time into C compiled by clang.
- **Runtime:** hand-written Win32 API emulation and 32-bit guest address-space mapping.
- **Graphics/audio:** Direct3D 9 and D3DX9 effects translated to Metal; CoreAudio for sound (Objective-C integration).
- **Analysis pipeline:** custom PE relocation recovery, recursive function discovery, indirect-call dispatch tables, and high-level emulation shortcuts for hot paths such as the D3DX effect framework. (source: wiki/sources/descriptions/TalhaMudo__NFSU2Recomp.md)

Primary languages: C (runtime + generated code), Python (lifter/analysis), Objective-C (Metal). README category: Cheat / RE Tools (static recompilation pipeline).

## Audience

Reverse engineers and developers studying x86 static translation, legacy DirectX ports, and game binary analysis—not anti-cheat or live multiplayer security work. (source: wiki/sources/descriptions/TalhaMudo__NFSU2Recomp.md)

## Links

- Repo: https://github.com/TalhaMudo/NFSU2Recomp

## Related

[[jsrf-recomp]] · [[levo]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
