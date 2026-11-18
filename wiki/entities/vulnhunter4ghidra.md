---
title: VulnHunter4Ghidra
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/overkazaf__VulnHunter4Ghidra.md
updated: 2026-11-18
confidence: medium
---

# VulnHunter4Ghidra

**VulnHunter4Ghidra** (overkazaf/VulnHunter4Ghidra) is a **Ghidra extension** and **headless CLI** for finding security flaws in **native executables** through **source-to-sink taint analysis**. A **Java** Ghidra plugin exports function metadata and communicates over **TCP** with a **Python** engine built on **angr** and **Z3** that constructs control-flow graphs, propagates taint across configurable call depth, and can symbolically verify whether untrusted input reaches dangerous APIs. Findings carry **CWE IDs** and severity labels for issues such as buffer overflows, format strings, command injection, and use-after-free. Supports **ELF**, **PE**, and **Mach-O**; interactive review inside Ghidra or batch workflows with **JSON** output and CI-friendly exit codes. Useful when auditing **game clients**, loaders, and **anti-cheat** or **DRM** native components. (source: wiki/sources/descriptions/overkazaf__VulnHunter4Ghidra.md)

## Architecture

- **Frontend:** Java Ghidra plugin — function metadata export, interactive finding review
- **Backend:** Python angr + Z3 — CFG construction, taint propagation, symbolic reachability checks
- **Transport:** TCP between Ghidra UI and analysis engine
- **Modes:** in-Ghidra UI or standalone headless CLI (JSON + exit codes)

## Positioning

Listed under **Cheat → RE Tools**. Complements overkazaf/[[ponce4ghidra]] (constraint solving / Find–Avoid symbolic execution) and [[d810g]] (deobfuscation) in the same Ghidra+angr toolchain; differs by emphasizing **automated vulnerability triage** (taint paths, CWE tagging) rather than manual constraint exploration. Pairs with [[angry-ghidra]] and core taint libraries such as [[triton]].

## Links

- Repo: https://github.com/overkazaf/VulnHunter4Ghidra

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ponce4ghidra]] · [[d810g]] · [[angry-ghidra]] · [[triton]] · [[ponce]]