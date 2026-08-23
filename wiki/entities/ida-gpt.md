---
title: ida-gpt
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MayerDaniel__ida_gpt.md
updated: 2026-08-23
confidence: medium
---

# ida-gpt

Python IDAPython helper that connects IDA Pro disassembly workflows to a ChatGPT-compatible backend. Provides functions to request plain-language function descriptions and automated renaming suggestions for variables, locations, and function symbols. Designed for interactive use inside IDA, where generated outputs are written back into the database as comments and renamed identifiers—speeding triage and annotation of unfamiliar binaries for reverse engineering practitioners. (source: wiki/sources/descriptions/MayerDaniel__ida_gpt.md)

Complements other in-IDA ChatGPT assistants such as [[wpechatgpt]], [[daila]], [[binoculars]], and [[aida]]—verify model output against disassembly/decompilation per [[research-rigor]].

## Links

- Repo: https://github.com/MayerDaniel/ida_gpt

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[wpechatgpt]] · [[daila]] · [[binoculars]] · [[aida]] · [[ida-llm-explainer]] · [[research-rigor]]
