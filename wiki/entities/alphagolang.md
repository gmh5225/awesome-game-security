---
title: AlphaGolang
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/SentineLabs__AlphaGolang.md
updated: 2026-08-21
confidence: medium
---

# AlphaGolang

IDAPython script toolkit for analyzing Go (Golang) binaries in IDA Pro. Organized as a step-by-step workflow covering binary identification, pclntab recovery, function discovery, string handling, and type extraction. Includes a YARA rule for quickly spotting Go executables across PE, ELF, and Mach-O formats. Primary use case is malware and threat analysis where stripped or heavily optimized Go samples are difficult to read manually. (source: wiki/sources/descriptions/SentineLabs__AlphaGolang.md)

Complements in-IDA Go metadata plugins such as [[golang-loader-assist]], offline pclntab/moduledata extractors such as [[goresym]], and hands-on Go RE curriculum [[go-hacking]] when analysts need a scripted IDA workflow for stripped Go binaries.

## Links

- Repo: https://github.com/SentineLabs/AlphaGolang

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[golang-loader-assist]] · [[goresym]] · [[go-hacking]] · [[binoculars]]
