---
title: DSH REA Plugin
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/jiuyou-7411__dsh-rea-plugin.md
  - wiki/sources/README-categories.md
updated: 2026-10-24
confidence: medium
---

# DSH REA Plugin

**dsh-rea-plugin** (jiuyou-7411/dsh-rea-plugin) is a **DeepSeek Harness (DSH) plugin** that exposes the REA reverse-engineering agent stack as a Chinese-language workbench with a web UI for browsing and running tools. JavaScript and Node.js bridge more than 220 MCP tools from upstream rea-agents, bundle offline documentation and agent skills, and provide a dashboard for health, tool usage, and localized error explanations. Optional engine install helpers cover Ghidra, JDK, and Frida from the panel. (source: wiki/sources/descriptions/jiuyou-7411__dsh-rea-plugin.md)

README category: Cheat / RE Tools.

## Stack

JavaScript/Node.js DSH plugin; bridges **220+ MCP tools** from upstream **rea-agents** into a localized web workbench. Bundled offline documentation and agent skills reduce extra REA profile setup. Dashboard surfaces health checks, per-tool usage, and localized error explanations; panel helpers can install or manage Ghidra, JDK, and Frida engines. (source: wiki/sources/descriptions/jiuyou-7411__dsh-rea-plugin.md)

## Capabilities

Android APK workflows via JADX, apktool, unpacking, and Frida instrumentation; native binaries through optional Ghidra integration; mobile-focused helpers for anti-injection checks, SO analysis, and related scripts. Analysis can run without extra REA profile setup when bundled docs and skills are used. (source: wiki/sources/descriptions/jiuyou-7411__dsh-rea-plugin.md)

## Target use cases

Security researchers and reverse engineers who want guided, agent-assisted binary and mobile app analysis inside DSH rather than raw command-line REA alone — game APK modding, anti-cheat module triage, and catalog-driven tool discovery with a localized UI. (source: wiki/sources/descriptions/jiuyou-7411__dsh-rea-plugin.md)

## Positioning

Complements [[dsh-plugins]] and [[dsh-ghidra]] as a REA-oriented DSH workbench (broader upstream MCP catalog vs PyGhidra-only Ghidra bridge). Pair with [[rea-atlas]] / [[rea-prompts]] for REA tagging discipline and [[research-rigor]] before enforcement conclusions.

## Links

- Repo: https://github.com/jiuyou-7411/dsh-rea-plugin

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/mobile-security]] · [[dsh-plugins]] · [[dsh-ghidra]] · [[ghidra-skill-for-dsh]] · [[rea]] · [[rea-atlas]] · [[rea-prompts]] · [[jadx]] · [[frida]] · [[research-rigor]]
