---
title: Miata
kind: entity
topics: [game-hacking, graphics-api, game:cs2]
sources:
  - wiki/sources/descriptions/staromodny__miata.md
  - wiki/sources/README-categories.md
updated: 2026-10-30
confidence: high
---

# Miata

**Miata** (staromodny/miata) is a free, open-source **external Counter-Strike 2 radar** for Windows: a standalone C++ executable (VS2022/CMake) that reads live client memory through configurable offsets (aligned with common dump tooling such as [[cs2-dumper]]) and draws teammate/enemy positions on a separate **Direct3D 9** overlay window via the header-only Daisy library. Layout, size, position, vertical sync, and capture visibility are driven by a simple text config. Aimed at game-security researchers, reverse engineers, and anti-cheat developers studying external memory radar on CS2. (source: wiki/sources/descriptions/staromodny__miata.md)

## Architecture

- **Memory:** out-of-process reads of the CS2 client; offsets loaded from a text file (cs2-dumper–compatible refresh workflow).
- **Game state:** Valve-style entity and pawn structures parsed into radar positions.
- **Rendering:** dedicated D3D9 device layer + Daisy minimap-style overlay (separate window from the game).

## Catalog

Listed under README **Cheat** → CS2 external/radar lanes beside browser stacks such as [[cs2-webradar]] and DMA radar samples such as [[cs2-dma-radar]]. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/staromodny/miata

## Related

[[cs2-dumper]] · [[cs2-webradar]] · [[cs2-offsets]] · [[cs2-dma-radar]] · [[world-to-screen]] · [[present-hook]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]]
