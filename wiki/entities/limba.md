---
title: limba
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/ThatLing__limba.md
updated: 2026-08-20
confidence: medium
---

# limba

Proof-of-concept **compile-time control-flow obfuscation** using **mixed boolean-arithmetic (MBA)** transformations. Generates boilerplate that hides real call targets by encoding jump addresses with randomized rewrite rules and per-build offsets. C++20-focused; targets Clang/clang-cl toolchains with premake-based integration examples. Intended for reverse-engineering resistance research and binary obfuscation experimentation (Cheat → compile-time control flow obfuscation using MBA). (source: wiki/sources/descriptions/ThatLing__limba.md)

Offensive-side MBA tooling distinct from expression generators such as [[mutaben]] and [[mba-obfuscator]] or deobfuscators such as [[cobra]] and [[promba]]; complements compile-time string/call hiding libraries such as [[obfusheader-h]] and [[crycall]].

## Links

- Repo: https://github.com/ThatLing/limba

## Related

[[mixed-boolean-arithmetic]] · [[control-flow-flattening]] · [[overviews/reverse-engineering]] · [[mutaben]] · [[mba-obfuscator]] · [[mixed-boolean-transform]] · [[obfusheader-h]] · [[promba]] · [[cobra]]
