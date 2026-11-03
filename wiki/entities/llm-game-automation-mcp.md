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

**LLM Game Automation MCP** is a Windows stack for driving single-player games in the background via LLM agents or scripts. A C++ **vinput** DLL injects into each game process (MinHook and related hooking) to deliver virtual keyboard, mouse, and gamepad input on the same paths games read, fake focus so titles keep rendering without foreground, and capture swapchain frames across Direct3D, OpenGL, and Vulkan. A TypeScript Node.js MCP server wraps the vinput CLI with tools for launch, capture, OCR-based text interaction, scripting, and input tracing. Built-in guards refuse injection when known online anti-cheat components or processes are present—useful for studying per-process input injection, graphics capture, and defensive refusal logic in offline automation and security research, not live multiplayer abuse. (source: wiki/sources/descriptions/CorruptedAng3l__llm-game-automation-mcp.md)

## Links

- Repo: https://github.com/CorruptedAng3l/llm-game-automation-mcp

## Related

[[cheat-mcp]] · [[mcp-reverse]] · [[present-hook]] · [[hardware-input-injection]] · [[overviews/game-engine]] · [[overviews/graphics-api]]
