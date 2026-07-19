---
title: Volatility
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/volatilityfoundation__volatility.md
updated: 2026-07-19
confidence: medium
---

# Volatility

Original Python 2 memory forensics framework for analyzing RAM dumps from Windows, Linux, and macOS. Plugin surface covers process listing (`pslist` / `psscan`), DLL enumeration, registry hive extraction, network connection recovery, kernel module detection, rootkit identification, and malware artifact analysis. Supports multiple address-space backends (raw dumps, crash dumps, hibernation files, VMware snapshots, FireWire/IEEE 1394) and profile-based type definitions for OS-version-specific structure parsing, including tools to build Linux/Mac kernel profiles from debug symbols. Useful for DFIR, malware research, and game-security post-mortem analysis of injected code, hidden processes, and rootkit artifacts. Successor lineage: [[volatility3]]. (source: wiki/sources/descriptions/volatilityfoundation__volatility.md)

## Links

- Repo: https://github.com/volatilityfoundation/volatility

## Related

[[volatility3]] · [[kvcforensic]] · [[systeminformer]] · [[openark]] · [[file-recovery-tool]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
