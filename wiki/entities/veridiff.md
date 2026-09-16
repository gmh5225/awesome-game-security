---
title: Veridiff
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Veridiff__Veridiff.md
  - wiki/sources/README-categories.md
updated: 2026-09-16
confidence: medium
---

# Veridiff

Frida **Stalker dual-trace** engine that finds the exact conditional branch where two executions of the same native code first diverge. Traces basic-block sequences from two runs, applies longest-common-prefix diff, and uses in-agent Capstone disassembly to pinpoint the deciding cmp/jump/branch. Ships as matching Python and Rust APIs with OLLVM-style CFF resync heuristics, optional warm-up to skip dynamic-linker false positives, and x86/ARM64 branch classification. Targets license checks, anti-cheat heuristics, and other obfuscated control flow where manual trace comparison does not scale. (source: wiki/sources/descriptions/Veridiff__Veridiff.md)

## How it works

- **Dual trace:** Frida Stalker records basic-block paths from two controlled runs of the same native function or region.
- **Diff:** Longest-common-prefix comparison isolates the first diverging basic block.
- **Pinpoint:** Capstone disassembly inside the agent identifies the branch instruction responsible.
- **OLLVM/CFF:** Resync heuristics help when control-flow flattening causes trace alignment drift.
- **APIs:** Python module and Rust crate with identical interfaces for automation pipelines.

Listed in README **Cheat → Frida** beside stealth-server builds and Stalker-based metadata tools such as [[il2cpp-re]].

## Links

- Repo: https://github.com/Veridiff/Veridiff

## Related

[[frida]] · [[il2cpp-re]] · [[control-flow-flattening]] · [[dynamic-binary-instrumentation]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
