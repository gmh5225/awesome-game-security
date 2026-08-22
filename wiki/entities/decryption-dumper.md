---
title: DecryptionDumper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Nuxar1__DecryptionDumper.md
updated: 2026-08-22
confidence: medium
---

# DecryptionDumper

Windows **C++ decryption routine dumper** (Nuxar1; cheat / `[Dump]`) that traces and reconstructs **encrypted pointer logic** at runtime. Launches a target under a debugger, **single-steps** instructions, and uses **Zydis**-based disassembly to track register and stack dependencies until decryption output resolves. Includes **pattern scanning**, **context restoration**, and **instruction filtering** to produce cleaner recovered instruction flows. Primarily useful for reverse engineering protected game binaries and studying anti-cheat-protected decryption behavior. (source: wiki/sources/descriptions/Nuxar1__DecryptionDumper.md)

Complements static decrypt IDA plugins such as [[ida-jm-xorstr-decrypt-plugin]] and title-specific `.text`/pointer decrypt samples such as [[league-unpacker]]. Pairs with debugger-assisted tracing peers such as [[veh-dumper]] and [[x64dbg]], and offset/pattern workflows such as [[gh-offset-dumper]] when turning recovered routines into reusable decrypt helpers for externals.

## Links

- Repo: https://github.com/Nuxar1/DecryptionDumper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[veh-dumper]] · [[gh-offset-dumper]] · [[league-unpacker]] · [[ida-jm-xorstr-decrypt-plugin]] · [[mixed-boolean-arithmetic]]
