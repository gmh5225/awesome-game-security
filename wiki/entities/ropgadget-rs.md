---
title: ropgadget-rs
kind: entity
topics: [reverse-engineering, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/hugsy__ropgadget-rs.md
updated: 2026-08-05
confidence: medium
---

# ropgadget-rs

Rust **ROP gadget finder** for discovering Return-Oriented Programming chains in binary executables. Scans **PE**, **ELF**, and **Mach-O** images for instruction sequences ending in return instructions that can be chained for exploitation; parallel scanning targets large binaries quickly. Aimed at exploit developers and vulnerability researchers building ROP chains for binary exploitation. (source: wiki/sources/descriptions/hugsy__ropgadget-rs.md)

Complements build-specific kernel gadget resolution via [[ntkernelwalkerlib]] / [[ntoskrnlwalker]] and general exploit-chain research beside samples such as [[smep-bypass]] and [[deepsleep]].

## Links

- Repo: https://github.com/hugsy/ropgadget-rs

## Related

[[ntkernelwalkerlib]] · [[ntoskrnlwalker]] · [[smep-bypass]] · [[deepsleep]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
