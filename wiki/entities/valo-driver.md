---
title: valo-driver
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__valo-driver.md
updated: 2026-08-07
confidence: medium
---

# valo-driver

Windows **kernel driver** (C) for reading Valorant process memory while evading [[vanguard]] kernel protections. Cross-process reads use **physical address translation**, **CR3 manipulation**, or **MDL mapping** instead of standard APIs Vanguard monitors — a kernel-mode external memory path for anti-cheat researchers studying Vanguard bypass vectors. (source: wiki/sources/descriptions/gmh5225__valo-driver.md)

Complements early-load samples such as [[valorant-esp-hack-with-driver]] and offset/SDK tooling ([[valorant-externals]], [[valorant-dumper]]) in the cheat / game:valorant lane; technique-wise sits beside generic CR3/MDL/phys-read research such as [[ntmemory]] and [[readphys]].

## Links

- Repo: https://github.com/gmh5225/valo-driver

## Related

[[vanguard]] · [[ntmemory]] · [[readphys]] · [[valorant-esp-hack-with-driver]] · [[valorant-externals]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
