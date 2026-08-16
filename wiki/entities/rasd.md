---
title: RASD
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/cryotb__RASD.md
updated: 2026-08-16
confidence: medium
---

# RASD

**RASD** is a C/C++ research project that reconstructs **return-address spoofing detection** from **R5AC**, the in-house anti-cheat deployed in **Apex Legends**. It replicates stackwalk checks that call `RtlCaptureStackBackTrace` from scattered instrumentation sites and flag callers whose return addresses were not produced by a normal `CALL`, unbacked **RWX / non-module** execution, and common x64 spoof gadgets (`jmp`, `add rsp; ret`, `int3`, and similar patterns). Aimed at anti-cheat engineers and defensive security researchers in the `Detection:Spoof Stack` lane. (source: wiki/sources/descriptions/cryotb__RASD.md)

Ships demonstration tests against open-source return-address spoofers and contrasts legitimate in-module calls with manually mapped cheat code that leaves spoofed frames on the stack when invoking monitored functions.

## Links

- Repo: https://github.com/cryotb/RASD

## Related

[[stack-spoofing]] · [[shadow-stack-walk]] · [[return-address-spoofer]] · [[callstackspoofer-2]] · [[x86-ret-spoof]] · [[vmdtstr]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
