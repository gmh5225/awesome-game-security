---
title: stripped-binary
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/keshav0045__stripped-binary.md
  - wiki/sources/README-categories.md
updated: 2026-10-29
confidence: medium
---

# stripped-binary

Docker-backed pipeline that trains and serves models to **predict original function names** from **Ghidra decompiler output** on symbol-stripped native binaries. Compiles open-source C at multiple optimization levels, pairs stripped/unstripped ELF twins for labels, and exports normalized headless Ghidra decompilation with leakage controls. Python covers dataset pairing, metrics, TF-IDF kNN baselines, optional LoRA on a code LLM, zero-shot API baselines, a FastAPI service, and a Ghidra script that applies ranked name suggestions with confidence scores. Targets analysts triaging packed game clients and anti-tamper builds where recovered identifiers accelerate manual RE. (source: wiki/sources/descriptions/keshav0045__stripped-binary.md)

## Links

- Repo: https://github.com/keshav0045/stripped-binary (README: Cheat / RE Tools — Ghidra plugin lane)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidrassist]] · [[binary-evidence]] · [[static-runtime-evidence]]
