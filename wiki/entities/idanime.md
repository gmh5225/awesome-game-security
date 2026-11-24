---
title: idanime
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/shwetsoni__idanime.md
updated: 2026-11-24
confidence: medium
---

# idanime

**idanime** (shwetsoni/idanime) ships twelve anime-styled color themes for **IDA Pro 9.x** with matching background artwork across disassembly, pseudocode, and graph views. Each theme is a user-installable CSS package with per-theme art assets. An **IDAPython** plugin on **PySide6** overlays and blends images on the graph canvas where native Qt theming cannot reach. Text views use **CustomIDAMemo** styling with transparent line backgrounds and anchored images; the plugin applies lighten/darken blending, **HiDPI** assets, and stylesheet-based theme detection to keep nodes and code readable. Cross-platform (**Windows**, **Linux**, **macOS**); aimed at reverse engineers, malware analysts, and game-security researchers in long IDA sessions who want customizable visuals without hurting workflow performance. (source: wiki/sources/descriptions/shwetsoni__idanime.md)

## Positioning

README category: **IDA themes** with decorative backgrounds—extends the analyst-comfort lane beside PoP-Lin/[[idapro-muils]] (scoped Qt dark styling), [[ida-nord-theme]], [[long-night]], and [[ida-dark-plus]] by adding per-view artwork in text panes and graph canvases. Does not alter disassembly, decompilation, or navigation semantics.

## Links

- Repo: https://github.com/shwetsoni/idanime

## Related

[[overviews/reverse-engineering]] · [[idapro-muils]] · [[ida-nord-theme]] · [[long-night]] · [[ida-dark-plus]] · [[idaskins]] · [[ida-themer]]