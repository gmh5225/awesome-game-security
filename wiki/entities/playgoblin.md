---
title: PlayGoblin
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/grloper__playgoblin.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# PlayGoblin

Open-source automated QA bot ([grloper/playgoblin](https://github.com/grloper/playgoblin)) that plays local builds like a persistent tester, records what goes wrong, and turns captured runs into evidence-backed bug reports. Listed under README **Game Develop / AI Agents** and **Game Testing**. (source: wiki/sources/descriptions/grloper__playgoblin.md) (source: wiki/sources/README-categories.md)

## Architecture

- **In-engine drivers:** Unity package and an experimental Unreal Engine C++ plugin drive the player through levels, crawl menus, and emit structured run logs.
- **Offline analyzer:** Python CLI ingests those logs and applies deterministic pass/fail checks (core gates are rule-based, not LLM judgment).
- **Agent bridge:** MCP server plus JSON CLI output expose findings to AI coding agents. (source: wiki/sources/descriptions/grloper__playgoblin.md)

## Deterministic checks

Crashes, dead UI buttons, stuck navigation, falls, blank frames, debug leftovers in shipping paths, and optional FPS regressions. Each finding ties to events, frames, or log lines for reproducible triage. (source: wiki/sources/descriptions/grloper__playgoblin.md)

## Outputs

HTML or Markdown reports, optional GitHub issue filing, and machine-readable CLI/MCP payloads for agent-driven fix loops. (source: wiki/sources/descriptions/grloper__playgoblin.md)

## Positioning

Targets game developers and QA workflows who want repeatable **overnight playtesting** and regression discovery on **local builds**—not anti-cheat or live security monitoring. Contrasts with injection-based Windows agent stacks such as [[llm-game-automation-mcp]]. Complements [[unity-automated-qa-examples]], [[fastlogs]], and [[pz-devharness]] in the Game Testing lane. (source: wiki/sources/descriptions/grloper__playgoblin.md)

## Links

- Repo: https://github.com/grloper/playgoblin

## Related

[[llm-game-automation-mcp]] · [[opengame]] · [[pz-devharness]] · [[unity-automated-qa-examples]] · [[fastlogs]] · [[quen-mcp]] · [[overviews/game-engine]]
