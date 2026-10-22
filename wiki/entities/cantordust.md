---
title: CantorDust
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Battelle__cantordust.md
  - wiki/sources/README-categories.md
updated: 2026-10-22
confidence: high
---

# cantordust

**CantorDust** ([Battelle/cantordust](https://github.com/Battelle/cantordust)) is a Java **Ghidra extension and script** plus optional **standalone desktop app** for interactive **binary visualization**—helping reverse engineers see structure in raw bytes and jump to the offsets that produce interesting patterns. (source: wiki/sources/descriptions/Battelle__cantordust.md)

## Architecture

| Layer | Role |
|-------|------|
| **Ghidra extension / script** | Embeds visualizations in Ghidra; click a plot point to sync the CodeBrowser listing to the corresponding file offset |
| **Standalone build** | Same visualization modes with an integrated hex pane (no Ghidra session required) |
| **Build** | Gradle (Java); small Python utility for development cleanup |

## Visual modes

Byte-value plots, digraph and **trigram clouds**, **metric maps** along space-filling curves, linear bitmaps, and byte-frequency views—with sliders to focus regions of large firmware, executable, or malware samples.

## Capabilities

- Navigate large binaries by **pattern recognition** (code vs data blobs, embedded artifacts) before deep disassembly.
- Complements in-Ghidra byte editors such as [[ghidra-hexeditor]] and [[scalpel]], and standalone workbenches like [[imhex]] and [[hexwalk]].
- README category: **Cheat → Ghidra Plugins** (visual triage for game client/module RE, not live memory cheating).

## Related

[[ghidra-hexeditor]] · [[scalpel]] · [[imhex]] · [[hexwalk]] · [[binary-cartography]] · [[binary-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]

## Links

- Repo: https://github.com/Battelle/cantordust
