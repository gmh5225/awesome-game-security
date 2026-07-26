---
title: FreeDirect
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/openeggbert__free-direct.md
updated: 2026-07-26
confidence: medium
---

# FreeDirect

C++20 compatibility layer that reimplements a narrow, game-driven subset of DirectX 3 (2D)—DirectDraw, DirectSound, and DirectPlay—so selected legacy Win32 titles can run without the original DirectX SDK or Windows. Surfaces, blits, palettes, clippers, and static PCM playback map onto SDL3; DirectPlay uses a pluggable transport with an ENet-based peer session/join/messaging path. Built with CMake; ships COM-style public headers and automated tests—aimed at call-site-driven porting of classic 2D DirectX games. Catalogued under DirectX Compatibility. (source: wiki/sources/descriptions/openeggbert__free-direct.md)

## Links

- Repo: https://github.com/openeggbert/free-direct

## Related

[[xidi]] · [[gta4-rtx]] · [[directxhook]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
