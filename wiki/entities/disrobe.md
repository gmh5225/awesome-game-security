---
title: disrobe
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/1-3-7__disrobe.md
updated: 2026-09-10
confidence: medium
---

# disrobe

**Rust-based modular platform** for unpacking, analyzing, and recovering readable code from **protected and obfuscated binaries**. Crate architecture spans native PE packers, Python protections (PyArmor, PyInstaller), mobile APKs, WebAssembly, JVM, .NET, Go, Erlang/BEAM, JavaScript, and many archive/container formats. Integrates with **Ghidra** for unpack and decompile workflows; ships **Python and TypeScript bindings**; includes benchmark harnesses that grade recovery quality against fixture corpora. Targets reverse engineers, malware analysts, and security researchers who need to strip packers, deobfuscate bytecode, and reconstruct logic from hardened executables. (source: wiki/sources/descriptions/1-3-7__disrobe.md)

Complements format-specific tooling such as [[de4py]] (Python obfuscator analysis), [[decbench]] (decompiler benchmarking), and curated packing indexes like [[awesome-executable-packing]].

## Links

- Repo: https://github.com/1-3-7/disrobe

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[de4py]] · [[decbench]] · [[awesome-executable-packing]] · [[pe-protector]] · [[pyarmor]] · [[control-flow-flattening]] · [[research-rigor]]
