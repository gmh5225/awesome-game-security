---
title: Ghidra Skill for DSH
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Cristallin2006__ghidra-skill-for-dsh.md
  - wiki/sources/README-categories.md
updated: 2026-09-26
confidence: medium
---

# Ghidra Skill for DSH

**ghidra-skill-for-dsh** (Cristallin2006/ghidra-skill-for-dsh) is a **DeepSeek Harness (dsh) agent skill family** pairing a persistent Ghidra 12.x headless RPC daemon with seven scenario-specific automated binary-analysis workflows. Python wraps a vendored ghidra-rpc engine with helper scripts for decompilation, triage, unpacking, crypto checks, emulation, and evidence logging, plus optional dsh hooks that enforce analysis discipline. (source: wiki/sources/descriptions/Cristallin2006__ghidra-skill-for-dsh.md)

README category: Cheat / RE Tools.

## Architecture

A long-lived Ghidra headless RPC daemon exposes sub-second analysis commands to dsh agents. Python helper scripts wrap the vendored ghidra-rpc engine for decompilation, triage, unpacking, crypto checks, emulation, and evidence logging. Optional dsh hooks mechanically enforce analysis discipline instead of relying on GUI workflows or MCP bridges. (source: wiki/sources/descriptions/Cristallin2006__ghidra-skill-for-dsh.md)

## Scenario skills

Seven dsh skills cover initial binary triage, packer unpacking, deep static analysis, vulnerability auditing, dynamic instrumentation with Frida and Qiling, PCAP and network forensics, and pure-DEX Android APK reversing. Workflows emphasize scripted guardrails and oracle-based verification over ad-hoc GUI or MCP tooling. (source: wiki/sources/descriptions/Cristallin2006__ghidra-skill-for-dsh.md)

## Target use cases

CTF reverse engineering, crackme solving, malware triage, vulnerability pre-screening, and forensic traffic analysis — including game clients and anti-cheat modules where fast scripted Ghidra commands and auditable evidence matter. (source: wiki/sources/descriptions/Cristallin2006__ghidra-skill-for-dsh.md)

## Positioning

Complements [[dsh-plugins]] PyGhidra bridge and [[ghidra-headless-mcp]] MCP paths as a dsh-native, scenario-driven Ghidra automation stack. Pair oracle outputs with [[research-rigor]] when acting on agent summaries.

## Links

- Repo: https://github.com/Cristallin2006/ghidra-skill-for-dsh

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dsh-plugins]] · [[ghidra-headless-mcp]] · [[research-rigor]] · [[frida]]
