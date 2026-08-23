---
title: shellcrypt
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Lavender-exe__Shellcrypt.md
updated: 2026-08-23
confidence: medium
---

# shellcrypt

Cross-platform **Python shellcode obfuscation utility** that transforms raw payload bytes into ready-to-paste source for loaders and injectors. Supports multiple encryption ciphers (AES, ChaCha20, RC4, Salsa20, XOR variants), can chain encoding and compression stages, and emits output for C, C#, Go, Rust, Nim, Python, and PowerShell. Primary use: offensive security and game-security research workflows for payload packing, format conversion, and loader prototyping—not an AC product. (source: wiki/sources/descriptions/Lavender-exe__Shellcrypt.md)

Complements academic Caesar-cipher shellcode labs such as [[shellcode-obfuscation]], entropy reduction via [[shellcode-entropyfix]], in-memory page-protection evasion such as [[shellcode-fluctuation]], and shellcode build frameworks such as [[scfw]] and [[shellcode-factory]].

## Links

- Repo: https://github.com/Lavender-exe/Shellcrypt (README: A QoL tool to obfuscate shellcode; future encoding/encryption/compression chaining)

## Related

[[shellcode-obfuscation]] · [[shellcode-entropyfix]] · [[shellcode-fluctuation]] · [[scfw]] · [[shellcode-factory]] · [[2pack]] · [[shoggoth]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
