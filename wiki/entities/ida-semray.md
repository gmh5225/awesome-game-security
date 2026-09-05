---
title: ida-semray
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/19h__ida-semray.md
updated: 2026-09-05
confidence: medium
---

# ida-semray

**IDA Pro plugin** for AI-assisted semantic binary analysis. Written in Python, it uses a **Gemini-powered** workflow to suggest function names, variable names, and detailed comments from decompiled code or assembly context. An interactive interface performs context-aware analysis across callers, callees, and references to accelerate reverse-engineering triage and code comprehension for security analysts. (source: wiki/sources/descriptions/19h__ida-semray.md)

Sits in the in-IDA LLM-assistant lane beside rename/explain tools such as [[gepetto]], [[ida-copilot]], and [[binarylens]], and broader copilots like [[aether]] and [[idassist]] that add chatbot or RAG workflows.

## Links

- Repo: https://github.com/19h/ida-semray

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[gepetto]] · [[ida-copilot]] · [[binarylens]] · [[aether]] · [[idassist]] · [[idaplugins]]
