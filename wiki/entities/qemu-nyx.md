---
title: QEMU-Nyx
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/nyx-fuzz__QEMU-Nyx.md
updated: 2026-07-27
confidence: medium
---

# QEMU-Nyx

Nyx-fuzz QEMU fork centered on **Intel PT** for hypervisor-assisted fuzzing: fast memory/device reset, precise guest disassembly (including swapped-out / unavailable code) with Intel-PT decoding, breakpoint-based guest instrumentation, and a fuzzing-frontend protocol. (source: wiki/sources/descriptions/nyx-fuzz__QEMU-Nyx.md)

Useful for game-security researchers and reverse engineers in the `Cheat > QEMU/KVM/PVE/VBOX` lane—coverage-guided VM fuzzing rather than guest fingerprint spoofing ([[qemu-anti-detection]]) or architecture-neutral record/replay ([[panda]]).

## Links

- Repo: https://github.com/nyx-fuzz/QEMU-Nyx (README tag: Intel-PT)

## Related

[[panda]] · [[smallworld]] · [[qemu-anti-detection]] · [[qemu-gvm]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
