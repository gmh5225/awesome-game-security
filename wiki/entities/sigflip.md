---
title: SigFlip
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/med0x2e__SigFlip.md
updated: 2026-07-30
confidence: medium
---

# SigFlip

Patches Authenticode-signed PE files (EXE, DLL, SYS, etc.) without invalidating the embedded signature. **SigInject** encrypts and injects shellcode into the image's `WIN_CERTIFICATE` certificate table, prints the encryption key, and writes a modified PE that keeps signature and certificate validity intact. A basic BOF/C/C# **SigLoader** consumes the key to decrypt and run the payload. Aimed at Some Tricks / Windows Ring3 research for studying weak Authenticode trust checks. (source: wiki/sources/descriptions/med0x2e__SigFlip.md)

Contrasts with [[sigthief]] (transplant `certTable` onto unsigned binaries) and complements `WIN_CERTIFICATE` digest work such as [[pedigest]]: here the focus is in-place certificate-table steganography while preserving an existing valid signature.

## Links

- Repo: https://github.com/med0x2e/SigFlip

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[sigthief]] · [[pedigest]] · [[totalpe2]]
