---
title: Gemini-Genius
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Jackiemin233__Gemini-Genius.md
updated: 2026-08-24
confidence: medium
---

# Gemini-Genius

Python toolkit for binary function similarity analysis using graph-based embeddings. Combines dataset preprocessing scripts, model training code, and inference utilities that operate on CFG and ACFG representations extracted with IDA. The workflow covers graph generation, embedding export, and similarity search between candidate functions—intended for reverse engineering and vulnerability research such as cross-binary function matching. Includes an IDA Python 3 plugin for binary file similarity comparison. (source: wiki/sources/descriptions/Jackiemin233__Gemini-Genius.md)

Complements MinHash and BSim pipelines such as [[mcrit-plugin]], [[bsimvis]], and [[ida-multi-mcp]], and graph diffing tools such as [[diaphora]] and [[ghidriff]] for AC client/driver variant tracking and obfuscated build comparison.

## Links

- Repo: https://github.com/Jackiemin233/Gemini-Genius

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[diaphora]] · [[mcrit-plugin]] · [[bsimvis]] · [[ida-multi-mcp]] · [[ghidriff]]
