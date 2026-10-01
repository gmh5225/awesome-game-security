---
title: AITools
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cheat-engine__AITools.md
  - wiki/sources/README-categories.md
updated: 2026-10-01
confidence: medium
---

# AITools

**AITools** (cheat-engine/aitools) is the official Cheat Engine extension that integrates large language model assistance into live memory analysis and reverse-engineering workflows. Implemented mainly in Lua with a Lazarus form-based UI, it connects to Google Gemini (public, Patreon, or personal API keys) or local model backends and exposes native CE capabilities to the model through `registerAITool` callbacks. (source: wiki/sources/descriptions/cheat-engine__AITools.md)

## Capabilities

- **In-app AI dialog** driving memory scan, disassembly, watchpoints, pointer chains, and Auto Assembler script creation/validation
- **Skills framework** with on-demand expert prompts for structure dissection, pointer scanning, Mono/IL2CPP runtime scripting, and Unreal Engine object traversal
- **Bundled RE skills** covering memory/pointer scan, Unreal, and auto-assembler workflows (source: wiki/sources/README-categories.md)

Unlike external MCP bridges such as [[cheatengine-mcp-bridge]] that pipe agent commands into CE from outside the process, AITools runs as an in-CE extension with direct access to the Lua engine and scanner. Pairs with verification-oriented agent tooling such as [[reverify]] and orchestrators such as [[skid-factory]] when LLM output must be grounded in tool evidence rather than model speculation alone. Complements official CE Lua extensions such as [[unreal-engine-tools]] and Mono helpers such as [[cheatengine-mono-helper]] for the IL2CPP/Mono skills bundled in its framework.

## Role in the README map

Listed under **Cheat → RE Tools** beside official CE Lua extensions such as [[unreal-engine-tools]] and agent-native RE hosts. Targets modders and game-security researchers who want conversational AI help building stable cheats and analyzing running processes from within Cheat Engine.

## Links

- Repo: https://github.com/cheat-engine/aitools

## Related

[[cheat-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[cheatengine-mcp-bridge]] · [[reverify]] · [[skid-factory]] · [[ceasta]] · [[unreal-engine-tools]] · [[cheatengine-mono-helper]] · [[research-rigor]]
