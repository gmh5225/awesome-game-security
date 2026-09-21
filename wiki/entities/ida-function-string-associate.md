---
title: ida-function-string-associate
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__ida-function-string-associate.md
  - wiki/sources/descriptions/partoftheworlD__GHIDRApy_FunctionStringAssociate.md
updated: 2026-09-21
confidence: medium
---

# ida-function-string-associate

IDA Pro 9.X plugin that associates string references with functions: it scans function bodies for string-reference operands and builds a navigable summary showing which literals each function touches. Auto-generates function comments from those string literals so analysts can infer purpose quickly during large binary triage. (source: wiki/sources/descriptions/gmh5225__ida-function-string-associate.md)

String-centric function identification—not rename automation, call graphs, or decompiler output. Ghidra-side counterpart [[ghidrapy-functionstringassociate]] mirrors this workflow with a node-based string-ref walk and repeatable function comments. (source: wiki/sources/descriptions/partoftheworlD__GHIDRApy_FunctionStringAssociate.md) Complements [[ida-names]] (symbol naming), [[ida-export-functions]] (function-list Markdown export), and [[idawilli]] string-decrypt automation when the goal is rapid “what strings does this function use?” orientation.

## Links

- Repo: https://github.com/gmh5225/ida-function-string-associate

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidrapy-functionstringassociate]] · [[ida-names]] · [[ida-export-functions]] · [[idawilli]] · [[idaplugins-list]]
