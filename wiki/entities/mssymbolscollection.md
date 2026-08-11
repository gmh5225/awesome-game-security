---
title: MSSymbolsCollection
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__MSSymbolsCollection.md
updated: 2026-08-11
confidence: medium
---

# MSSymbolsCollection

Pre-downloaded collection of **Microsoft debug symbols (PDB files)** for Windows system components. Ships symbol files for **`ntoskrnl`**, **`CI.dll`**, and other kernel-mode binaries used in kernel reverse engineering and driver development—reducing reliance on live Microsoft Symbol Server pulls during offline RE. (source: wiki/sources/descriptions/gmh5225__MSSymbolsCollection.md)

Complements on-demand manifest generation via [[pdblister]] and programmatic PDB parsing via [[pdb]] / [[pdb-rs]]. Pair with [[ntoskrnlwalker]] / [[ntkernelwalkerlib]] for build-target offset and gadget resolution, and with [[ntsleuth]] for syscall-table extraction once symbols are loaded in IDA or WinDbg.

## Links

- Repo: https://github.com/gmh5225/MSSymbolsCollection

## Related

[[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[pdblister]] · [[pdb]] · [[pdb-rs]] · [[ntoskrnlwalker]] · [[ntkernelwalkerlib]] · [[ntsleuth]] · [[ntoskrnl-file-collection]] · [[research-rigor]]
