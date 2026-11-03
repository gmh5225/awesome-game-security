---
title: LLM Game Automation MCP
kind: entity
topics: [game-engine, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/CorruptedAng3l__llm-game-automation-mcp.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# LLM Game Automation MCP

Windows stack ([CorruptedAng3l/llm-game-automation-mcp](https://github.com/CorruptedAng3l/llm-game-automation-mcp)) that lets LLM agents or scripts drive **single-player** games in the background. Listed under README **Game Develop / MCP server**. (source: wiki/sources/descriptions/CorruptedAng3l__llm-game-automation-mcp.md) (source: wiki/sources/README-categories.md)

## Architecture

- **vinput (C++ / MSVC):** Injects a DLL per game process; **MinHook** and related API hooking deliver virtual keyboard, mouse, and gamepad input on the same channels the title reads.
- **Background operation:** Fakes focus so games keep rendering without holding foreground.
- **Graphics capture:** Reads swapchain frames across **Direct3D**, **OpenGL**, and **Vulkan** (DXGI/Vulkan/GL paths). (source: wiki/sources/descriptions/CorruptedAng3l__llm-game-automation-mcp.md)

## MCP server

TypeScript **Node.js** MCP wraps the vinput CLI with tools for process launch, frame capture, **OCR-based** text interaction, scripting, and input tracing. (source: wiki/sources/descriptions/CorruptedAng3l__llm-game-automation-mcp.md)

## Anti-cheat guards

Built-in checks **refuse injection** when known online anti-cheat components or processes are present—defensive refusal logic for offline automation rather than live multiplayer abuse. (source: wiki/sources/descriptions/CorruptedAng3l__llm-game-automation-mcp.md)

## Research value

Useful for studying **per-process input injection**, multi-API **graphics capture**, and voluntary AC process refusal in automation, testing, and security research. Contrasts with in-engine QA bots such as [[playgoblin]] and memory-focused MCP stacks such as [[cheat-mcp]]. (source: wiki/sources/descriptions/CorruptedAng3l__llm-game-automation-mcp.md)

## Links

- Repo: https://github.com/CorruptedAng3l/llm-game-automation-mcp

## Related

[[playgoblin]] · [[cheat-mcp]] · [[mcp-reverse]] · [[present-hook]] · [[hardware-input-injection]] · [[capture-engine]] · [[overviews/game-engine]] · [[overviews/graphics-api]]
