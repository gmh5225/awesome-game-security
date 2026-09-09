---
title: Binary Diffing
kind: concept
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/joxeankoret__diaphora.md
updated: 2026-09-09
confidence: high
---

# Binary Diffing

Structural and semantic comparison of binary builds for patch analysis, anti-cheat driver update tracking, obfuscated-client logic isolation, and vulnerability research. Diff output is **candidate evidence**—corroborate claimed semantic changes before assigning security impact. (source: wiki/sources/skills/reverse-engineering.md)

## Corpus tools

| Tool | Role |
|------|------|
| BinDiff | Graph-based structural function/basic-block comparison |
| [[diaphora]] | IDA-based program comparison; match quality requires validation |
| [[ghidriff]] | Ghidra-based diffing; command-line and scriptable |
| DarunGrim | Patch-analysis-focused differ |
| [[turbodiff]] | Lightweight IDA diffing plugin |

Game-security uses include tracking anti-cheat driver updates between versions, reviewing changed behavior and trust-boundary assumptions in supplied builds, and comparing obfuscated builds to isolate logic changes.

## Evidence limits

A comparative quality ranking requires a specified benchmark and independently checked matches. Preserve:

- Tool and host disassembler versions
- Both input hashes
- Architecture and compiler/optimization context
- Unmatched functions and alignment/layout-only changes

Similarity scores and decompiled differences suggest where to look—they do not alone establish exploitability, bypass feasibility, or enforcement impact. Pair diff hits with [[binary-evidence]] reachability/observation checks and [[research-rigor]] reconciliation when layers disagree.

[[diaphora]] maintainer documentation describes an IDA-based diffing workflow; treat exported match lists as hypotheses until validated on representative builds. (source: wiki/sources/descriptions/joxeankoret__diaphora.md)

## Related

[[binary-evidence]] · [[research-rigor]] · [[diaphora]] · [[ghidriff]] · [[turbodiff]] · [[mixed-boolean-arithmetic]] · [[control-flow-flattening]] · [[overviews/reverse-engineering]]
