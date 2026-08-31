---
title: BinaryLens
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Berk000x__BinaryLens.md
updated: 2026-08-31
confidence: medium
---

# BinaryLens

IDA Pro plugin that uses large language models to accelerate reverse-engineering workflows on large binaries. Supports bulk function renaming, explaining binary logic from decompiler context, and renaming local variables directly in Hex-Rays views. Implemented in C++ with the IDA SDK and OpenSSL integration; supports multiple model backends for analysis tasks. Aimed at analysts working on game clients and anti-cheat modules where manual triage of huge IDBs is slow. (source: wiki/sources/descriptions/Berk000x__BinaryLens.md)

Rename-and-explain focus complements broader copilots such as [[aether]] and [[idassist]] (chat, RAG, vulnerability analysis) and local HITL assistants such as [[ida-llm-explainer]] (llama.cpp with explicit accept before DB writes). Peers with cloud rename/explain plugins like [[ida-gpt]] and [[gepetto]] in the Cheat IDA Plugins / LLM-assistant lane.

## Links

- Repo: https://github.com/Berk000x/BinaryLens

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[aether]] · [[ida-llm-explainer]] · [[ida-gpt]] · [[gepetto]] · [[idassist]] · [[idaplugins]]
