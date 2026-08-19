---
title: Anti-Debugger-Protector-Loader
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/YouNeverKnow00__Anti-Debugger-Protector-Loader.md
updated: 2026-08-19
confidence: medium
---

# Anti-Debugger-Protector-Loader

Windows **C++ anti-debugging and protection** example from YouNeverKnow00 for the `Anti Cheat → Anti Debugging` lane. Continuously scans for debugger executables, window titles, and related drivers; bundles multiple debugger-detection checks with optional automatic termination. Configurable scan intervals and optional protection actions; includes **VMProtect SDK** integration artifacts. Main audience: software-protection and game-security researchers studying practical anti-debug patterns. (source: wiki/sources/descriptions/YouNeverKnow00__Anti-Debugger-Protector-Loader.md)

Complements passive technique catalogs such as [[makin]] and [[anti-debugging]], bypass practice labs such as [[gh-anti-debug-bypass-practice-tool]], and commercial packer integration study via [[vmprotect]].

## Links

- Repo: https://github.com/YouNeverKnow00/Anti-Debugger-Protector-Loader

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[makin]] · [[anti-debugging]] · [[gh-anti-debug-bypass-practice-tool]] · [[vmprotect]] · [[kernelmode-dll-injector]] · [[scyllahidedetector2]] · [[x64dbg]]
