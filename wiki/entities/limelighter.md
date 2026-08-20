---
title: Limelighter
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Tylous__Limelighter.md
updated: 2026-08-20
confidence: medium
---

# Limelighter

Go command-line tool for generating and applying code-signing certificates on Windows binaries. Builds spoofed certificate material from domain certificate metadata, packages keys into PFX files, and signs executables or DLLs through external signing utilities. Also supports signing with operator-supplied valid certificates. Primary use case is red-team signing experiments and defensive research into trust and EDR detection behavior. README category: Fake Cert. (source: wiki/sources/descriptions/Tylous__Limelighter.md)

Contrasts with devkit-only fake cert synthesis via [[lazy-sign]], structurally invalid Authenticode injection via [[fakesign]], signature transplantation via [[sigthief]], and in-place signed-PE patching via [[sigflip]]: here the focus is programmatic cert generation from domain metadata plus flexible signing through external tools.

## Links

- Repo: https://github.com/Tylous/Limelighter

## Related

[[lazy-sign]] · [[fakesign]] · [[sigthief]] · [[sigflip]] · [[osslsigncode]] · [[magic-signer]] · [[pesign-analyzer]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
