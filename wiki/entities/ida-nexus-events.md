---
title: ida-nexus-events
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrexodia__ida-nexus-events.md
updated: 2026-09-04
confidence: medium
---

# ida-nexus-events

**IDA Nexus Event Viewer** is a standalone terminal application that discovers locally published IDA Nexus databases and streams live IDB hook events from a selected instance. Built with Python 3.11+, the Textual TUI framework, and the ida-nexus client library, it presents a split-pane interface for browsing ready databases and watching structured `/idb_events` as they arrive. (source: wiki/sources/descriptions/mrexodia__ida-nexus-events.md)

Each event row includes timestamps, revisions, event names, execution provenance, and callback-specific fields, with color coding for renames, functions, segments, types, patches, comments, and Python script operations. It targets reverse engineers and game security analysts who use IDA Pro with the Nexus Code Mode plugin and need real-time visibility into database changes and what triggered them.

Observability companion to batch LLM harnesses such as [[ida-nexus-docker]] (same author; disposable Docker runs with ZIP audit trails) and live agent automation via [[ida-pro-mcp]] — this tool focuses on interactive, in-session monitoring of Nexus-driven IDB mutations rather than orchestrated prompt pipelines or MCP tool calls.

## Links

- Repo: https://github.com/mrexodia/ida-nexus-events

## Related

[[overviews/reverse-engineering]] · [[ida-nexus-docker]] · [[ida-pro-mcp]] · [[ida-no-mcp]] · [[retoolsync]] · [[research-rigor]]
