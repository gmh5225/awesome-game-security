---
title: Awesome AI Reverse Engineering
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/zhuyansen__awesome-ai-reverse-engineering.md
  - wiki/sources/README-categories.md
updated: 2026-10-14
confidence: high
---

# Awesome AI Reverse Engineering

Curated catalog of open-source tools that connect **AI coding agents** (Claude Code, Codex, and similar) to reverse engineering workflows. Targets **security researchers**, **malware analysts**, and engineers who want LLM-driven automation for binary, mobile, and protocol RE—not a general cheat link dump. (source: wiki/sources/descriptions/zhuyansen__awesome-ai-reverse-engineering.md)

## Catalog scope

Roughly **122 vetted repositories**, grouped by workflow:

- **Disassembler / decompiler MCP servers** — Ghidra, IDA Pro, Binary Ninja, radare2, x64dbg bridges for agent-driven decompile, navigation, and guarded IDB edits.
- **Mobile stacks** — jadx, apktool, Frida, and related agent/MCP wrappers for APK/DEX and dynamic instrumentation.
- **Web and JavaScript protocol analysis** — tooling for HTTP/JS-centric RE beside native binaries.
- **Agent skill packs** — composable instruction sets for coding agents in RE tasks.
- **Example rebuild projects** — reference ports such as [[rea-mytechnotalent]] illustrating end-to-end agent RE pipelines.

Peers individual MCP bridges listed in [[overviews/reverse-engineering]] (AI-assisted RE lane) and mobile agent tooling in [[overviews/mobile-security]]. (source: wiki/sources/descriptions/zhuyansen__awesome-ai-reverse-engineering.md)

## Metadata and grading

Each list entry includes **star counts** and **security grades** from automated README review, with **machine-readable JSON metadata** alongside the markdown lists—useful for triaging which agent-facing RE repos to trust before wiring them into local MCP or skill workflows. Pair with [[research-rigor]] when acting on agent output or third-party automation. (source: wiki/sources/descriptions/zhuyansen__awesome-ai-reverse-engineering.md)

## Role in the README map

Listed under **Cheat → RE Tools** as a curated AI-agent RE stack index (Ghidra/IDA MCP servers, mobile tooling, agent skills, security-graded projects).

## Links

- Repo: https://github.com/zhuyansen/awesome-ai-reverse-engineering

## Related

[[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/mobile-security]] · [[open-reverselab]] · [[skid-factory]] · [[reverify]] · [[kiln-ida]] · [[binary-ninja-headless-mcp]] · [[awesome-mcp-servers]]
