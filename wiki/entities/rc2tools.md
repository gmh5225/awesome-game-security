---
title: rc2tools
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ryanmsartor__rc2tools.md
updated: 2026-11-08
confidence: medium
---

# rc2tools

**rc2tools** (ryanmsartor/rc2tools) is a Python-centric CLI toolkit for analyzing and modifying *Rolan's Curse II* on **Game Boy** by working directly with ROM images and documented in-ROM layouts. A Bash entry script drives workflows; **Pillow** decodes Game Boy **2bpp** tiles and assembles **16×16** sprite sheets from chosen byte ranges. (source: wiki/sources/descriptions/ryanmsartor__rc2tools.md)

## Capabilities

- **extract-json** pulls per-character HP, MP, and ability tables into JSON keyed by the ROM's **SHA-256** hash.
- Accepts raw `.gb` files or full **xxd**-style hex dumps so edited stats appear in the output after ROM patching.
- Supporting documentation maps ROM offsets and save formats; unit tests cover extraction and rendering.

## Positioning

Aimed at ROM hackers, game-data researchers, and title-specific balancing/RE—not generic anti-cheat or live-service security tooling. Sits in the retro handheld lane beside [[rom-weaver]] patch workflows, [[bizhawk]] RAM/search tooling, and [[openfpga-gbc-cheats-ui]] hardware cheat deploy—not live memory trainers.

## Links

- Repo: https://github.com/ryanmsartor/rc2tools

## Related

[[rom-weaver]] · [[bizhawk]] · [[openfpga-gbc-cheats-ui]] · [[kevboy]] · [[feather-gb]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
