---
title: bsimvis
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MISP__bsimvis.md
updated: 2026-08-23
confidence: medium
---

# bsimvis

Binary similarity analysis platform built on Ghidra and its BSim (Behavioral Similarity) plugin. Compares decompiled functions and feature vectors across large binary corpora, storing decompiled code and metadata in a Kvrocks-backed database with Redis job queues and optional Milvus vector search. Exposes a REST API and web UI for score-filtered similarity search, BSim-based function diffing, HDBSCAN family clustering with dendrogram visualization, call-graph navigation, tagging, analyst notes, and optional local LLM summaries. Written primarily in Python with a JavaScript frontend; targets reverse engineers and malware analysts who need scalable cross-binary similarity beyond Ghidra's built-in BSim database—including AC client/driver variant tracking and obfuscated build comparison. (source: wiki/sources/descriptions/MISP__bsimvis.md)

Complements headless Ghidra diffing via [[ghidriff]] and IDA-centric pipelines such as [[diaphora]], [[ida-multi-mcp]], and [[mcrit-plugin]] for corpus-scale function matching.

## Links

- Repo: https://github.com/MISP/bsimvis

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidriff]] · [[ghidra-mcp]] · [[diaphora]] · [[ida-multi-mcp]]
