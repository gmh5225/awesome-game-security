---
title: REA (Reverse Engineer Anything)
kind: entity
topics: [reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/morluto__rea.md
  - wiki/sources/README-categories.md
updated: 2026-10-09
confidence: medium
---

# REA (Reverse Engineer Anything)

**REA** (morluto/rea) is a local **CLI and Model Context Protocol server** that connects AI coding agents to a unified reverse-engineering toolkit for software without source code. Implemented primarily in TypeScript on Node.js, it bridges external analyzers and returns findings with explicit **evidence provenance and stated limitations** so agents or terminal users can trace features, explain behavior, and guide reimplementation without treating model output as ground truth. (source: wiki/sources/descriptions/morluto__rea.md)

README category: Game Develop / MCP server.

## Capabilities

Cross-format coverage includes native binaries, JavaScript and Electron apps, .NET assemblies, websites and network captures, Android APKs, firmware images, **process runtime behavior**, and offline diagnostics such as ELF layout review and recorded crash evidence. Bridges include Hopper, Ghidra, IDA Pro, JADX, pwntools, mitmproxy, and other external analyzers; deep native disassembly/decompilation still requires those tools installed separately on the host. (source: wiki/sources/descriptions/morluto__rea.md)

## Architecture

TypeScript/Node.js orchestration runs analysis **locally** on the analyst machine, aggregating tool outputs into agent-consumable results rather than replacing each disassembler with a cloud service. MCP and CLI entry points share the same toolkit surface for IDE agents and terminal workflows. (source: wiki/sources/descriptions/morluto__rea.md)

## Target use cases

Reverse engineers, security researchers, and developers who need deep visibility into binaries, managed code, and web or mobile applications—for third-party behavior analysis, research, and structured reimplementation planning with auditable evidence trails. (source: wiki/sources/descriptions/morluto__rea.md)

## Positioning

Sits in the README **Game Develop → MCP server** lane beside single-backend bridges such as [[binary-ninja-headless-mcp]] and [[ghidra-headless-mcp]], but targets **cross-format agent-assisted RE** with explicit limitation reporting. Pair agent summaries with [[research-rigor]] before enforcement or attribution conclusions; complement deterministic verifiers such as [[reverify]] when claims must be machine-checked.

## Links

- Repo: https://github.com/morluto/rea

## Related

[[binary-ninja-headless-mcp]] · [[ghidra-headless-mcp]] · [[ida-pro-mcp]] · [[delamain]] · [[dnspymcp]] · [[reverify]] · [[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
