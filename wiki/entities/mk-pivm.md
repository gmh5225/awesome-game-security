---
title: mkPIVM
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/D7EAD__mkPIVM.md
updated: 2026-08-26
confidence: medium
---

# mkPIVM

**Process-independent virtual machine code obfuscation engine** (D7EAD) that lifts **x86/x64** instructions—including arbitrary shellcode—into a **custom intermediate representation**, generates **polymorphic position-independent virtual machine (PIVM)** bytecode with **encrypted handlers**, and **embeds the VM dispatcher into PE executables**. Aimed at anti-cheat engineers and reverse engineers studying VM-based native protection in the Anti Cheat → Obfuscation Engine / `[VM]` lane. (source: wiki/sources/descriptions/D7EAD__mkPIVM.md)

Useful as an open PIVM/shellcode-to-VM pipeline reference alongside [[binary-shield]], [[guardian-rs]], [[covirt]], and [[x64-virtualizer-rs]] — emphasizing process-independent polymorphic VM generation rather than a fixed commercial protector model.

## Links

- Repo: https://github.com/D7EAD/mkPIVM

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[binary-shield]] · [[guardian-rs]] · [[covirt]] · [[x64-virtualizer-rs]] · [[phantasm-x86-virtualizer]] · [[vmattack]]
