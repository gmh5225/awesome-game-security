---
title: CTRComposer
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/samaBR85__CTRComposer.md
updated: 2026-07-27
confidence: medium
---

# CTRComposer

Raw `.3gx` overlay engine and blank plugin template for Nintendo 3DS games under the Luma3DS plugin loader (C + assembly). Renders a themeable on-screen UI to the framebuffer without CTRPluginFramework or game-specific hooks, using the system shared font, inline button glyphs, and settings under the plugin install path. Ships as a self-contained any-Title-ID starter (~90% game-independent) so developers mainly add a cheat table, art, and Title ID — aimed at building new cheat/overlay plugins or reviving older `.plg`/`.3gx` plugins that no longer load on current Luma3DS. (source: wiki/sources/descriptions/samaBR85__CTRComposer.md)

## Links

- Repo: https://github.com/samaBR85/CTRComposer

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[ocarina-ctr-composer]] · [[se-tools]]
