---
title: ida-nexus-docker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrexodia__ida-nexus-docker.md
updated: 2026-08-21
confidence: medium
---

# ida-nexus-docker

**IDA Nexus Docker runner** is a disposable container harness for automated static binary analysis with IDA Pro 9.4+, the Pi coding agent, and Hex-Rays IDA Nexus. Each run copies samples into an isolated workspace, executes a sequence of LLM-driven prompts as separate Pi sessions, and packages IDA Nexus semantic traces, Pi transcripts, and worker logs into a portable ZIP audit archive. (source: wiki/sources/descriptions/mrexodia__ida-nexus-docker.md)

The stack combines Docker, Python orchestration, shell entrypoints, and Node-based Pi tooling. Model provider settings are supplied at runtime rather than baked into the image, keeping credentials and host paths out of the container while treating samples as hostile. Workflows target reproducible prompt-driven tasks such as unpacking, API and string recovery, configuration extraction, and IDB markup.

Containerized batch harness rather than an in-IDA MCP bridge: complements live agent automation via [[ida-pro-mcp]] (same author; full IDAPython MCP surface), real-time Nexus event monitoring via [[ida-nexus-events]] (Textual TUI for live `/idb_events` streams), and read-only OpenCode harnesses such as [[re-harness]] by emphasizing disposable isolation and exportable audit trails for malware and game-security RE.

## Links

- Repo: https://github.com/mrexodia/ida-nexus-docker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-pro-mcp]] · [[ida-nexus-events]] · [[re-harness]] · [[ida-cli]] · [[headless-ida-mcp-server]] · [[research-rigor]]
