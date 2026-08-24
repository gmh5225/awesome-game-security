---
title: IDA Gepetto
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/apkunpacker__IDA-Gepetto.md
updated: 2026-08-18
confidence: medium
---

# IDA Gepetto

IDA Pro plugin (apkunpacker fork) that queries **local language models** to explain decompiled functions and suggest better variable names. Built in Python for IDAPython, it integrates into the Hex-Rays pseudocode UI via context-menu actions and keyboard shortcuts. Configurable model backends and localization through plugin settings and translation files. Aimed at reverse engineers accelerating malware analysis and game-security research workflows inside IDA. (source: wiki/sources/descriptions/apkunpacker__IDA-Gepetto.md)

Distinct from the original [[gepetto]] (JusticeRage; cloud/local multi-provider ChatGPT-category plugin)—this fork focuses on offline local inference. Complements other local-LLM IDA assistants such as [[ida-llm-explainer]] and multi-provider dockable panels like [[idassist]] and [[rikugan]] rather than agent tool loops or MCP bridges.

## Links

- Repo: https://github.com/apkunpacker/IDA-Gepetto

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[gepetto]] · [[ida-llm-explainer]] · [[idassist]] · [[rikugan]] · [[ida-assistant]] · [[aida]] · [[research-rigor]]
