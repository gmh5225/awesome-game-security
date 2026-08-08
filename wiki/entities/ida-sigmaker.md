---
title: ida-sigmaker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mahmoudimus__ida-sigmaker.md
  - wiki/sources/descriptions/gmh5225__ida-sigmaker.md
updated: 2026-08-08
confidence: medium
---

# ida-sigmaker

Two related IDA Pro signature-maker plugins share this name in the curated list. Both target reverse engineers who need durable byte patterns for function identification across binary versions—common in cheat/mod development and game-security RE.

## mahmoudimus/ida-sigmaker

Zero-dependency IDA Pro 9.0+ plugin for creating and searching unique byte-pattern signatures during reverse engineering. Written mainly in Python with optional Cython/SIMD speedups (AVX2, NEON, SSE2), it runs cross-platform on Windows, macOS, and Linux. (source: wiki/sources/descriptions/mahmoudimus__ida-sigmaker.md)

### Capabilities

- Generate the **shortest unique signature** for a function or selection
- Wildcard address-bearing operands; **XREF-based fallback** when byte patterns are ambiguous
- **Batch search** multiple patterns with text, CSV, or JSON output
- **Seed-then-refine** uniqueness algorithm plus optional native SIMD scanner for large-database searches

## gmh5225/ida-sigmaker

IDA Pro plugin for automatically generating byte-pattern signatures from selected disassembly. Creates IDA-style and code-style signature patterns with wildcards for variable bytes, ensuring uniqueness within the binary. Generated signatures support pattern scanning in cheat or mod development workflows. (source: wiki/sources/descriptions/gmh5225__ida-sigmaker.md)

Lighter-weight generation focus—no built-in search/SIMD stack like the mahmoudimus variant. See also [[sigmakerex]] for gmh5225's enhanced multi-format maker.

## Links

- Repo (mahmoudimus): https://github.com/mahmoudimus/ida-sigmaker
- Repo (gmh5225): https://github.com/gmh5225/ida-sigmaker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[sigmakerex]] · [[ida-fusion]] · [[yarascan-ida]] · [[patternsleuth]] · [[sig-database]]
