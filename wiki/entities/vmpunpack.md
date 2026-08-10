---
title: vmpunpack
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/milk-analyzer__vmpunpack.md
updated: 2026-08-10
confidence: medium
---

# vmpunpack

Generic **x64 Windows PE unpacker** for VMProtect and similar packers. Written in **Python 3.8+** with stdlib-only dependencies, it drives a packed sample through a patched **sogen** emulator that bypasses anti-VM and anti-debug checks, runs the packer stub to the original entry point (OEP), and dumps the unpacked memory image. The tool reconstructs a loadable PE suitable for static analysis in IDA or Ghidra, extracts IOCs such as domains, URLs, and IP addresses from the dump, and automatically fills ordinal import gaps in the emulation environment. It unpacks protected binaries but **does not devirtualize** VMProtect bytecode, leaving virtualized functions intact for further manual analysis. Primary audience: malware analysts and reverse engineers who need to unpack VMProtect-protected samples in locked-down analysis environments. (source: wiki/sources/descriptions/milk-analyzer__vmpunpack.md)

Complements static LZMA-based unpack via [[vmpunpacker]] and Go static rebuild via [[vmpstatic]]; differs from emulation generic-packers like [[xvolkolak]] by targeting VMProtect/packer stubs with sogen and stdlib-only Python for air-gapped labs. Pair unpacked output with Fix VMP devirt tooling such as [[novmpy]], [[rumba]], or [[vmp-vmp3-64bit-disasm-prerelease-]] when virtualized functions remain.

## Links

- Repo: https://github.com/milk-analyzer/vmpunpack

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[vmpunpacker]] · [[vmpstatic]] · [[xvolkolak]] · [[novmpy]] · [[rumba]]
