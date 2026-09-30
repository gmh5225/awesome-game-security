---
title: ida-zh-cn
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/3641397194-wq__ida-zh-cn.md
  - wiki/sources/README-categories.md
updated: 2026-09-30
confidence: medium
---

# ida-zh-cn

Runtime **Simplified-Chinese localization plugin** for **IDA Pro 9.x** that translates the disassembler interface without patching IDA binaries or installation files. Implemented as an IDAPython plugin using Python with PyQt5 and Qt5, it applies paint-time translation through `QProxyStyle` for menus, tabs, and headers while leaving widget identifiers in English so IDAPython scripts and other plugins continue to work. (source: wiki/sources/descriptions/3641397194-wq__ida-zh-cn.md)

## Scope

- **Target:** IDA Pro 9.x on Windows, macOS, and Linux
- **Implementation:** IDAPython, PyQt5/Qt5, `QProxyStyle` paint-time translation
- **Category:** Cheat / RE Tools (README)
- **Dictionary:** ~1860 bundled entries; user overrides; logging of untranslated strings
- **Features:** one-click toggle restores full English UI; install scripts for all three platforms

Localization tooling for reverse engineers and game security researchers who want a Chinese interface without breaking automation or analysis workflows—parallel to visual comfort plugins such as [[idapro-muils]], [[ida-dark-plus]], and [[ida-nord-theme]].

## Links

- Repo: https://github.com/3641397194-wq/ida-zh-cn

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idapro-muils]] · [[ida-settings]] · [[ida-plugin-repository]] · [[list-of-ida-plugins]]
