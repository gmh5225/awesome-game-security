---
title: BenMcAvoy IDA Plugins
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/BenMcAvoy__IDA-Plugins.md
updated: 2026-11-18
confidence: medium
---

# BenMcAvoy IDA Plugins

CMake-built **IDA Pro 9.x / Hex-Rays** plugin suite aimed at MSVC native and game binaries. Utilities ship together for vtable and virtual-call navigation, one-click STL container retyping and cleanup, collapsing inlined **XXHash32/64** and CRT idioms (e.g. `strlen` loops), and **MSVC RTTI**-based singleton and inheritance analysis with struct layout synthesis. A **Lua function finder** targets Scrap Mechanic–style binaries by locating `luaL_register` bindings, renaming Lua entry points, and folding argument-count check boilerplate into readable pseudocode. Implemented in C++ against the modern IDA SDK with a small Python doc generator. (source: wiki/sources/descriptions/BenMcAvoy__IDA-Plugins.md)

Integrated MSVC game-binary ergonomics pack—not a single-purpose plugin. Distinct from repnz/[[ida-plugins]] (register cross-references) and from gmh5225's curated index [[list-of-ida-plugins]]. Complements C++ static-RE tools such as [[classmaker]], [[pyclassinformer]], [[rtti-parser]], [[ida-vtable-tools]], and [[ida-vtable-explorer]].

## Links

- Repo: https://github.com/BenMcAvoy/IDA-Plugins

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[classmaker]] · [[pyclassinformer]] · [[rtti-parser]] · [[ida-vtable-tools]] · [[ida-vtable-explorer]] · [[list-of-ida-plugins]] · [[ida-plugins]] · [[idaplugins]]