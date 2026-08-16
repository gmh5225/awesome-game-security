---
title: droidrun
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/droidrun__droidrun.md
updated: 2026-08-16
confidence: medium
---

# droidrun

**droidrun** is a Python framework for controlling Android and iOS devices through LLM-powered agents that automate device interactions from natural-language commands. It drives taps, navigation, and app workflows via **ADB** on Android and platform-native **accessibility APIs** on iOS, with a scripter-agent architecture, custom tool registration, and structured output for reliable automation. Supported LLM backends include OpenAI, Anthropic, Gemini, Ollama, and DeepSeek. Primary users are mobile security testers and QA engineers automating Android/iOS app testing and interaction workflows with AI-driven device control. (source: wiki/sources/descriptions/droidrun__droidrun.md)

Complements all-in-one Android control platforms such as [[lamda]] and static-analysis MCP servers such as [[delamain]] and [[apktool-mcp-server]] — droidrun targets natural-language **device actuation** rather than decode/decompile or bundled MITM/Frida stacks.

## Links

- Repo: https://github.com/droidrun/droidrun

## Related

[[lamda]] · [[delamain]] · [[apktool-mcp-server]] · [[android-proxy-mcp]] · [[mobile-re-skill]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
