---
title: ghidra-gradle-plugin
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/astrelsky__GhidraGradlePlugin.md
updated: 2026-08-18
confidence: medium
---

# ghidra-gradle-plugin

**Archived** Gradle plugin for building Ghidra extensions. Configures classpaths from a local Ghidra installation, wires in extension build scripts, and provides helper tasks for IDE setup. Implementation is mainly Java and Groovy; focus is developer ergonomics around extension packaging rather than runtime analysis features. Most relevant for reverse-engineering tool authors who maintain custom Ghidra plugins. (source: wiki/sources/descriptions/astrelsky__GhidraGradlePlugin.md)

Build-tooling peer used by Gradle-based Ghidra extensions such as [[ghidra-orbis]] from the same maintainer; complements the full [[ghidra]] framework tree and runtime plugins ([[gfred]], [[dragonhook]], [[ghidra-mcp]]).

## Links

- Repo: https://github.com/astrelsky/GhidraGradlePlugin (README tag: Gradle)

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[ghidra-orbis]] · [[gfred]] · [[gui-plugin-template]]
