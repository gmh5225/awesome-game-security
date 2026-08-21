---
title: hiearchy-eac
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Sinclairq__hiearchy-eac.md
updated: 2026-08-21
confidence: medium
---

# hiearchy-eac

Windows **kernel proof-of-concept** for bypassing **EasyAntiCheat.sys self-integrity checks** by manipulating **call hierarchy** and **memory reads**. Implemented in **C++** with supporting **assembly**; hooks selected verification routines to redirect inspection toward a **cleaned image copy**. Monitors **module load events**, tracks **EAC driver memory boundaries**, and **spoofs stack and register references** during integrity-related accesses. Primary use case is anti-cheat reverse engineering and defensive understanding of integrity verification paths. Listed under `[Integrity Checks]`. (source: wiki/sources/descriptions/Sinclairq__hiearchy-eac.md)

Complements callback-driven section-compare analysis such as [[bypassing-easyanticheat-integrity-check]] and historical integrity PoCs such as [[cveac-2020]] by focusing on call-hierarchy semantics, memory-read redirection, and stack/register spoofing during EAC self-checks rather than only static image comparison.

## Links

- Repo: https://github.com/Sinclairq/hiearchy-eac

## Related

[[easy-anti-cheat]] · [[bypassing-easyanticheat-integrity-check]] · [[cveac-2020]] · [[kernel-callbacks]] · [[stack-spoofing]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
