---
title: cs2-signature-list
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/Salvatore-Als__cs2-signature-list.md
updated: 2026-08-21
confidence: medium
---

# cs2-signature-list

Reference corpus (Salvatore-Als) of **Counter-Strike 2 function-signature notes** for locating internal game routines. Organized as Markdown documentation plus an **IDC helper script**, with separate pages for features such as team switching, item giving, chat handling, and damage-related routines. (source: wiki/sources/descriptions/Salvatore-Als__cs2-signature-list.md)

Rather than publishing fixed universal byte patterns, the project documents **string anchors** and guidance to refine signature searches across CS2 builds—useful when automated offset dumpers break after patches. Targets game reverse engineering, modding research, and maintaining offset/signature updates for security tooling. Listed under cheat / `[Signature]`.

Complements live offset feeds such as [[cs2-dumper]] and [[cs2-offsets]], educational Source 2 internals in [[cs2-internals]], and in-binary anticheat RE in [[cs2-anticheat]].

## Links

- Repo: https://github.com/Salvatore-Als/cs2-signature-list

## Related

[[cs2-dumper]] · [[cs2-offsets]] · [[cs2-offsets-ro0ti]] · [[cs2-internals]] · [[cs2-things]] · [[cs2-anticheat]] · [[hazedumper]] · [[gh-offset-dumper]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
