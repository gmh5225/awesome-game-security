---
title: patch-finder
kind: entity
topics: [reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/momo5502__patch-finder.md
updated: 2026-07-29
confidence: medium
---

# patch-finder

IDA Pro plugin that detects **in-memory patches and hooks** by scanning executable memory regions of a running process and comparing them byte-by-byte against the corresponding on-disk PE image. Uses the IDA SDK for segment enumeration and a custom PE parser to align virtual addresses with file offsets, then highlights discrepancies in the disassembly view. (source: wiki/sources/descriptions/momo5502__patch-finder.md)

Useful for game-security researchers studying inline hooks, AC integrity checks, or live-vs-disk module tampering — complements runtime scanners such as [[xmalhunter]] and hook-integrity research such as [[hook-buster]].

## Links

- Repo: https://github.com/momo5502/patch-finder

## Related

[[kiroshi]] · [[xmalhunter]] · [[hook-buster]] · [[present-hook-detection]] · [[skiphook]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
