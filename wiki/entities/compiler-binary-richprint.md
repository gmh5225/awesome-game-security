---
title: compiler-binary-richprint
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__compiler-binary-richprint.md
updated: 2026-08-09
confidence: medium
---

# compiler-binary-richprint

Utility that **prints compiler information** stored in the **Rich Header** of a Windows PE executable. The Rich Header sits between the legacy MZ/DOS stub and the PE signature—an undocumented MSVC linker artifact listing toolchain object IDs and build counts that triage analysts use to fingerprint how a binary was produced. (source: wiki/sources/descriptions/gmh5225__compiler-binary-richprint.md)

Useful for game-security researchers and reverse engineers studying offensive techniques in the cheat / RE tools lane—quickly confirming whether a game client, cheat module, or injected DLL was built with a particular Visual Studio / linker generation before deeper IDA/Ghidra work. Complements PE viewers such as [[pe-bear]] and [[totalpe2]], compiler/packer ID tools such as [[nauz-file-detector]], and PE literacy guides such as [[underthehoodofexecutables]].

## Links

- Repo: https://github.com/gmh5225/compiler-binary-richprint

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[pe-bear]] · [[totalpe2]] · [[nauz-file-detector]] · [[underthehoodofexecutables]]
