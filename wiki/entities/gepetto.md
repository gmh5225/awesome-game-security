---
title: Gepetto
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/JusticeRage__Gepetto.md
updated: 2026-08-24
confidence: medium
---

# Gepetto

Python IDAPython plugin for IDA Pro that uses large language models to explain decompiled functions and suggest variable renames and code comments directly from Hex-Rays pseudocode. Integrates via menu actions and hotkeys; supports multiple cloud and local model providers through configuration. Aimed at reverse engineers who want faster code comprehension in malware, software, and game-security analysis workflows. (source: wiki/sources/descriptions/JusticeRage__Gepetto.md)

Complements other cloud-LLM IDA assistants such as [[wpechatgpt]], [[ida-gpt]], and [[daila]], local/offline tooling like [[ida-llm-explainer]] and [[ida-gepetto]] (apkunpacker fork), and agent bridges like [[ida-mcp-server-plugin]]—verify model output against disassembly/decompilation per [[research-rigor]].

## Links

- Repo: https://github.com/JusticeRage/Gepetto

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[wpechatgpt]] · [[ida-gpt]] · [[ida-llm-explainer]] · [[ida-gepetto]] · [[idassist]] · [[research-rigor]]
