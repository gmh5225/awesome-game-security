---
title: LazySign
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering, windows-kernel, mobile-security]
sources:
  - wiki/sources/descriptions/jfmaes__LazySign.md
updated: 2026-08-03
confidence: medium
---

# LazySign

Fake-certificate Authenticode signing with zero additional dependencies—all bundled binaries come from Microsoft's own devkits. Aimed at low-level Windows, Linux, and mobile researchers in the Some Tricks / Windows Ring3 lane. README category: Fake Cert. (source: wiki/sources/descriptions/jfmaes__LazySign.md)

Contrasts with leaked-cert signers such as [[magic-signer]] and expiry-bypass sideloads such as [[sign-expired]]: here the focus is synthesizing fake cert material from Microsoft SDK tooling, not transplanting real signatures ([[sigthief]]), patching signed PE certificate tables ([[sigflip]]), or injecting structurally plausible but invalid Authenticode blobs via [[fakesign]].

## Links

- Repo: https://github.com/jfmaes/LazySign

## Related

[[sigthief]] · [[sigflip]] · [[sign-expired]] · [[magic-signer]] · [[pesign-analyzer]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
