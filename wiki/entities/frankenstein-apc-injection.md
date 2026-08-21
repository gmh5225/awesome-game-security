---
title: FrankensteinAPCInjection
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/S12cybersecurity__FrankensteinAPCInjection.md
updated: 2026-08-21
confidence: medium
---

# FrankensteinAPCInjection

Windows **process injection** proof of concept (C++) that executes payloads by **reusing existing system resources** instead of allocating new ones. Finds **leaked process and thread handles**, locates **pre-existing RWX memory**, and queues special user APCs through **`NtQueueApcThreadEx2`**. Avoids high-noise APIs such as `VirtualAllocEx`, `VirtualProtectEx`, and `CreateRemoteThread`; includes optional shellcode encryption. Intended for offensive security research and for evaluating how EDR or anti-cheat products detect low-footprint injection paths. (source: wiki/sources/descriptions/S12cybersecurity__FrankensteinAPCInjection.md)

README lane: NtQueueApcThreadEx2 + existing handles & natural RWX.

Complements sibling RWX discovery tooling such as [[rwxfinder]] and broader injection corpora such as [[windows-process-injection]] and APC study samples such as [[apc-research]].

## Links

- Repo: https://github.com/S12cybersecurity/FrankensteinAPCInjection

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[rwxfinder]] · [[windows-process-injection]] · [[apc-research]] · [[poolparty]] · [[injectors]]
