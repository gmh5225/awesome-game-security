---
title: ida-sigmaker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mahmoudimus__ida-sigmaker.md
updated: 2026-07-31
confidence: medium
---

# ida-sigmaker

Zero-dependency IDA Pro 9.0+ plugin for creating and searching unique byte-pattern signatures during reverse engineering. Written mainly in Python with optional Cython/SIMD speedups (AVX2, NEON, SSE2), it runs cross-platform on Windows, macOS, and Linux. (source: wiki/sources/descriptions/mahmoudimus__ida-sigmaker.md)

## Capabilities

- Generate the **shortest unique signature** for a function or selection
- Wildcard address-bearing operands; **XREF-based fallback** when byte patterns are ambiguous
- **Batch search** multiple patterns with text, CSV, or JSON output
- **Seed-then-refine** uniqueness algorithm plus optional native SIMD scanner for large-database searches

Primary audience: reverse engineers and game-security practitioners who need durable in-IDA code signatures for analysis, tooling, or anti-cheat-related workflows.

## Links

- Repo: https://github.com/mahmoudimus/ida-sigmaker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-fusion]] · [[yarascan-ida]] · [[patternsleuth]] · [[sig-database]]
