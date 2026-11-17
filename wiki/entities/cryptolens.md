---
title: CryptoLens
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ShadowStrike-Labs__CryptoLens.md
updated: 2026-11-17
confidence: medium
---

# CryptoLens

IDA Pro plugin and standalone **Python** package for locating **cryptographic**, **hashing**, and related code in x86/x64 **Windows** binaries. It combines static scans of constants, lookup tables, instruction patterns, and function structure with optional **Hex-Rays** decompiler analysis, **API-name hash** resolution, library and key fingerprinting, **entropy mapping**, and debugger memory recovery for live keys and cipher state. The built-in catalog covers SHA-2, MD5, BLAKE2, Keccak, AES, ChaCha, RC4, MurmurHash, xxHash, FNV, SipHash, and many CRC and PRNG families, with precision rules that reduce false positives from isolated constant matches. Results can be browsed in IDA, annotated in the database, or exported as **JSON** or **HTML**; the same engines run from a **CLI** without IDA. Aimed at reverse engineers and security researchers triaging protected executables, cheats, malware, and other Windows binaries. (source: wiki/sources/descriptions/ShadowStrike-Labs__CryptoLens.md)

Broader algorithm fingerprinting than constant-only YARA hits—complements [[findcrypt-yara]] and [[ghidra-findcrypt]], and sits beside title-specific decrypt helpers such as [[ida-plugin-strings-decryptor-anogs]]. Cheat / IDA Plugins lane.

## Capabilities

- **Multi-signal static scan** — constants, S-boxes/tables, instruction idioms, and function-shape heuristics with false-positive controls.
- **Optional Hex-Rays** — decompiler-assisted confirmation on matched regions.
- **API hash & library ID** — resolve hashed import names; fingerprint known crypto libraries and key material.
- **Entropy & debugger recovery** — map high-entropy regions; recover live keys/cipher state from process memory during debug sessions.
- **Export** — IDA annotations, JSON/HTML reports, headless CLI for batch pipelines.

## Links

- Repo: https://github.com/shadowstrike-labs/cryptolens

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[findcrypt-yara]] · [[ghidra-findcrypt]] · [[findyara-ida]] · [[auto-re]] · [[ida-plugins]] · [[list-of-ida-plugins]]