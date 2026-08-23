---
title: Shelter
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/Kudaes__Shelter.md
updated: 2026-08-23
confidence: medium
---

# Shelter

**Shelter** is a **Rust** crate for **ROP-based sleep obfuscation**: it **encrypts in-memory payloads** (AES-128; optional **whole-PE** coverage), **strips execute permission** while sleeping, and **resumes through ROP** when work continues. The design avoids timer- and APC-heavy patterns and integrates **stack spoofing** plus **indirect syscalls** for stealth-focused execution control. Core logic is Rust with **assembly stubs** for low-level behavior. Primary use: advanced red-team tooling research and **in-memory evasion** experimentation in the page-protection / sleep-hide lane. (source: wiki/sources/descriptions/Kudaes__Shelter.md)

Same-author Windows evasion crate: [[unwinder]] (call-stack spoofing). Pairs with related sleep/page-protection PoCs such as [[deepsleep]], [[death-sleep]], and [[shellcode-fluctuation]].

## Links

- Repo: https://github.com/Kudaes/Shelter

## Related

[[unwinder]] · [[deepsleep]] · [[death-sleep]] · [[shellcode-fluctuation]] · [[stack-spoofing]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
