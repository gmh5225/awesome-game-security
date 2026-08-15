---
title: CUTracer
kind: entity
topics: [reverse-engineering, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/facebookresearch__CUTracer.md
updated: 2026-08-15
confidence: medium
---

# CUTracer

Dynamic binary instrumentation tool for **tracing and analyzing CUDA kernel instructions**. Separates lightweight GPU-side data collection (instrumentation) from host-side processing (analysis). Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / DBI lane — runtime CUDA kernel visibility rather than static PTX disassembly. (source: wiki/sources/descriptions/facebookresearch__CUTracer.md)

Complements static GPU virtual-ISA tooling such as [[ptxninja]] and broader DBI frameworks covered under [[dynamic-binary-instrumentation]].

## Links

- Repo: https://github.com/facebookresearch/CUTracer

## Related

[[ptxninja]] · [[dynamic-binary-instrumentation]] · [[tinyinst]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
