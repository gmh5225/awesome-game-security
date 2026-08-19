---
title: WPeChatGPT
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/WPeace-HcH__WPeChatGPT.md
updated: 2026-08-19
confidence: medium
---

# WPeChatGPT

IDA Pro plugin that uses large language models to assist binary analysis workflows inside the disassembler. Written in Python (IDAPython), it integrates with OpenAI-compatible APIs to explain function behavior, rename variables, attempt Python reconstructions of small routines, and run vulnerability-oriented checks from decompiled views. An automated mode traverses function trees and summarizes findings. Aimed at reverse engineers and game-security researchers who want AI-assisted triage inside IDA. (source: wiki/sources/descriptions/WPeace-HcH__WPeChatGPT.md)

Complements other cloud-LLM IDA assistants such as [[vulchatgpt]], [[daila]], and [[ida-plugin-pcodegpt]], and local/offline tooling like [[ida-llm-explainer]] and [[ida-gepetto]]—verify model output against disassembly/decompilation per [[research-rigor]].

## Links

- Repo: https://github.com/WPeace-HcH/WPeChatGPT

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vulchatgpt]] · [[daila]] · [[ida-plugin-pcodegpt]] · [[ida-llm-explainer]] · [[ida-gepetto]] · [[idassist]] · [[research-rigor]]
