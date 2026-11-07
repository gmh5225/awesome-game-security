---
title: nvdisasm
kind: entity
topics: [reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/ioncodes__nvdisasm.md
updated: 2026-11-07
confidence: medium
---

# nvdisasm

Curated **NVIDIA GPU SASS** disassembler architecture definitions for decoding compiled **CUDA** and graphics **shader machine code**. Organized by GPU generation and streaming-multiprocessor (SM) version from **Kepler through Hopper**, with per-architecture machine descriptions, instruction encoding patterns, and execution-pipe latency tables in NVIDIA-style disassembler formats. Covers SASS mnemonics, register and predicate rules, **CUDA ELF** relocations, and validation conditions (including SASS-only encoding checks). Game-security and reverse-engineering analysts use these specs to inspect GPU kernels and shaders without depending solely on the proprietary CUDA toolkit disassembler. (source: wiki/sources/descriptions/ioncodes__nvdisasm.md)

Specification data—not a standalone GUI disassembler. Complements high-level GPU frame tools ([[gpu-inspector]], RenderDoc) and virtual-ISA plugins such as [[ptxninja]] (PTX in Binary Ninja); pairs with dynamic CUDA tracing via [[cutracer]] when runtime instruction evidence is required.

## Links

- Repo: https://github.com/ioncodes/nvdisasm

## Related

[[overviews/reverse-engineering]] · [[overviews/graphics-api]] · [[ptxninja]] · [[cutracer]] · [[gpu-inspector]]
