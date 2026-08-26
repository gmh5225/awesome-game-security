---
title: PeVisor
kind: entity
topics: [reverse-engineering, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/Nitr0-G__PeVisor.md
updated: 2026-08-26
confidence: medium
---

# PeVisor

Early-stage **Windows PE analysis and instrumentation toolkit** (Nitr0-G; C/C++) centered on the **PeVisor** component. Integrates **[[blackbone]]** for process control, hooking, and memory mapping, plus **Unicorn** for emulation-oriented workflows. Includes sample targets and protection versus unprotection test material for binary experimentation. Primarily suited to advanced malware and game-security researchers exploring PE internals, runtime hooks, and emulator-assisted analysis. README tag: PE. (source: wiki/sources/descriptions/Nitr0-G__PeVisor.md)

Complements static PE tooling such as [[pe-bear]], live injection scanners such as [[pe-sieve]] / [[xmalhunter]], headerless reconstruction via [[pereconstruct]], and Unicorn PE instrumentation such as [[unicorn-pe]] in the Windows binary analysis lane.

## Links

- Repo: https://github.com/Nitr0-G/PeVisor (README tag: PE)

## Related

[[blackbone]] · [[pe-bear]] · [[pe-sieve]] · [[pereconstruct]] · [[unicorn-pe]] · [[modfinder]] · [[xmalhunter]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
