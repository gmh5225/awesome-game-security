---
title: pdb-rs
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/microsoft__pdb-rs.md
updated: 2026-07-30
confidence: medium
---

# pdb-rs

Microsoft’s Rust PDB (Program Database) reader/writer with full MSF container support, CodeView symbol and type records, DBI stream parsing, TPI/IPI streams, and COFF image metadata. The `codeview` crate encodes/decodes symbol kinds (`S_PUB`, `S_PROC`, `S_LOCAL`) and type records (`LF_CLASS`, `LF_POINTER`, `LF_PROCEDURE`) with architecture-specific register mappings for x86, AMD64, and ARM64. (source: wiki/sources/descriptions/microsoft__pdb-rs.md)

Useful for programmatic PDB inspection or generation in Rust tooling—pair with [[pdblister]] for Symbol Server manifest prefetch and [[pdb]] (DIA SDK) or [[pdbr]] (standalone Python extract) or dbghelp loads in debuggers when a Windows-native stack is preferred.

## Links

- Repo: https://github.com/microsoft/pdb-rs

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[pdb]] · [[pdblister]] · [[pdbr]] · [[kpdb]] · [[ntsleuth]] · [[totalpe2]] · [[x64dbg]]
