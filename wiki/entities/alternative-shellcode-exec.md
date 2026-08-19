---
title: Alternative Shellcode Exec
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/aahmad097__AlternativeShellcodeExec.md
updated: 2026-08-19
confidence: medium
---

# Alternative Shellcode Exec

Windows **Alternative Code Execution** collection: C++ Visual Studio proof-of-concept samples that run position-independent shellcode through callback APIs instead of `CreateThread`. Each project demonstrates a different callback-based execution primitive and API-abuse pattern aimed at reducing reliance on common injection paths. Primary use case is offensive security and game-security research into user-mode evasion and detection bypass. (source: wiki/sources/descriptions/aahmad097__AlternativeShellcodeExec.md)

Complements shellcode injection toolkits such as [[jektor]], object-to-shellcode frameworks such as [[obj2shellcode]], and broader injection corpora such as [[windows-process-injection]].

## Links

- Repo: https://github.com/aahmad097/AlternativeShellcodeExec

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[jektor]] · [[obj2shellcode]] · [[scfw]] · [[shellcode-factory]] · [[windows-process-injection]]
