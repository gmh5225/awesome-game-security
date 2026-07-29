---
title: TitanHide
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrexodia__TitanHide.md
updated: 2026-07-29
confidence: medium
---

# TitanHide

Windows **kernel driver** that hides debuggers from selected processes by hooking **Nt*** kernel routines via **SSDT table hooks** and tampering with return values seen by the target. Aimed at game-security researchers and reverse engineers studying offensive anti-debug / cheat-debugging lanes. (source: wiki/sources/descriptions/mrexodia__TitanHide.md)

Complements usermode ScyllaHide-class plugins; defensive detection samples such as [[scyllahidedetector2]] target the broader hide-plugin surface. Pairs with anti-debug catalogs ([[makin]], [[anti-debugging]]) and SSDT inspection tools ([[openark]]).

## Links

- Repo: https://github.com/mrexodia/TitanHide

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[scyllahidedetector2]] · [[makin]] · [[anti-debugging]] · [[openark]] · [[x64dbg]]
