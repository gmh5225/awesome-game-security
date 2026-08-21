---
title: unxorer
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/SamuelTulach__unxorer.md
updated: 2026-08-21
confidence: medium
---

# unxorer

IDA Pro/Home plugin (C++) that recovers **stack strings** from obfuscated binaries through **Unicorn** emulation. The plugin explores branching paths, preserves emulation state, and scans stack data for decoded text. Configurable starting points and output navigation integrate the workflow directly into IDA. Useful for malware and game-security analysis where stack-string obfuscation is common. (source: wiki/sources/descriptions/SamuelTulach__unxorer.md)

## Links

- Repo: https://github.com/SamuelTulach/unxorer

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-jm-xorstr-decrypt-plugin]] · [[anti-xorstr]] · [[ripr]] · [[unicorn-pe]]
