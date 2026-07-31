---
title: GoReSym
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mandiant__GoReSym.md
updated: 2026-07-31
confidence: medium
---

# GoReSym

Mandiant tool for extracting function metadata and type information from Go binaries. Parses the Go runtime's pclntab (PC line table) and moduledata structures to recover function names, source file paths, and type definitions even from stripped Go executables. Outputs recovered symbols in a format compatible with IDA Pro and other disassemblers. Aimed at malware analysts and reverse engineers restoring symbol information in stripped Go binaries. (source: wiki/sources/descriptions/mandiant__GoReSym.md)

Complements hands-on Go RE curriculum [[go-hacking]] and Mandiant .NET tooling such as [[dncil]].

## Links

- Repo: https://github.com/mandiant/GoReSym

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[go-hacking]] · [[dncil]] · [[symless]] · [[idadeflat]]
