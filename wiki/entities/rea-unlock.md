---
title: Rea-Unlock
kind: entity
topics: [reverse-engineering, game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/zheedevVn__Rea-Unlock.md
updated: 2026-10-17
confidence: medium
---

# Rea-Unlock

**Rea-Unlock** (zheedevVn/Rea-Unlock) is an agent-oriented reverse-engineering platform that exposes a **Model Context Protocol server and CLI** so AI coding assistants can drive structured analysis workflows on real binaries and applications. Implementation is mainly TypeScript and Node.js, with Python, Java, Swift, and C++ bridges into disassemblers and debuggers. (source: wiki/sources/descriptions/zheedevVn__Rea-Unlock.md)

## Integrations

Static and dynamic tooling includes Ghidra, Hopper, Cutter, IDA-family analyzers, JEB, JADX, Apktool, Frida, LLDB, pwndbg, pwntools, and mitmproxy for traffic capture. (source: wiki/sources/descriptions/zheedevVn__Rea-Unlock.md)

## Coverage

Artifact types span native PE, ELF, and Mach-O (including specialty ISAs), Android and Harmony mobile packages, Apple bundles, Electron and JavaScript recovery, WASM and EVM bytecode, firmware, Flutter AOT, managed .NET NativeAOT, plus packet, pcap, and browser network observation. (source: wiki/sources/descriptions/zheedevVn__Rea-Unlock.md)

## Audience

Targets security researchers, malware analysts, and **game security engineers** who need LLM-assisted deep inspection of clients, protocols, and anti-tamper logic rather than ad hoc scripting alone. (source: wiki/sources/descriptions/zheedevVn__Rea-Unlock.md)

## Positioning

Same broad lane as morluto [[rea]] (cross-format MCP/CLI agent RE with external tool bridges) but as an independent repo with wider mobile, bytecode, and network-capture surface in the README summary. Distinct from [[rea-mytechnotalent]] (Python offline-first triage + local RAG). Pair agent output with [[research-rigor]] before enforcement conclusions.

## Links

- Repo: https://github.com/zheedevVn/Rea-Unlock

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/mobile-security]] · [[rea]] · [[rea-mytechnotalent]] · [[frida]] · [[ghidra]] · [[ghidra-mcp]] · [[jadx]] · [[apktool]]
