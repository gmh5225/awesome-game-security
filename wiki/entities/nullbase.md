---
title: NullBase
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/NullTerminatorr__NullBase.md
updated: 2026-08-22
confidence: medium
---

# NullBase

Simple **C++ game-hack base** (NullTerminatorr) designed to be easy to read and extend. Core building blocks include **memory helpers**, **entity and local-player abstractions**, **math utilities**, and **world-to-screen** projection code. The project uses a straightforward **Visual Studio** solution layout so learners can quickly navigate modules and add features. Primary use case: teaching beginners how cheat frameworks are structured and iterated—not a production anti-cheat evasion stack. (source: wiki/sources/descriptions/NullTerminatorr__NullBase.md)

Complements other NullTerminatorr educational samples such as [[nullhook]] (split driver+client kernel cheat tutorial) and [[thread-hijacking-injector]] (compact injection PoC) when studying how cheat codebases grow from readable scaffolds into more advanced architectures.

## Architecture highlights

| Component | Role |
|-----------|------|
| Memory helpers | Cross-module read/write and pointer utilities |
| Entity / local-player | Game-object abstractions for iteration and state |
| Math utilities | Vectors, angles, and common game-math helpers |
| World-to-screen | Camera/view projection for ESP-style overlays |
| Visual Studio layout | Clear project structure for learner navigation |

See [[world-to-screen]] for projection math and [[intro-to-gamehacking]] for step-by-step beginner labs that pair well with this scaffold.

## Links

- Repo: https://github.com/NullTerminatorr/NullBase

## Related

[[overviews/game-hacking]] · [[world-to-screen]] · [[intro-to-gamehacking]] · [[gamehacking-cheatsheet]] · [[nullhook]] · [[thread-hijacking-injector]] · [[lab-esp-and-aimbot]]
