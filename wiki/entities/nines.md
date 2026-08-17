---
title: NineS
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/buzzer-re__NineS.md
updated: 2026-08-17
confidence: medium
---

# NineS

**PlayStation 5 ELF injector** that manually maps ELF payloads into remote PS5 processes and executes them in remote threads. C codebase built on John Törnblom's PS5 SDK; exposes a TCP server on port **9033** accepting a target process name plus ELF binary, then performs manual mapping (section load, relocations, thread creation). Includes a Python helper for sending injection payloads. Aimed at console security researchers studying PS5 process injection, ELF manual mapping, and remote code execution on FreeBSD-based game consoles. (source: wiki/sources/descriptions/buzzer-re__NineS.md)

Unlike static RE loaders ([[ida-ps5-elf-plugin]], [[elfloader]]), NineS is a live runtime injector into already-running game/system processes on jailbroken PS5 hosts.

## Links

- Repo: https://github.com/buzzer-re/NineS

## Related

[[ps5-linux-loader]] · [[ida-ps5-elf-plugin]] · [[a53-code-exec]] · [[elfloader]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
