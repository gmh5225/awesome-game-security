---
title: mcrit-plugin
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/danielplohmann__mcrit-plugin.md
updated: 2026-08-16
confidence: medium
---

# mcrit-plugin

IDA Pro plugin that integrates with **MCRIT** (MinHash-based Code Recognition and Intelligence Toolkit) for binary function similarity matching and code recognition directly from the disassembler. Provides a GUI to upload samples, query function matches, browse similarity scores, and manage a MCRIT server connection within IDA. Aimed at malware analysts and reverse engineers performing large-scale binary code similarity analysis and function identification. (source: wiki/sources/descriptions/danielplohmann__mcrit-plugin.md)

Complements graph- and structure-based IDA diffing via [[diaphora]] and [[binexport]] by indexing functions with MinHash signatures against a shared MCRIT corpus—useful when hunting reused code across unrelated samples rather than diffing two known builds. Pairs with cross-build symbol browsers such as [[windiff]] and agent-oriented IDA automation via [[ida-pro-mcp]].

## Links

- Repo: https://github.com/danielplohmann/mcrit-plugin

## Related

[[overviews/reverse-engineering]] · [[diaphora]] · [[binexport]] · [[windiff]] · [[ida-pro-mcp]] · [[idaplugins]]
