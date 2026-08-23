---
title: BEClient
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/LilPidgey__BEClient.md
updated: 2026-08-23
confidence: medium
---

# BEClient

Small C++ proof-of-concept client (LilPidgey) that demonstrates how to initialize and call the [[battleye]] in-process client DLL interface. It defines game and anti-cheat data structures, registers callback functions, and invokes exported routines such as run, command, and exit handlers. The Visual Studio Windows project includes structure headers for client communication fields. Primary use case is reverse engineering and research on anti-cheat client integration behavior inside game processes. (source: wiki/sources/descriptions/LilPidgey__BEClient.md)

Complements full protocol emulators such as [[be-emulator]] and service/install shims such as [[fakeeye]] with a minimal, structure-accurate scaffold focused on the game↔BEClient DLL contract rather than bypass or title-specific tooling like [[arma3beclient]].

## Links

- Repo: https://github.com/LilPidgey/BEClient

## Related

[[battleye]] · [[be-emulator]] · [[fakeeye]] · [[arma3beclient]] · [[battleye-decryption]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
