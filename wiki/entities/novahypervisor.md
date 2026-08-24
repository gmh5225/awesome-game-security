---
title: NovaHypervisor (Idov31)
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Idov31__NovaHypervisor.md
updated: 2026-08-24
confidence: medium
---

# NovaHypervisor (Idov31)

**NovaHypervisor** is a **defensive x64 Intel host hypervisor** (Idov31) for protecting **sensitive kernel memory regions**. It enforces **memory access policies** and protects selected addresses with **read, write, or execute controls**, aiming to **mitigate kernel attacks such as BYOVD**. Implemented in **C++ and assembly** as a **Windows kernel driver**, with a **companion client** for adding and removing protections and **support tooling for logging**. Intended mainly for **anti-cheat and endpoint defense research** in virtualized kernel security. (source: wiki/sources/descriptions/Idov31__NovaHypervisor.md)

Defensive counterpart to offensive VT-x/EPT stacks such as [[hypervisor]] and [[ophion]], and to EPT read deception such as [[notruth]]. Complements [[byovd]] threat modeling and platform trust features such as [[hvci]]. Same author lane as [[idov31-venom]].

## Links

- Repo: https://github.com/Idov31/NovaHypervisor [NovaHypervisor is a defensive x64 Intel host based hypervisor. The goal of this project is to protect against kernel based attacks]

## Related

[[byovd]] · [[hvci]] · [[hypervisor]] · [[ophion]] · [[notruth]] · [[idov31-venom]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
