---
title: VALVeAntiCheat1
kind: entity
topics: [anti-cheat, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/shefben__VALVeAntiCheat1.md
updated: 2026-08-01
confidence: medium
---

# VALVeAntiCheat1

Reverse-engineered reconstruction of **Valve Anti-Cheat 1 (VAC1)** security modules from the GoldSrc and WON-era Half-Life period (~2002–2004). Documents and reimplements the original **ModuleC** (client) and **ModuleS** (server) architecture: thin native DLLs act as sandboxed bytecode virtual machines that receive detection programs over the network rather than embedding cheat scanners directly. (source: wiki/sources/descriptions/shefben__VALVeAntiCheat1.md)

Includes C++ source for the module framework and VM interpreter, Python utilities to decrypt/rebuild/repack on-the-wire VAC containers, and notes on blob encryption, engine callback interfaces, memory integrity checks, and the server-side UDP network layer. Visual Studio 6 project files target the original fixed-base PE layout. Aimed at game-security researchers and reverse engineers studying early commercial anti-cheat design and GoldSrc engine protection.

Historical VAC1 study complements modern VAC3 exploration tools such as [[vac3-dumper]], [[vac-module-dumper]], [[vackeyretrieval]], and [[vac3-inhibitor]].

## Links

- Repo: https://github.com/shefben/VALVeAntiCheat1

## Related

[[regamedll-cs]] · [[vac3-dumper]] · [[vac-module-dumper]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
