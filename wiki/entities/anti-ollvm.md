---
title: anti-ollvm
kind: entity
topics: [reverse-engineering, mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/IIIImmmyyy__AntiOllvm.md
updated: 2026-08-24
confidence: medium
---

# anti-ollvm

**AntiOllvm** (IIIImmmyyy) is an **Arm64 simulated execution framework** for removing **OLLVM control-flow flattening**. It identifies dispatcher patterns and reconstructs complete **if-else control-flow graphs** from obfuscated functions. The core tool is written in **C#**, with companion **Python** scripts for **IDA CFG extraction**, machine-code generation via **Keystone**, and CFG rebuilding. Targets reverse engineers analyzing obfuscated binaries in security and game-protection research. README tag: `[AntiOllvm Fla with Fake Runtime]`. (source: wiki/sources/descriptions/IIIImmmyyy__AntiOllvm.md)

Complements x86/x64 Miasm-based [[ollvm-unflattener]] and angr-backed [[idadeflat]] with an **AArch64 fake-runtime** deflatten lane; pairs with ARM64 branch-deobfuscation tooling such as [[deobfbr]] on Android `.so` targets.

## Links

- Repo: https://github.com/IIIImmmyyy/AntiOllvm

## Related

[[control-flow-flattening]] · [[ollvm-unflattener]] · [[idadeflat]] · [[deobfbr]] · [[d810-ng]] · [[unflat]] · [[armshellcode]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]]
