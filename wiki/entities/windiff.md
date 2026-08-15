---
title: WinDiff
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/ergrelet__windiff.md
updated: 2026-08-15
confidence: medium
---

# WinDiff

Web-based tool for browsing and comparing symbols, types, and syscalls across different versions of Microsoft Windows binaries. A Rust CLI downloads PE files via Winbindex, fetches matching PDBs from the Microsoft symbol server, and extracts exported symbols, reconstructed types, modules, and syscall tables into gzip-compressed JSON databases. A Next.js/React frontend loads those static databases and provides Browse and Diff views for side-by-side comparison across OS builds. Targets reverse engineers and security researchers analyzing Windows internals, EDR/anti-cheat surfaces, and version-to-version kernel or user-mode binary changes. (source: wiki/sources/descriptions/ergrelet__windiff.md)

Complements IDA-centric binary diffing via [[diaphora]] and [[binexport]] by pre-indexing cross-build symbol/type/syscall metadata without importing each PE into a disassembler. Pairs with offline symbol caches such as [[mssymbolscollection]] and manifest tooling such as [[pdblister]], and with SSN extraction tools such as [[ntsleuth]] when syscall-table deltas need programmatic follow-up.

## Links

- Repo: https://github.com/ergrelet/windiff

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[diaphora]] · [[binexport]] · [[mssymbolscollection]] · [[pdblister]] · [[ntsleuth]] · [[win32k-file-collection]] · [[ntoskrnl-file-collection]]
