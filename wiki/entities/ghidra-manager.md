---
title: ghidra-manager
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/alexbevi__ghidra-manager.md
updated: 2026-08-18
confidence: medium
---

# ghidra-manager

Cross-platform Python CLI that installs Ghidra and assembles a curated extension set pinned to that exact release. Tracks stable GitHub releases, verifies download assets against published SHA-256 digests, and keeps the active installation plus one complete rollback pair. Manages plugins from immutable release commits, discovers and launches Ghidra projects, and exposes MCP bridge, multi-instance launch, doctor checks, and binary compare workflows. Targets reverse engineers and security analysts who need a repeatable, version-safe Ghidra toolchain on Windows, Linux, and macOS. (source: wiki/sources/descriptions/alexbevi__ghidra-manager.md)

Operational complement to the upstream [[ghidra]] framework and agent-facing MCP paths such as [[ghidra-mcp]] / [[ghidra-headless-mcp]]—this tool standardizes install, extension curation (including GhidraMCP), project launch, and diff workflows rather than adding in-Ghidra analysis features.

## Links

- Repo: https://github.com/alexbevi/ghidra-manager

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidra-mcp]] · [[ghidra-headless-mcp]] · [[ghidriff]] · [[ghidra-bridge]] · [[gfred]]
