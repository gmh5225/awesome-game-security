---
title: Tools (doomedraven)
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/doomedraven__Tools.md
updated: 2026-08-16
confidence: medium
---

# Tools (doomedraven)

Collection of utility scripts for **malware-analysis infrastructure**: KVM/QEMU virtualization setup, IDA Pro string-deobfuscation scripts, **Volatility3** plugins, database-management helpers, **flare-emu** deobfuscation, **libguestfs** Docker containers, and Windows configuration scripts commonly used in **CAPE/Cuckoo** sandbox environments. Targets analysts and security researchers standing up automated dynamic-analysis labs and performing binary deobfuscation. (source: wiki/sources/descriptions/doomedraven__Tools.md)

Complements Windows analysis VM bundles such as [[flare-vm]] and [[retoolkit]], memory-forensics stacks such as [[volatility3]], and Cuckoo virtual-environment detection research such as [[anticuckoo]].

## Notable scripts

- [kvm-qemu.sh](https://github.com/doomedraven/Tools/blob/master/Virtualization/kvm-qemu.sh) — QEMU/KVM host provisioning (README: `[QEMU Script]`)

## Links

- Repo: https://github.com/doomedraven/Tools

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[flare-vm]] · [[retoolkit]] · [[volatility3]] · [[anticuckoo]]
