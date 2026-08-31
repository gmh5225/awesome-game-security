---
title: AETHER
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/CSIT-SG__AETHER.md
updated: 2026-08-29
confidence: medium
---

# AETHER

IDA Pro plugin that integrates large language models into the reverse-engineering workflow as an AI-powered copilot. Provides AI-assisted decompilation, an interactive chatbot with tool-calling support, function annotation, vulnerability analysis, and RAG-based context retrieval from binary databases. The Python plugin supports multiple LLM providers and ships with prompt templates, syntax highlighting, and a custom viewer UI—aimed at malware analysts and reverse engineers seeking LLM-augmented binary analysis inside IDA. (source: wiki/sources/descriptions/CSIT-SG__AETHER.md)

Broader copilot scope than rename/explain-only assistants such as [[binarylens]], [[ida-llm-explainer]], and [[gepetto]]—AETHER adds chatbot tool-calling, vulnerability analysis, and RAG over the IDB. Complements agent bridges like [[ida-pro-mcp]] and [[ida-mcp-server-plugin]] (external MCP automation) rather than replacing them; peers with multi-provider dockable panels like [[idassist]] and [[ida-assistant]].

## Links

- Repo: https://github.com/CSIT-SG/AETHER

## Related

[[overviews/reverse-engineering]] · [[ida-pro-mcp]] · [[ida-llm-explainer]] · [[gepetto]] · [[ida-gepetto]] · [[ida-assistant]] · [[idassist]] · [[aida]] · [[idaplugins]]
