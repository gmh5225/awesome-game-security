---
title: emotet-deobfuscator
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/ElvisBlue__emotet-deobfuscator.md
updated: 2026-08-25
confidence: medium
---

# emotet-deobfuscator

**IDA Hex-Rays plugin** that deobfuscates **control-flow flattening** logic commonly seen in **Emotet** malware samples. Written in **Python** and built on the **IDA microcode API**, it identifies dispatcher registers, status values, and flattened branch patterns, then rewrites block transitions, inserts corrected jump targets, and cleans leftover dispatch instructions to produce clearer pseudocode. Primary use case is malware reverse engineering and analysis of heavily obfuscated binaries. (source: wiki/sources/descriptions/ElvisBlue__emotet-deobfuscator.md)

Scoped to Emotet-style CFF recovery inside IDA/Hex-Rays—not a general OLLVM unflattener. Complements broader Hex-Rays deobfuscation plugins such as [[hex-rays-deob]], [[hrtng]], and [[d810-ng]]. Same author as [[x64dbgpython]] (ElvisBlue). README category: IDA plugin to deobfuscate emotet CFF.

## Links

- Repo: https://github.com/ElvisBlue/emotet-deobfuscator

## Related

[[control-flow-flattening]] · [[hex-rays-deob]] · [[hrtng]] · [[d810-ng]] · [[pikabot-deobfuscator]] · [[x64dbgpython]] · [[overviews/reverse-engineering]]
