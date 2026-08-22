---
title: VPGATHER
kind: entity
topics: [reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/Peribunt__VPGATHER.md
updated: 2026-08-22
confidence: medium
---

# VPGATHER

User-mode proof of concept for **stealth address-validity probing** — tests whether a virtual address would fault before directly dereferencing it. Uses **AVX2 VPGATHER** instruction behavior plus **vectored exception handling** to infer accessibility with reduced side effects on target memory state. Includes CPU support checks and a simple API for repeated probes. Relevant to reverse engineering, anti-cheat bypass research, and low-level security work where conventional RPM or pointer dereference would disturb page state or trigger stronger AC signals. (source: wiki/sources/descriptions/Peribunt__VPGATHER.md)

Defensive research such as [[bloodhound]] applies the same VPGATHER accessibility technique for EPT/NPT hook detection rather than offensive memory recon.

## Links

- Repo: https://github.com/Peribunt/VPGATHER

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[bloodhound]] · [[cpp-veh-dbi]]
