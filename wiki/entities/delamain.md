---
title: Delamain
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/xjoker__delamain.md
updated: 2026-07-22
confidence: medium
---

# Delamain

Headless MCP (Model Context Protocol) server that exposes the full JADX Android APK/DEX decompiler to AI agents. Java backend (Javalin wrapping jadx’s headless API) plus a Python FastMCP gateway for auth, routing, and out-of-band file transfer in a single Docker image. Agents can decompile classes, search code/strings, trace xrefs and data flow, inspect manifests/resources, generate Frida hooks, run security scans, and rename/annotate code with bounded, paginated output. Low-memory mmap-backed index targets servers, CI, and constrained environments where an agent drives analysis instead of a GUI. (source: wiki/sources/descriptions/xjoker__delamain.md)

Complements the core [[jadx]] decompiler and apktool decode/rebuild MCP tools such as [[apktool-mcp-server]] — Delamain is the jadx-decompile / xref / Frida-hook lane for agent-driven Android RE.

## Links

- Repo: https://github.com/xjoker/delamain

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[jadx]] · [[apktool-mcp-server]] · [[frida]] · [[il2cpp]]
