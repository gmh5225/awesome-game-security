---
title: pyobfus
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/zhurong2020__pyobfus.md
updated: 2026-09-02
confidence: medium
---

# pyobfus

**Open-source, AST-based Python code obfuscator** that transforms source before shipping to deter reverse engineering and protect intellectual property. Applies cross-file identifier renaming, string and numeric literal encoding, import rewriting, and **control-flow flattening**, with YAML configuration and framework-aware presets for FastAPI, Django, Flask, and related stacks. Notable features include pre-flight risk scanning, **reverse stack-trace mapping** for debugging protected builds, a machine-readable JSON CLI, an **MCP server** for AI coding agents, and a VS Code extension; an optional Pro tier adds stronger protections such as AES string encryption. Targets CPython 3.9–3.14 for commercial Python applications, game-related tooling, and other shipped code against casual analysis and tampering. (source: wiki/sources/descriptions/zhurong2020__pyobfus.md)

Complements [[pyarmor]] on the Python protection side and [[de4py]] on the analyst side; AST-level CFF ties to [[control-flow-flattening]].

## Links

- Repo: https://github.com/zhurong2020/pyobfus

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[pyarmor]] · [[de4py]] · [[control-flow-flattening]] · [[javascript-obfuscator]]
