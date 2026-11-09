---
title: S3 Mobile
kind: entity
topics: [mobile-security, reverse-engineering, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/duruer__s3-mobile.md
updated: 2026-11-09
confidence: medium
---

# S3 Mobile

[duruer/s3-mobile](https://github.com/duruer/s3-mobile) — **mobile port of The Settlers III** on **Android and iOS** from **user-supplied GOG game files**. Runs the original Windows **`S3.EXE`** via emulation and API HLE rather than a ground-up game rewrite. (source: wiki/sources/descriptions/duruer__s3-mobile.md)

## Host stack

Primarily **Rust**: **x86 CPU interpreter** with optional **ARM64 JIT**. **High-level emulation (HLE)** of **KERNEL32**, **USER32**, **GDI32**, **DirectDraw**, **DirectSound**, **DirectInput**, and **DirectPlay**. Supporting tooling includes Python analysis scripts and small Java/Swift frontends for mobile packaging, plus **multiplayer relay networking** and determinism testing for lockstep play. (source: wiki/sources/descriptions/duruer__s3-mobile.md)

## Reverse engineering

Documents extensive RE of **`S3.EXE`**: PE imports, game state, DirectX usage, Wine runtime traces, byte patches for executable variants, and a **mod framework** with guest hooks and touch-oriented UI layers. (source: wiki/sources/descriptions/duruer__s3-mobile.md)

## Research use

Study **guest x86 execution** separate from **reimplemented Win32/DirectX host paths**—same lift-vs-HLE discipline as [[winlator]], [[orthros]], and [[bottleship]]. Useful for classic PC **preservation**, binary RE, and bringing legacy Win32 titles to mobile without full source rewrites. (source: wiki/sources/descriptions/duruer__s3-mobile.md)

## Links

- Repo: https://github.com/duruer/s3-mobile

## Related

[[winlator]] · [[orthros]] · [[bottleship]] · [[static-runtime-evidence]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
