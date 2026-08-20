---
title: Shellcode-Obfuscation
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/n1h-nb__Shellcode-Obfuscation.md
updated: 2026-08-20
confidence: medium
---

# Shellcode-Obfuscation

Academic lab project exploring **shellcode obfuscation** to evade Windows **antivirus** detection. Implements a **Caesar-cipher** encoding pipeline: a **Python** obfuscator transforms raw shellcode bytes and a **C** loader decodes and executes the payload via **`VirtualAlloc`** and in-memory execution. Includes a baseline unmodified shellcode loader for comparison and documents how **signature**, **heuristic**, and **machine-learning** AV methods detect raw payloads versus obfuscated variants, with bypass-rate measurements. Aimed at offensive security researchers and defenders studying obfuscation impact on detection—not an AC product. (source: wiki/sources/descriptions/n1h-nb__Shellcode-Obfuscation.md)

Complements entropy-reduction tooling such as [[shellcode-entropyfix]], in-memory page-protection evasion such as [[shellcode-fluctuation]], and shellcode build frameworks such as [[scfw]] and [[shellcode-factory]].

## Links

- Repo: https://github.com/n1h-nb/Shellcode-Obfuscation

## Related

[[shellcode-entropyfix]] · [[shellcode-fluctuation]] · [[scfw]] · [[shellcode-factory]] · [[2pack]] · [[byvalver]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
