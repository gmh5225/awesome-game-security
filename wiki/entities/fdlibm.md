---
title: fdlibm
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/freemint__fdlibm.md
updated: 2026-08-15
confidence: medium
---

# fdlibm

Portable C **libm** implementation centered on Sun's Freely Distributable **fdlibm** transcendental and elementary math routines (`sin`, `cos`, `exp`, `log`, `pow`, etc.). Listed under README **Mathematics** for engine programmers and gameplay or simulation developers who need a self-contained math runtime rather than platform CRT libm alone. (source: wiki/sources/descriptions/freemint__fdlibm.md)

Sits beside SIMD vector/matrix libraries such as [[rtm]] and [[directxmath]] and higher-level cheat-oriented frameworks such as [[omath]] as a lower-level scalar floating-point building block—not a render hook or AC artifact.

## Links

- Repo: https://github.com/freemint/fdlibm

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[rtm]] · [[directxmath]] · [[omath]] · [[int-fastdiv]]
