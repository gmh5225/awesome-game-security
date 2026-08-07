---
title: qiling-il2cpp-dump
kind: entity
topics: [game-engine, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__qiling-il2cpp-dump.md
updated: 2026-08-07
confidence: medium
---

# qiling-il2cpp-dump

Unity [[il2cpp]] metadata dumper that uses the **Qiling** emulation framework to extract class definitions, method addresses, and type information **without launching the game**. It emulates IL2CPP runtime initialization inside Qiling's sandbox, triggers metadata registration, then dumps the recovered structures. Targets obfuscated or anti-tamper protected IL2CPP binaries where static metadata-only dumpers fail. (source: wiki/sources/descriptions/gmh5225__qiling-il2cpp-dump.md)

Complements static dumpers such as [[il2cppdumper]], reflection-driven [[il2cpp-runtime-dumper]], and live Frida bridges such as [[frida-il2cpp-bridge]] when analysts need emulation-based metadata recovery on hardened Unity builds.

## Links

- Repo: https://github.com/gmh5225/qiling-il2cpp-dump

## Related

[[il2cpp]] · [[il2cppdumper]] · [[il2cpp-runtime-dumper]] · [[frida-il2cpp-bridge]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
