---
title: ClassMaker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Pycatchown__ClassMaker.md
updated: 2026-08-22
confidence: medium
---

# ClassMaker

IDA Python plugin that automatically reconstructs C++ classes from constructor pseudocode. It traces vtable assignments, creates or updates IDA structs, and applies naming heuristics to class layouts. Targets 32-bit and 64-bit workflows and is designed around practical reversing rather than full-binary automation—mainly for reverse engineers who want to speed up manual class and vtable recovery in game or native binaries. (source: wiki/sources/descriptions/Pycatchown__ClassMaker.md)

Constructor-pseudocode–driven class recovery for IDA—not RTTI metadata parsing or interactive vtable editing. Complements [[pyclassinformer]] and [[rtti-parser]] (RTTI-driven hierarchy/rename), [[ida-vtable-tools]] (vtable skeleton export / slot indexing), and [[classy]] (manual class/vtable organization and C header export).

## Links

- Repo: https://github.com/Pycatchown/ClassMaker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[pyclassinformer]] · [[rtti-parser]] · [[ida-vtable-tools]] · [[ida-medigate]] · [[classy]] · [[ida-missinglink]]
