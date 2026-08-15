---
title: Shoggoth
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/frkngksl__Shoggoth.md
updated: 2026-08-15
confidence: medium
---

# Shoggoth

**Polymorphic x86/x64 shellcode encoder** that uses the **asmjit** JIT assembler to emit unique, position-independent encrypted payloads on each run. Applies **two encryption layers** with **randomized decoder stubs**, yielding output executable directly as shellcode. Bundles standalone **COFF and PE reflective loaders** (position-independent blobs) for loading Cobalt Strike BOFs or arbitrary PE executables from memory. Listed under Anti Cheat → Polymorphic Encryptor / shellcode engine & tricks; aimed at red-team operators and defensive researchers studying polymorphic shellcode and in-memory PE/BOF loading—not an AC product. (source: wiki/sources/descriptions/frkngksl__Shoggoth.md)

Complements bad-byte banishment via [[byvalver]], shellcode factory tooling such as [[shellcode-factory]], entropy reduction such as [[shellcode-entropyfix]], and AsmJit-based PE mutation such as [[alcatraz]].

## Links

- Repo: https://github.com/frkngksl/Shoggoth

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[byvalver]] · [[shellcode-factory]] · [[shellcode-entropyfix]] · [[2pack]] · [[usb-monitor-bof]] · [[shredder-rs]]
