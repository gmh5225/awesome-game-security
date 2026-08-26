---
title: WProtect (DeDf)
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/DeDf__WProtect.md
updated: 2026-08-26
confidence: medium
---

# WProtect (DeDf)

**Windows executable protection** project that **virtualizes selected native code blocks** into a custom virtual-machine format. The pipeline **disassembles target instructions**, **builds VM bytecode**, **redirects original code with jump stubs**, and **appends a new PE section** storing transformed logic and runtime tables. Implemented mainly in **C++** with **AsmJit**, **udis86**, and custom **PE parsing/rewriting** utilities. Aimed at **software protection research**, **reverse engineering practice**, and analysis of **VM-based anti-tamper** techniques—not a commercial AC product. (source: wiki/sources/descriptions/DeDf__WProtect.md)

Distinct from the separate [[wprotect]] obfuscation-engine reference (`xiaoweime/WProtect`). Useful alongside open x86 VM virtualizers such as [[phantasm-x86-virtualizer]], [[x64-virtualizer-rs]], and [[nocturne]] when studying PE rewrite + custom VM bytecode pipelines.

## Links

- Repo: https://github.com/DeDf/WProtect

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[wprotect]] · [[phantasm-x86-virtualizer]] · [[x64-virtualizer-rs]] · [[nb-obfuscator]] · [[alcatraz]]
