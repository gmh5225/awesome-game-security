---
title: interactive-feedback-mcp
kind: entity
topics: [overview, game-engine]
sources:
  - wiki/sources/descriptions/noopstudios__interactive-feedback-mcp.md
updated: 2026-07-27
confidence: medium
---

# interactive-feedback-mcp

MCP (Model Context Protocol) server that lets AI coding assistants request interactive user feedback—input, confirmations, and selections via structured UI prompts—during automated workflows (human-in-the-loop). Fits the Game Develop → MCP server lane (`[Interactive User Feedback MCP]`); useful for tooling builders wiring agents that need operator confirmation mid-run rather than editor automation or live RE tools. (source: wiki/sources/descriptions/noopstudios__interactive-feedback-mcp.md)

Complements agent-facing MCP bridges such as [[unity-mcp]] (Unity editor), [[deepwiki-mcp]] (docs/wiki retrieval), and [[memmcp]] (CE-like memory tooling) by targeting HITL prompts instead of engine, documentation, or process-memory surfaces. macOS-native variant [[interactive-feedback-macos-mcp]] (AppleScript dialogs + image support; gmh5225 fork) extends the same HITL lane on Apple hosts.

## Links

- Repo: https://github.com/noopstudios/interactive-feedback-mcp

## Related

[[interactive-feedback-macos-mcp]] · [[overviews/overview]] · [[overviews/game-engine]] · [[unity-mcp]] · [[deepwiki-mcp]] · [[memmcp]]
