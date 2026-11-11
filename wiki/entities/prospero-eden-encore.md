---
title: Prospero.Eden Encore
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/niakw__ProsperoEden-Encore.md
  - wiki/sources/README-categories.md
updated: 2026-11-11
confidence: medium
---

# Prospero.Eden Encore

PS5 homebrew that ports the **ProsperoEden** Nintendo Switch emulator stack into a native TV-oriented launcher (niakw/ProsperoEden-Encore). Eden-based builds run Switch **NS1/NS2** containers and related native loader formats from a console-local library UI. Aimed at researchers studying closed-platform homebrew deployment, emulator hardening, JIT behavior, and low-level graphics on PlayStation—not online anti-cheat bypass. README category: `Nintendo Switch`. (source: wiki/sources/descriptions/niakw__ProsperoEden-Encore.md) (source: wiki/sources/README-categories.md)

## Stack

**C++** with **Makefile**-driven builds, plus Python verification and staging tooling for reproducible releases. Validated **PS5 system firmware 13.60**; **Dynarmic** ARM64 JIT; **Vulkan** and **OpenGL** with RADV-style GPU paths; per-game profiles; flexible firmware/key storage for Switch dumps; bounded caching. (source: wiki/sources/descriptions/niakw__ProsperoEden-Encore.md)

## UX and engineering

TV-first **DualSense** launcher with multi-language UI catalogs. **CodeQL**-driven security review and explicit separation from jailbreak or entitlement exploits. (source: wiki/sources/descriptions/niakw__ProsperoEden-Encore.md)

## Positioning

Same-author crossover with [[niak-ps5]] and Eden-line ports such as [[opensw]] (Android) and [[nxbox]] (Xbox UWP). (source: wiki/sources/descriptions/niakw__ProsperoEden-Encore.md)

## Links

- Repo: https://github.com/niakw/ProsperoEden-Encore

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]] · [[nxbox]] · [[opensw]] · [[niak-ps5]]
