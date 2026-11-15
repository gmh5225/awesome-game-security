---
title: linnut 1.6.2 decomp (Angry Birds PC)
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/BurnerAccount-dec__linnut1.6.2-decomp.md
updated: 2026-11-15
confidence: medium
---

# linnut 1.6.2 decomp (Angry Birds PC)

Unofficial **from-scratch reimplementation** of the *Angry Birds* **PC runtime engine**, rebuilt by diffing clean **C++** against **Ghidra decompilations** of retail executables. **CMake** builds **C++** with **SDL2**, **OpenGL 1.x**, embedded **Lua 5.1**, and vendored **Box2D 2.1/2.2**; gameplay stays in each title’s original **Lua scripts** because the host exposes the native APIs those scripts expect rather than reauthoring logic. Physics paths are tuned to match decompiled **Box2D** behavior; **Lua bytecode** can be decrypted and lifted via **unluac**; the tree adds level editors, **save states**, debug overlays, optional executable replacement, and documented scripting/mod hooks. Intended for reverse engineers, preservationists, and researchers studying classic *Angry Birds* PC and related ports with **legally obtained game assets**—not live anti-cheat or online security tooling. (source: wiki/sources/descriptions/BurnerAccount-dec__linnut1.6.2-decomp.md)

README lane: unofficial C++ engine rebuild from Ghidra decompiles; SDL2, OpenGL, Lua 5.1, Box2D; runs original Lua; Game Engine / source.

## Links

- Repo: https://github.com/BurnerAccount-dec/linnut1.6.2-decomp

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[provenance-elite-force-ii-decomp-android-linux]] · [[harvest-moon-snes-decomp]] · [[static-runtime-evidence]]