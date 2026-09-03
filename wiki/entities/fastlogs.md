---
title: fastlogs
kind: entity
topics: [game-engine, mobile-security]
sources:
  - wiki/sources/descriptions/AitiX__Fastlogs.md
updated: 2026-09-03
confidence: medium
---

# fastlogs

Open-source debug and bug-reporting engine for game builds where the engine console is hard or impossible to reach — WebGL, portals, mobile, and consoles. From a running build, a single gesture or agent call ships recent log lines, device info, context breadcrumbs, screenshots, and scene snapshots to a self-hosted Node.js server that stores reports in SQLite and returns a short shareable viewer link. (source: wiki/sources/descriptions/AitiX__Fastlogs.md)

Clients exist for **Unity** (C# UPM package) and **GameMaker** (GML) under one shared JSON ingest contract. Features include crash auto-capture, offline outbox, a browsable catalog with full-text search and triage, optional sinks to Slack/Discord/webhooks/issue trackers, and PII scrubbing by default. A headless send path and remote command channel let QA, developers, or AI agents inspect and drive a live build without a debugger — shortening the loop from a distributed-build bug to a filterable browser console. (source: wiki/sources/descriptions/AitiX__Fastlogs.md)

## Links

- Repo: https://github.com/AitiX/Fastlogs

## Related

[[unity-mcp]] · [[interactive-feedback-mcp]] · [[games-test-automation-example]] · [[unity-automated-qa-examples]] · [[overviews/game-engine]] · [[overviews/mobile-security]]
