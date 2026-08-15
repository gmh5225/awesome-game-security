---
title: DaliVM
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/fatalSec__DaliVM.md
updated: 2026-08-15
confidence: medium
---

# DaliVM

Python-based Dalvik virtual machine emulator that executes DEX bytecode through opcode interpretation, class loading, and Android API mocking. Supports static analysis and dependency tracing for Android malware analysis and reverse engineering without requiring a full Android runtime. README highlights string decryption, Multi-DEX support, and Dalvik bytecode emulation for Android static analysis. (source: wiki/sources/descriptions/fatalSec__DaliVM.md)

Complements smali-layer editors such as [[dalvikus]] and DEX→Java decompilers such as [[jadx]] by actually running Dalvik bytecode paths in Python—useful when obfuscated string decryption or control-flow logic must be exercised offline rather than only disassembled.

## Links

- Repo: https://github.com/fatalSec/DaliVM

## Related

[[dalvikus]] · [[jadx]] · [[dex2jar]] · [[rnidbg]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
