---
title: r2smt
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/seifreed__r2SMT.md
updated: 2026-08-12
confidence: medium
---

# r2smt

Rust toolkit integrating radare2 with SMT solvers (Z3, CVC5, Bitwuzla) to analyze conditional branches in compiled binaries. Lifts disassembly through a typed IR, backward slicing, and SSA before querying solvers for sound, fail-closed verdicts on opaque predicates, dead branches, and constant conditions. Supports x86, x86_64, AArch64, and AArch32 (Thumb); cross-checks lifting paths via differential equivalence checking; can annotate r2 sessions or apply reversible byte patches with rollback manifests. Batch mode sweeps directories with JSON/Markdown reports. Aimed at reverse engineers deobfuscating protected or tamper-resistant binaries, including game anti-cheat and malware workflows. (source: wiki/sources/descriptions/seifreed__r2SMT.md)

Not a full protector unpacker—focused on SMT-backed branch/obfuscation analysis and patch assist within the Cheat → Radare Plugins lane.

## Links

- Repo: https://github.com/seifreed/r2SMT

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[radius2]] · [[r2morph]] · [[opaque-predicates-detective]] · [[obfuscation-analysis]] · [[stp]]
