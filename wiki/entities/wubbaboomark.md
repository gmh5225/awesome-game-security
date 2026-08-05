---
title: WubbabooMark
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/hfiref0x__WubbabooMark.md
updated: 2026-08-05
confidence: medium
---

# WubbabooMark

**Debugger trace detector** aimed at finding evidence of software debugger use and of anti-anti-debug tooling that hides debugger presence by tampering with aspects of the program environment. Targets the common Windows RE stack—Ghidra, IDA, OllyDbg, x32dbg/x64dbg, WinDbg—and hide-plugin class artifacts rather than shipping as a production anti-cheat component. Mainly useful for anti-cheat engineers and defensive security researchers in the anti-cheat / anti-debugging lane. (source: wiki/sources/descriptions/hfiref0x__WubbabooMark.md)

Complements technique catalogs such as [[makin]] and [[anti-debugging]], hide-detection samples such as [[scyllahidedetector2]], and offensive hide/bypass tooling (ScyllaHide / TitanHide / HyperHide class) covered under [[overviews/reverse-engineering]] anti-analysis.

## Links

- Repo: https://github.com/hfiref0x/WubbabooMark

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[makin]] · [[scyllahidedetector2]] · [[anti-debugging]] · [[x64dbg]]
