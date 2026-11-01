---
title: SwitchWakerHD
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/centollOS__SwitchWakerHD.md
updated: 2026-11-01
confidence: medium
---

# switchwakerhd

Native **static recompilation** port of *The Legend of Zelda: The Wind Waker HD* (Wii U retail binaries) to modern hosts—Switch (deko3D), Vulkan desktops, Android, and Meta Quest—using player-supplied Wii U game files rather than full-system emulation. (source: wiki/sources/descriptions/centollOS__SwitchWakerHD.md)

## Stack

- **Build:** C++ / CMake host runtime; Python pipelines decompile PowerPC guest code, recompile to native, extract and verify assets, and benchmark on real consoles.
- **Graphics:** Wii U **Latte** shader translation to **Vulkan** or **deko3D**; shader manifests; optional profile-guided optimization.
- **Dev introspection:** TCP debug server on Nintendo Switch (live logs, warps, deployment during development).
- **Extras:** SDL input, mod SDK and world-editor workflows, C# desktop installers.

## Audience

Reverse engineers and game-security researchers studying large-scale commercial decompilation, encrypted disc archives, GPU shader recovery, and runtime introspection on closed platforms—beside other static-recomp ports such as [[smo-recomp]] and [[mcla-pc]]. The repository ships **no game assets**; users must supply their own Wii U dump.

## Links

- Repo: https://github.com/centollOS/SwitchWakerHD

## Related

[[smo-recomp]] · [[mcla-pc]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
