---
title: AntiDebugging
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/revsic__AntiDebugging.md
updated: 2026-07-24
confidence: medium
---

# AntiDebugging

C++ **anti-debugging technique** sample focused on debugger-resistance patterns for the `Anti Cheat → Anti Debugging` lane. Aimed at anti-cheat engineers and defensive researchers studying how protected clients detect or frustrate attached debuggers, rather than shipping as a production AC component. (source: wiki/sources/descriptions/revsic__AntiDebugging.md)

Complements Windows anti-debug catalogs such as [[makin]] (30+ API/PEB/HWBP/timing/TLS checks), Black Hat 2012 PoCs [[blackhat2012]], and ScyllaHide-class hide detection via [[scyllahidedetector2]]. Same author as VEH DBI sample [[cpp-veh-dbi]].

## Links

- Repo: https://github.com/revsic/AntiDebugging

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[makin]] · [[scyllahidedetector2]] · [[blackhat2012]] · [[cpp-veh-dbi]] · [[x64dbg]]
