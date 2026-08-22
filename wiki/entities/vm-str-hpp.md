---
title: vm_str.hpp
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Mowokuma__vm_str.hpp.md
updated: 2026-08-22
confidence: medium
---

# vm_str.hpp

Header-only C++20 compile-time string obfuscation library. Transforms string literals into runtime-reconstructed data: the build generates an obfuscation bytecode schema at compile time, and a small stack-based virtual machine rebuilds strings during execution. Macros expose narrow and wide string forms while aiming to keep plaintext strings out of static program data. Primary use case is software hardening and reverse-engineering resistance in security-sensitive codebases (Anti Cheat → String Crypter). (source: wiki/sources/descriptions/Mowokuma__vm_str.hpp.md)

Distinct from simple XOR constexpr crypters: the VM-backed bytecode path adds an extra reconstruction layer versus direct decrypt-at-runtime libraries. Useful alongside compile-time string crypters such as [[obfuscate]] / [[crystr]] / [[static-string-obfuscation]] / [[skcrypter]] / [[mystic-xorstr]]. Not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/Mowokuma/vm_str.hpp

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[obfuscate]] · [[crystr]] · [[static-string-obfuscation]] · [[skcrypter]] · [[mystic-xorstr]] · [[xorlit]]
