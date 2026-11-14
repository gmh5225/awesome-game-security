---
title: Teach Me Assembly
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/awaxiaoyu__teach-me-assembly.md
updated: 2026-11-14
confidence: medium
---

# Teach Me Assembly

**Teach Me Assembly** (awaxiaoyu) is a fully **offline** **IDAPython** plugin for **IDA Pro** that adds **Chinese semantic comments** to each disassembled instruction in the current function. It consumes IDA’s decode results and local rule logic only—no AI, cloud services, or cross-instruction data-flow inference. Built-in coverage spans x86 conditionals, stack/call idioms, and common ARM, MIPS, and RISC-V load/store/arithmetic/branch mnemonics, with operand-aware explanations of registers, immediates, and memory references. Analysts can extend or override behavior via a companion **JSON mnemonic map** reloaded on each run. Aimed at reverse engineers and game security analysts who want faster per-line assembly readability while dissecting binaries in IDA. (source: wiki/sources/descriptions/awaxiaoyu__teach-me-assembly.md)

Rule-driven listing annotations—not Hex-Rays decompilation, automated renaming, or LLM copilots. Complements bilingual/stripped-binary helpers such as [[ida-zh-cn]] (UI localization) and [[ida-better-information]] (libc/FLIRT + math notes), and contrasts with AI explainers such as [[aida]] and [[ida-llm-explainer]].

## Links

- Repo: https://github.com/awaxiaoyu/teach-me-assembly

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[cbs]] · [[auto-enum]] · [[idacomments]] · [[idaplugins]]