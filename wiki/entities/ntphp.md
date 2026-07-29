---
title: NtPhp
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/mrexodia__NtPhp.md
updated: 2026-07-29
confidence: medium
---

# NtPhp

Experimental **PHP interpreter embedded in Windows kernel drivers** — run PHP scripts from Ring0 WDK `.sys` modules instead of rebuilding C for every logic tweak. Listed under **Anti Cheat → Dynamic Script**; aimed at anti-cheat engineers and defensive kernel researchers prototyping driver-side policy without a full compile cycle. (source: wiki/sources/descriptions/mrexodia__NtPhp.md)

The upstream tagline is deliberately tongue-in-cheek: *“Ever wanted to execute PHP in your kernel driver? Look no further!”* Implementation is C/C++ kernel driver work (WDK). Pairs with other mrexodia driver/RE tooling such as [[titanhide]] and [[dumpulator]].

## Links

- Repo: https://github.com/mrexodia/NtPhp

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[wdutf]] · [[document]] · [[titanhide]]
