---
title: ida-slides
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/hyuunnn__ida-slides.md
updated: 2026-08-05
confidence: medium
---

# ida-slides

IDA Pro plugin (IDA 9.2+, Python) that renders **Marp or Slidev** slide decks in a dockable IDA tab for live reverse-engineering presentations. Slides and the IDB stay linked both ways: `@name` and `@0xADDR` tokens jump to disassembly or Hex-Rays pseudocode, and range syntax can embed live decompiled lines into the deck on each save. Hover previews of decompiled excerpts, a right-click action to copy `@reference` tokens from IDA views, deck lint for unresolved references, and live reload via a file watcher keep walkthroughs synchronized with the database. Rendering uses native OS webviews (WKWebView on macOS, WebView2 on Windows) with the Marp or Slidev CLI so the deck stays beside disassembly rather than in an external browser. Aimed at reverse engineers who want to present or walk through analysis while staying inside IDA. (source: wiki/sources/descriptions/hyuunnn__ida-slides.md)

Presentation and documentation tooling—complements capture/annotation plugins such as [[ida-screenshot]] and [[draw-ida]] rather than performing binary analysis itself.

## Links

- Repo: https://github.com/hyuunnn/ida-slides

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-screenshot]] · [[draw-ida]] · [[idaplugins]]
