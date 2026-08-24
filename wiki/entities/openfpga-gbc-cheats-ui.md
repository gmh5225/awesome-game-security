---
title: openfpga-gbc-cheats-ui
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/kroy-the-rabbit__openfpga-GBC-cheats-ui.md
  - wiki/sources/README-categories.md
updated: 2026-08-24
confidence: medium
---

# openfpga-gbc-cheats-ui

Desktop **Pocket cheat picker** (Python/tkinter) for selecting and deploying cheat codes onto an Analogue Pocket SD card for Game Boy and Game Boy Color openFPGA cores. Three-pane UI browses systems, games, and cheats from the libretro database, then writes `.cht` files to the card in one action. Parses Game Genie and GameShark formats, matches cheats to ROM dumps or manually entered cartridge names, and flags whether each code applies as a safe CPU read patch or a direct RAM write. Shares its cheat-file parser with the openfpga-GBC-cheats core and includes CLI utilities to verify Game Genie compare bytes against ROM images. Targets retro hardware enthusiasts and RE-minded users managing cheats on real Analogue Pocket hardware rather than emulators. (source: wiki/sources/descriptions/kroy-the-rabbit__openfpga-GBC-cheats-ui.md)

Listed in the README under **Game Boy**.

## Links

- Repo: https://github.com/kroy-the-rabbit/openfpga-GBC-cheats-ui

## Related

[[kevboy]] · [[feather-gb]] · [[gb-studio]] · [[bizhawk]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
