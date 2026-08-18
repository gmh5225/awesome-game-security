---
title: Unpacker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/anpa1200__Unpacker.md
updated: 2026-08-18
confidence: medium
---

# Unpacker

Modular **Python 3.10+** tool that **detects and unpacks packed malware samples** so analysts can reach real code, imports, and strings for static analysis. Combines multi-method packer identification — section names, entropy analysis, heuristics, and optional signatures — for **PE and ELF** binaries, then routes each sample to a pluggable unpacker module. Supported techniques include native **UPX** decompression, **Unipacker**-based Unicorn emulation for 32-bit **ASPack**, **Themida**, and **VMProtect**, and **Qiling** emulation for 64-bit VMProtect, with optional multi-layer re-detection and PE rebuilding. Provides a single CLI pipeline from detection through unpacking and validation, aimed at malware analysts, threat-intelligence workflows, and reverse engineers working on packed executables in defensive security contexts. (source: wiki/sources/descriptions/anpa1200__Unpacker.md)

Complements emulation-based generic unpackers such as [[xvolkolak]] and VMP-focused tools such as [[vmpunpacker]] / [[vmpunpack]] by offering a unified Python pipeline with pluggable packer modules and both PE/ELF coverage.

## Links

- Repo: https://github.com/anpa1200/Unpacker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[xvolkolak]] · [[vmpunpacker]] · [[vmpunpack]] · [[unlicense]] · [[magicmida-rs]] · [[unicorn-pe]]
