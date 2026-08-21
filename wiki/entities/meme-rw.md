---
title: meme-rw
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/SamuelTulach__meme-rw.md
updated: 2026-08-21
confidence: medium
---

# meme-rw

**meme-rw** (SamuelTulach) is a C++/CMake **proof-of-concept framework** for accessing **protected process memory** in game security contexts. It implements a **vulnerable-driver mapping** approach with driver-loading helpers, process and module utilities, and memory read/write control routines. The project demonstrates end-to-end primitives for opening a target process and operating on its memory. Primary use cases are **anti-cheat bypass experimentation** and **defensive research** into how protected-memory access techniques are built. README category: cheat / [kdmapper]. (source: wiki/sources/descriptions/SamuelTulach__meme-rw.md)

Sits in the kdmapper-family lane as a higher-level protected-process R/W framework rather than a bare mapper — overlaps the cross-process kernel memory path documented by [[ntmemory]], [[driver-read-write]], and [[readwrite-kernel-stable]], but emphasizes vulnerable-driver bootstrap plus process open and module enumeration in one CMake project.

## Links

- Repo: https://github.com/SamuelTulach/meme-rw

## Related

[[kdmapper]] · [[kdmapper-rs]] · [[byovd]] · [[ntmemory]] · [[driver-read-write]] · [[readwrite-kernel-stable]] · [[mutante]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
