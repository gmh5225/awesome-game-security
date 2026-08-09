---
title: X64DBG MapLdr
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__X64DBG-MapLdr.md
updated: 2026-08-09
confidence: medium
---

# X64DBG MapLdr

[[x64dbg]] plugin (C++) that loads linker `.MAP` output (or MAP files exported from IDA Pro) and applies symbol names and addresses to the debugged binary. Parses MAP files from MSVC, Borland, and other linkers, importing function names, global variable names, and segment information into x64dbg's symbol database—bridging compile-time symbol information with live runtime debugging when PDBs are unavailable. (source: wiki/sources/descriptions/gmh5225__X64DBG-MapLdr.md)

Complements the IDA-side [[ida-pro-loadmap]] workflow and PDB-based symbol recovery ([[pdb]], [[pdblister]]). Useful for game and anti-cheat client RE when a build-time MAP is available but public symbols are stripped.

## Links

- Repo: https://github.com/gmh5225/X64DBG-MapLdr

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[ida-pro-loadmap]] · [[pdb]] · [[idenlibx]] · [[symbridge]]
