---
title: Android-MemoryTool
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Android-MemoryTool.md
updated: 2026-08-15
confidence: medium
---

# Android-MemoryTool

Single-header C/C++ library for reading and writing process memory on Android through `/proc/pid/mem`, exposing a minimal API for runtime memory inspection and modification of target application processes without requiring ptrace attachment. Listed in the Cheat / RPM lane for game-security researchers building root-assisted external memory tools. (source: wiki/sources/descriptions/gmh5225__Android-MemoryTool.md)

Complements full memory editors such as [[android-mem-edit]], CLI scanners such as [[cheap-engine]] and [[mypower]], and driver/socket IPC kits such as [[root-socket-kit]] and [[rwmem]] when the workflow is a lightweight embeddable `/proc/pid/mem` primitive rather than a GUI scanner or kernel driver.

## Links

- Repo: https://github.com/gmh5225/Android-MemoryTool

## Related

[[android-mem-edit]] · [[cheap-engine]] · [[mypower]] · [[root-socket-kit]] · [[rwmem]] · [[android-cheat-template]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
