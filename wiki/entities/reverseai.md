---
title: reverseai
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/dagoSte__reverseai.md
  - wiki/sources/README-categories.md
updated: 2026-11-11
confidence: medium
---

# reverseai

**ReverseAI** ([dagoSte/reverseai](https://github.com/dagoSte/reverseai)) is an open-source **static** reverse-engineering engine (primarily Python) that inspects **untrusted binaries, packages, and archives without executing them**. Heavy analyzers—Ghidra, JADX, LIEF, YARA-X, and a JavaScript parser—run inside **locked offline Docker containers**, while built-in host parsers cover **ELF, PE, Mach-O, APK**, and related formats. Every reported fact is tied to **exact file bytes**, **re-derived on the host**, and labeled **supported**, **derived**, or **unsupported** before it appears in structured reports. A **CLI** and **MCP server** expose verified Q&A for analysts and coding agents; an optional **hive** module can orchestrate AI-assisted reconstruction of native code into compilable **C or C++**. Targets defensive work such as malware triage, **anti-cheat and game-client analysis**, and other RE where tool output must not be taken on faith. (source: wiki/sources/descriptions/dagoSte__reverseai.md)

Listed under README **Cheat → RE Tools** beside verification-gated hosts such as [[reverify]] and offline orchestrators such as [[harness-for-rea]].

## Architecture

| Layer | Role |
|-------|------|
| **Host parsers** | ELF, PE, Mach-O, APK, and related formats on the analyst machine |
| **Locked containers** | Ghidra, JADX, LIEF, YARA-X, JS parser—offline, non-executing analysis |
| **Verification** | Host re-derivation from bytes; supported / derived / unsupported classification |
| **Interfaces** | CLI for humans; MCP server for agents |
| **Hive (optional)** | AI-assisted lift of native programs toward compilable C/C++ |

## Positioning

**Verification-first static stack** for hostile inputs: contrasts with live-memory lanes (Cheat Engine) and complements [[harness-for-rea]] (planner + Docker REA specialist UI) by centering **byte-anchored reports** and MCP over untrusted PE/APK/JS. Pair [[binary-evidence]] and [[research-rigor]] when acting on agent or container output. (source: wiki/sources/descriptions/dagoSte__reverseai.md)

## Links

- Repo: https://github.com/dagoSte/reverseai

## Related

[[research-rigor]] · [[binary-evidence]] · [[reverify]] · [[harness-for-rea]] · [[awesome-ai-reverse-engineering]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
