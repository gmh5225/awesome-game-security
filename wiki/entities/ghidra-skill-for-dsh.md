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

## Scenario skills

Seven skills cover initial binary triage, packer unpacking, deep static analysis, vulnerability auditing, dynamic instrumentation (Frida and Qiling), PCAP/network forensics, and pure-DEX Android APK reversing. Emphasizes fast sub-second Ghidra commands, scripted guardrails, and oracle-based verification instead of GUI or MCP tooling.

## Positioning

Complements [[dsh-plugins]] PyGhidra bridge and [[ghidra-headless-mcp]] MCP paths for CTF reverse engineering, crackme solving, malware triage, vulnerability pre-screening, and forensic traffic analysis on game clients and AC modules.

## Links

- Repo: https://github.com/Cristallin2006/ghidra-skill-for-dsh

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dsh-plugins]] · [[ghidra-headless-mcp]] · [[research-rigor]] · [[frida]]
