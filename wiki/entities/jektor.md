---
title: Jektor
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gavz__Jektor.md
updated: 2026-08-15
confidence: medium
---

# Jektor

Windows **shellcode injection toolkit** demonstrating five execution techniques: `CreateThread`, `CreateRemoteThread` (into a hidden notepad process), `QueueUserAPC` with `NtTestAlert` APC queue flush, `EnumTimeFormatsEx` callback abuse, and `CreateFiber` scheduling. All API calls are dynamically resolved via `GetProcAddress` at runtime to avoid IAT entries; payloads use XOR-encrypted msfvenom shellcode with NOP-sled prepending to evade signature-based detection. Listed under Injection/Shellcode Testing for AC stress evaluation and offensive injection tradecraft study. (source: wiki/sources/descriptions/gavz__Jektor.md)

Complements broader injection corpora such as [[windows-process-injection]] and focused injection-testing harnesses such as [[injectors]].

## Links

- Repo: https://github.com/gavz/Jektor

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[injectors]] · [[scfw]] · [[shellcode-factory]] · [[obj2shellcode]]
