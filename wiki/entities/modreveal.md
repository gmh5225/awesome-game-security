---
title: modreveal
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/jafarlihi__modreveal.md
updated: 2026-08-04
confidence: medium
---

# modreveal

C tool to **find hidden Linux kernel modules** — listed under **Anti Cheat → Detection:Hide** for anti-cheat engineers and defensive security researchers studying LKMs that evade normal `/proc/modules` or `lsmod` enumeration (rootkit-style module concealment). (source: wiki/sources/descriptions/jafarlihi__modreveal.md)

Complements Windows-side hide detectors such as [[hidden-module-detector]] and offensive Linux LKM work such as [[venom]] / [[vermagic]] in the same kernel-module research lane.

## Links

- Repo: https://github.com/jafarlihi/modreveal

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[hidden-module-detector]] · [[venom]] · [[vermagic]] · [[vmlinux-to-elf]]
