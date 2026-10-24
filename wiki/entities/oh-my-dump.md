---
title: Oh My Dump
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/nevergiveupcpp__oh-my-dump.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: medium
---

# Oh My Dump

IDA Pro **9.x plugin** that exports and re-applies reverse-engineering annotations when moving between older and newer builds of the same x86/x64 Windows binary. Serializes analysis into JSON built from byte signatures with wildcards, then locates matching code and data in a new IDB to restore names, type declarations, comments, background colors, and breakpoints. Pattern matching can follow RIP-relative and offset-based addressing so labels stay aligned across rebased or patched binaries. Implemented in C++20 with CMake and the IDA SDK. (source: wiki/sources/descriptions/nevergiveupcpp__oh-my-dump.md)

Suited to game-security analysts who need to preserve manual IDA work across frequent client or anti-cheat updates where FLIRT signatures or Lumina metadata alone do not carry full context. Complements [[ida-migrator]] IDB migration and [[binary-diffing]] build-to-build triage on [[overviews/reverse-engineering]].

## Links

- Repo: https://github.com/nevergiveupcpp/oh-my-dump

## Related

[[ida-migrator]] · [[binary-diffing]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
