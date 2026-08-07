---
title: VT debuger
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__vt-debuger.md
updated: 2026-08-07
confidence: medium
---

# VT debuger

Hypervisor-based debugger that uses **Intel VT-x** to debug programs without triggering standard debugger detection. A thin hypervisor places the target under hardware-assisted virtualization and intercepts execution through **VM exits**, providing breakpoint, single-step, and memory-watch capabilities that remain invisible to typical anti-debugging checks. Aimed at reverse engineers studying anti-debug–protected software. (source: wiki/sources/descriptions/gmh5225__vt-debuger.md)

Sits in the VT-x stealth-debugging lane beside [[erisdbg]] and hacked-hypervisor stress tooling such as [[vt-debuuger]] — useful for mapping virtualization-assisted debug surfaces, not a production anti-cheat component.

## Links

- Repo: https://github.com/gmh5225/vt-debuger (README tag: VT debuger)

## Related

[[erisdbg]] · [[vt-debuuger]] · [[hypervisor]] · [[hv]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
