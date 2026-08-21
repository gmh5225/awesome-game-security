---
title: Copy RVA
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/RomanRybachek__Copy_RVA.md
updated: 2026-08-21
confidence: medium
---

# Copy RVA

**Copy RVA** (RomanRybachek) is a lightweight **IDA Pro plugin** that copies the **RVA under the cursor** to the clipboard. Implemented as a Python IDAPython script, it integrates into the standard IDA plugin workflow and context menu. The tool helps when setting breakpoints in WinDbg on drivers that lack public symbols by quickly converting static disassembly locations into usable RVAs for live kernel debugging. Aimed at reverse engineers and kernel or game security researchers who need faster offset handling between IDA static analysis and WinDbg attach. (source: wiki/sources/descriptions/RomanRybachek__Copy_RVA.md)

Complements sibling [[ioctl-helper]] for RomanRybachek driver-RE tooling, and IDA driver-annotation plugins such as [[driver-buddy-reloaded]] and [[ida-kmdf]] when bridging static driver IDBs to live WinDbg sessions.

## Links

- Repo: https://github.com/RomanRybachek/Copy_RVA

## Related

[[ioctl-helper]] · [[driver-buddy-reloaded]] · [[ida-kmdf]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
