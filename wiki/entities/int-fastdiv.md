---
title: int_fastdiv
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/milakov__int_fastdiv.md
updated: 2026-07-30
confidence: medium
---

# int_fastdiv

Header-only C++ drop-in integer type that replaces runtime division with precomputed multiply-and-shift operations derived from *Hacker's Delight* magic-number theory. Overloads `/` and `%` so call sites can swap a constant divisor once and avoid repeated hardware divides—reported ~2× faster than native integer division on CPU. Annotated `__host__ __device__` for use in CUDA GPU kernels alongside host code, making it useful for hot paths in engine simulation, grid indexing, and GPU-side compute shaders. (source: wiki/sources/descriptions/milakov__int_fastdiv.md)

## Links

- Repo: https://github.com/milakov/int_fastdiv

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[rtm]] · [[omath]] · [[gamedev-libraries]]
