---
title: PyMemoryEditor
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/JeanExtreme002__PyMemoryEditor.md
  - wiki/sources/README-categories.md
updated: 2026-10-02
confidence: medium
---

# PyMemoryEditor

**PyMemoryEditor** (JeanExtreme002/PyMemoryEditor) is a pure-Python library for reading, writing, and searching the memory of running processes through OS-level APIs on Windows, Linux, and macOS. Built on **ctypes** with optional **NumPy**-accelerated scanning, it supports Cheat Engine-style value searches, AOB pattern scans, multi-level pointer chains, and reverse pointer scanning. The project includes a **PySide6 (Qt) GUI** that mirrors Cheat Engine's attach-and-scan workflow and an optional **Model Context Protocol server** that lets AI assistants run the full scan-and-refine loop. (source: wiki/sources/descriptions/JeanExtreme002__PyMemoryEditor.md)

## Capabilities

- Cross-platform process attach and memory read/write via ctypes OS APIs (Windows, Linux, macOS)
- Value scans, AOB pattern scans, pointer chains, and reverse pointer scanning
- Optional NumPy-accelerated scan paths
- PySide6 Qt GUI with CE-style attach-and-scan workflow
- Optional MCP server for AI-assisted scan/refine automation

## Use cases

Aimed at **game modding**, **reverse engineering**, and **game security research** where cross-platform process memory analysis is needed—especially when analysts prefer Python libraries and agent MCP integration over native Windows-only CE forks. (source: wiki/sources/descriptions/JeanExtreme002__PyMemoryEditor.md)

## Positioning

Listed under **Cheat → Debugging** beside native memory scanners such as [[cheat-engine]], [[simple-memory-editor]], [[pointer-lab]], and [[mhsx]]. Unlike Windows-only C/C++ alternatives, PyMemoryEditor bundles scanner primitives, GUI, and optional MCP in one pure-Python package. Complements external CE MCP bridges such as [[cheatengine-mcp-bridge]], standalone memory MCP servers such as [[memmcp]], and agent-ready trainers such as [[apprentice]] and official CE AI tooling such as [[aitools]].

## Links

- Repo: https://github.com/JeanExtreme002/PyMemoryEditor

## Related

[[cheat-engine]] · [[simple-memory-editor]] · [[pointer-lab]] · [[mhsx]] · [[cheatengine-mcp-bridge]] · [[memmcp]] · [[apprentice]] · [[aitools]] · [[n0xis]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
