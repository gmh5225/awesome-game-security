---
title: reai-ida
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/RevEngAI__reai-ida.md
updated: 2026-08-21
confidence: medium
---

# reai-ida

IDA Pro plugin that connects the disassembler to the **RevEng.AI** AI-assisted reverse engineering platform. Written in Python with Qt-based dialogs and service layers for API integration, it supports binary upload, similarity-based function matching, automated renaming, auto-unstrip workflows, and AI decompilation views. Targets reverse engineers who want to accelerate analysis of stripped binaries with machine-learning-assisted tooling. (source: wiki/sources/descriptions/RevEngAI__reai-ida.md)

Complements local signature-based renaming ([[renamaida]]), cloud function recognition ([[finger]]), and in-IDA LLM assistants ([[wpechatgpt]], [[ida-gepetto]], [[binoculars]])—verify platform-suggested names and decompilation against disassembly per [[research-rigor]].

## Links

- Repo: https://github.com/RevEngAI/reai-ida

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[renamaida]] · [[finger]] · [[wpechatgpt]] · [[ida-gepetto]] · [[binoculars]] · [[mcrit-plugin]] · [[vt-ida-plugin]] · [[research-rigor]]
