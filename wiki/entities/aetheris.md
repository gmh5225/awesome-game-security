---
title: Aetheris
kind: entity
topics: [dma-attack, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/Dray973__Aetheris.md
updated: 2026-08-31
confidence: medium
---

# Aetheris

PyQt6 Windows forensics suite (Aetheris Quantum Core) combining process/memory forensics, storage analysis, live network/firewall control, registry engineering, and natural-language automation in one dashboard. Optional native engines include MemProcFS, Capstone, Keystone, and PCILeech-FPGA for guarded physical-memory read/write alongside process autopsy (Authenticode verification), MFT parsing, GeoIP-enriched connection monitoring, and persistence auditing. Emphasizes an auditable reversible trust model—hash-chained logging, global dry-run rehearsal, Omega Rollback undo, and confirmation gates on destructive actions. Plugin API plus headless CLI for scheduled forensic capture. (source: wiki/sources/descriptions/Dray973__Aetheris.md)

## Role in the DMA stack

GUI forensics workspace lane distinct from low-level libraries ([[volk-dma]], [[dmalibrary]]) and agent MCP bridges ([[pcileech-memprocfs-mcp]])—integrates PCILeech-FPGA DMA R/W with broader live-system instrumentation for malware, persistence, and privilege-escalation research on controlled machines. (source: wiki/sources/README-categories.md)

Not to be confused with CSIT-SG [[aether]] (IDA Pro LLM copilot).

## Links

- Repo: https://github.com/Dray973/Aetheris

## Related

[[pcileech]] · [[pcileech-fpga]] · [[pcileech-memprocfs-mcp]] · [[memtools]] · [[volk-dma]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
