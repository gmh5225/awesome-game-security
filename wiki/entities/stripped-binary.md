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

**stripped-binary** (keshav0045/stripped-binary) trains and serves models that suggest **original function names** for symbol-stripped native binaries from **Ghidra decompiler output**. Targets reverse engineers and binary analysts triaging packed **game clients**, anti-tamper builds, and other stripped ELF/PE workloads where recovered identifiers speed orientation and manual RE. (source: wiki/sources/descriptions/keshav0045__stripped-binary.md)

## Dataset pipeline

| Stage | Role |
|-------|------|
| Docker build farm | Compiles open-source C with **gcc** and **clang** at multiple optimization levels |
| ELF twins | Pairs stripped and unstripped binaries for ground-truth function labels |
| Ghidra export | Headless decompilation with normalization and **leakage controls** on training features |
| Python tooling | Dataset pairing, evaluation metrics, and reproducible train/eval splits |

## Models & delivery

| Component | Role |
|-----------|------|
| TF-IDF kNN | Baseline k-nearest-neighbor name suggestions from decompiler text |
| LoRA (optional) | Fine-tunes a code LLM on the paired corpus |
| API baselines | Zero-shot cloud LLM comparisons for benchmarking |
| FastAPI service | HTTP inference with ranked suggestions and confidence scores |
| Ghidra script | Applies ranked renames inside the analyst’s Ghidra session |

## Links

- Repo: https://github.com/keshav0045/stripped-binary (README: Cheat / RE Tools — Ghidra stripped-name inference)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[plugin-ghidra]] · [[reai-ida]] · [[ghidrassist]] · [[binary-evidence]] · [[static-runtime-evidence]]
