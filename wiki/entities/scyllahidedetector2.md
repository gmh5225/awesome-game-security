---
title: ScyllaHideDetector2
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/samshine__ScyllaHideDetector2.md
updated: 2026-07-23
confidence: medium
---

# ScyllaHideDetector2

C/C++ **ScyllaHide Detector V2** sample that detects ScyllaHide anti-anti-debug use when a target is under debug and bytes are restored. Centers on hooking / debugging artifacts useful to anti-cheat engineers and defensive researchers studying the `Anti Cheat → Anti Debugging` lane against hide plugins (ScyllaHide / TitanHide / HyperHide class). (source: wiki/sources/descriptions/samshine__ScyllaHideDetector2.md)

Complements anti-debug technique catalogs such as [[makin]] and tool-presence detectors such as [[cedetector]]; pairs with the ScyllaHide-class hide/bypass surface covered under [[overviews/reverse-engineering]] anti-analysis.

## Links

- Repo: https://github.com/samshine/ScyllaHideDetector2

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[makin]] · [[cedetector]] · [[x64dbg]]
