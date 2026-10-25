---
title: NiakPS5
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/niakw__NiakPS5.md
  - wiki/sources/README-categories.md
updated: 2026-10-25
confidence: high
---

# NiakPS5

**NiakPS5** (niakw/NiakPS5) is a native, full-screen home interface for homebrew-enabled **PlayStation 5** consoles: a custom game and app library with **DualSense** navigation, local title discovery, and launches through a **loopback-only broker** on `127.0.0.1`. (source: wiki/sources/descriptions/niakw__NiakPS5.md)

README category: **PlayStation** (homebrew dashboard / library shell).

## Library and launch

- Scans **locally installed** titles into a browsable library.
- Starts games/apps via the **127.0.0.1** launch broker (no wide-area network surface in the described design).
- Renders animated **3D PS4/PS5-style case art**; optional **LaunchBox CDN** artwork is fetched **only when a title is selected** (lazy network use). (source: wiki/sources/descriptions/niakw__NiakPS5.md)

## Stack

- **GPL-licensed** native PS5 application (**C/C++**) with **OpenGL** rendering validated in **CI**.
- **Python** scripts and tests for packaging and metadata workflows beside the native title. (source: wiki/sources/descriptions/niakw__NiakPS5.md)

## Positioning

Aimed at PS5 homebrew users and researchers who want a **self-contained library shell** that respects Sony **launch and licensing boundaries** rather than replacing system shell components—adjacent to runtime launch/injection tooling ([[nines]], [[elfloader]]) and static PS5 binary RE ([[ida-ps5-elf-plugin]]) in the same PlayStation lane as HV/homebrew stacks ([[ps5-linux-loader]], [[bd-un-jb]]). (source: wiki/sources/descriptions/niakw__NiakPS5.md)

## Links

- Repo: https://github.com/niakw/NiakPS5

## Related

[[ps5-linux-loader]] · [[nines]] · [[elfloader]] · [[ida-ps5-elf-plugin]] · [[cheatrunner-patches]] · [[game-cheats]] · [[bd-un-jb]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
