---
title: figma-context-mcp
kind: entity
topics: [game-engine, overview]
sources:
  - wiki/sources/descriptions/GLips__Figma-Context-MCP.md
updated: 2026-08-25
confidence: medium
---

# figma-context-mcp

Framelink MCP for Figma (also listed as Cursor Talk To Figma MCP server) exposes structured Figma design data to AI coding agents via the Model Context Protocol. Built in TypeScript, it provides dedicated tools to fetch simplified design metadata and download referenced images, supporting stdio and HTTP transports while translating raw Figma API responses into model-friendly layout and style context. Primary use case is design-to-code automation—developers wire Cursor or other MCP clients so assistants implement UI accurately from Figma files. Fits Game Develop → MCP server / design-to-code lane. (source: wiki/sources/descriptions/GLips__Figma-Context-MCP.md)

Complements DCC and editor MCP bridges such as [[blender-mcp]] (3D scene authoring) and [[unity-mcp]] (in-engine scripting) by targeting UI design specs rather than runtime engine or 3D asset surfaces; differs from [[deepwiki-mcp]] (documentation retrieval) by sourcing live Figma layout/style context for frontend and game-UI implementation.

## Links

- Repo: https://github.com/GLips/Figma-Context-MCP

## Related

[[blender-mcp]] · [[unity-mcp]] · [[deepwiki-mcp]] · [[interactive-feedback-mcp]] · [[overviews/game-engine]] · [[overviews/overview]]
