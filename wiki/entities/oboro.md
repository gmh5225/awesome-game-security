---
title: Oboro
kind: entity
topics: [reverse-engineering, mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/luluovo1__Oboro.md
updated: 2026-10-18
confidence: medium
---

# Oboro

**Oboro** is a customized **LLVM-based compiler and binary tooling** monorepo (luluovo1) centered on **Clang** and **LLVM BOLT**. The tree follows a typical **llvm-project** layout: Clang frontend, diagnostics, plugins, and static analyzer components alongside BOLT post-link binary analysis, optimization, and rewrite infrastructure. Bilingual README/contributing docs and standalone usage manuals target integrators who build and deploy specialized native toolchains for **binary hardening** and reverse-engineering-related analysis of protected game and application code. (source: wiki/sources/descriptions/luluovo1__Oboro.md)

## Distribution focus

Ships **prebuilt Android NDK LLVM 21 / OLLVM** toolchain builds with **FLA**, **BCF**, **indirection**, and **string/constant encryption** passes aimed at hardening native **`.so`** modules in mobile game and app protection workflows. (source: wiki/sources/descriptions/luluovo1__Oboro.md)

## Links

- Repo: https://github.com/luluovo1/Oboro

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[control-flow-flattening]] · [[dll-ollvm]] · [[amice]] · [[ollvm-unflattener]] · [[deobfbr]] · [[dprotect]]
