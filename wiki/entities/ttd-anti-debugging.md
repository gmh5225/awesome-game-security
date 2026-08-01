---
title: TtdAntiDebugging
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/liors619__TtdAntiDebugging.md
updated: 2026-08-01
confidence: medium
---

# TtdAntiDebugging

C/C++ **debug testing** sample centered on **hooking and debugging** workflows for the `Cheat → Debug Testing` lane. Aimed at anti-cheat engineers and defensive security researchers stress-testing anti-debug / debugger-detection behavior under analysis, rather than shipping as a production AC component. (source: wiki/sources/descriptions/liors619__TtdAntiDebugging.md)

The repo name implies **Time Travel Debugging (TTD)**-oriented anti-debug study — exercising how protected clients or AC probes behave when recorded or replayed under WinDbg-class debug tooling alongside conventional hooking surfaces.

Complements anti-debug technique catalogs such as [[makin]], C++ samples such as [[anti-debugging]], and ScyllaHide-class hide detection via [[scyllahidedetector2]].

## Links

- Repo: https://github.com/liors619/TtdAntiDebugging

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[makin]] · [[anti-debugging]] · [[scyllahidedetector2]] · [[windbg-scripts]] · [[x64dbg]]
