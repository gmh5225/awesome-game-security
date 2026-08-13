---
title: EAC
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__EAC.md
updated: 2026-08-13
confidence: medium
---

# EAC

Mixed **Easy Anti-Cheat** reference bundle (gmh5225; cheat / explore anticheat:eac) — not a single runnable project. Combines reversed `easyanticheat.sys` source focused on kernel callback logic (driver dispatch validation, Process Hacker driver detection, blacklisted-driver checks, `ntoskrnl` patch scanning, driver hashing routines) with an **EAC/EOS SDK** tree (binaries, headers, tools such as `EOS_FileDecryptionTool`). Useful for reverse engineers studying [[easy-anti-cheat]] kernel heuristics, driver integrity monitoring, and the SDK surface used by EAC and EOS deployments. Complements decompile dumps such as [[easyanticheat-reversing]], reimplemented reversed-source archives such as [[eazy-anti-cheat-src]], and extract utilities such as [[eac-extractor-utility]] by pairing callback-focused reversed driver logic with integration artifacts. (source: wiki/sources/descriptions/gmh5225__EAC.md)

## Links

- Repo: https://github.com/gmh5225/EAC

## Related

[[easy-anti-cheat]] · [[easyanticheat-reversing]] · [[eazy-anti-cheat-src]] · [[eac-extractor-utility]] · [[eac-bypass-1]] · [[kernel-callbacks]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
