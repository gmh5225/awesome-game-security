---
title: rust-obfuscator
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/dronavallipranav__rust-obfuscator.md
updated: 2026-08-16
confidence: medium
---

# rust-obfuscator

Set of **Rust source-level obfuscation** tools centered on an automatic obfuscator that walks Rust projects and inserts procedural macros for string-literal encryption, control-flow flattening, and symbol renaming. Ships the **`cryptify`** proc-macro crate for fine-grained compile-time string encryption and **`labyrinth_macros`** for source-level control-flow obfuscation. Aimed at security researchers and Rust developers studying source-level obfuscation techniques and hardening Rust binaries against static analysis—not a commercial protector. (source: wiki/sources/descriptions/dronavallipranav__rust-obfuscator.md)

Useful as a Rust-language Obfuscation Engine reference alongside LLVM IR pass tools such as [[the-poor-mans-obfuscator]] and post-compile PE mutators such as [[obfuscator]].

## Links

- Repo: https://github.com/dronavallipranav/rust-obfuscator

## Related

[[overviews/reverse-engineering]] · [[control-flow-flattening]] · [[javascript-obfuscator]] · [[the-poor-mans-obfuscator]] · [[obfuscator]] · [[skcrypter]]
