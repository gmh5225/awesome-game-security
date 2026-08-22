---
title: AngryGhidra
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Nalen98__AngryGhidra.md
updated: 2026-08-22
confidence: medium
---

# AngryGhidra

**Ghidra extension** that embeds **angr symbolic execution** into interactive reverse-engineering workflows. Analysts set **start**, **find**, and **avoid** addresses, launch symbolic exploration from the Ghidra UI, and apply **patched bytes** back into the analysis database. The plugin uses **Java** for Ghidra integration and **Python** with **angr** and **claripy** for analysis automation. Intended for CTF solving, malware and binary research, and general software or game reverse engineering where path constraints and automated patching accelerate triage. (source: wiki/sources/descriptions/Nalen98__AngryGhidra.md)

Complements standalone angr tooling such as [[angrop]] and [[oxidizer]] by bridging symbolic exploration into Ghidra's disassembly/decompiler context—similar in spirit to Binary Ninja symbolic plugins like [[seninja]] and multi-backend harnesses like [[smallworld]].

## Links

- Repo: https://github.com/Nalen98/AngryGhidra

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[ghidra-bridge]] · [[angrop]] · [[oxidizer]] · [[seninja]] · [[smallworld]] · [[decbench]]
