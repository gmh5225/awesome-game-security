---
title: gnn-deobfuscation
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/LostOxygen__gnn_deobfuscation.md
updated: 2026-08-23
confidence: medium
---

# gnn-deobfuscation

**Graph Neural Network (GNN)** approach to deobfuscating **Mixed Boolean-Arithmetic (MBA)** expressions. Python codebase with training and testing pipelines; datasets span multiple MBA obfuscators (**Loki**, **MBABlast**, **MBAObfuscator**), organized by variable count and operation depth. Targets deobfuscation researchers and security analysts exploring machine-learning simplification of obfuscated arithmetic. (source: wiki/sources/descriptions/LostOxygen__gnn_deobfuscation.md)

Complements algebraic simplifiers ([[mba]], [[mbased]], [[cobra]]), synthesis tools ([[promba]], [[qsynthesis]]), and interactive tooling ([[mba-wasm]]).

## Links

- Repo: https://github.com/LostOxygen/gnn_deobfuscation

## Related

[[mixed-boolean-arithmetic]] · [[overviews/reverse-engineering]] · [[mba]] · [[mbased]] · [[cobra]] · [[promba]] · [[qsynthesis]] · [[mba-wasm]] · [[mba-obfuscator]] · [[mutaben]]
