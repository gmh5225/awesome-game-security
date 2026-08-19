---
title: STS2-KitLib
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/WRXinYue__STS2-KitLib.md
updated: 2026-08-19
confidence: medium
---

# STS2-KitLib

Modular in-game developer toolkit mod for **Slay the Spire 2** aimed at mod authors, testers, reverse engineers, and anyone automating or stress-testing game behavior. Written primarily in **C#** with **Harmony** IL patching; a core host loads optional satellite modules for user tools, AI, cheats, and development features. Notable capabilities include a browser-based developer console for live logs and combat telemetry, an **MCP bridge** for automated game-state queries and scripted actions, Harmony patch analysis, and diagnostic ZIP export for mod feedback. Supporting **Python** build automation and a **TypeScript/Vue** dev viewer round out the workflow. (source: wiki/sources/descriptions/WRXinYue__STS2-KitLib.md)

## Architecture

| Component | Role |
|-----------|------|
| Core host | Loads and orchestrates optional satellite modules |
| Satellite modules | User tools, AI, cheat presets, and dev features |
| Browser dev console | Live logs and combat telemetry |
| MCP bridge | Automated game-state queries and scripted in-game actions |
| Harmony patch analysis | IL patch introspection for mod authors |
| Diagnostic ZIP export | Bundled feedback artifacts for mod debugging |

## Links

- Repo: https://github.com/WRXinYue/STS2-KitLib

## Related

[[cheatengine-mcp-bridge]] · [[duckov-marketmod]] · [[wellsanticheat]] · [[positron]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
