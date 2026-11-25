---
title: unpack
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/orca-zhang__unpack.md
updated: 2026-11-25
confidence: medium
---

# unpack

**Rust-centric packer inspection and layered static unpacking** for protected executables. Detects packers and protectors, decodes compressed payloads, and **recursively peels nested layers** without executing samples. The Rust core ships native decoders for common compression schemes and integrates the official **UPX** backend; Go drivers extend format coverage to roughly **twenty-two** schemes including **ASPack**, **Themida**, **VMProtect**, **MPRESS**, and other PE-focused protectors. Surfaces include a CLI, an embeddable Rust library, and a **Go SDK** for automated pipelines. Where full unpack is unavailable, **static PE recovery** can repair headers, sections, and entry points for downstream disassembly. Targets reverse engineers, malware analysts, and game-security researchers who need reliable format identification and non-executing layered unpacking on Windows and cross-platform binaries. (source: wiki/sources/descriptions/orca-zhang__unpack.md)

Complements multi-format static recovery such as [[disrobe]], Python malware unpack pipelines such as [[unpacker]], and curated packing indexes such as [[awesome-executable-packing]].

## Links

- Repo: https://github.com/orca-zhang/unpack

## Related

[[overviews/reverse-engineering]] · [[disrobe]] · [[unpacker]] · [[unlicense]] · [[magicmida-rs]] · [[vmpunpacker]] · [[awesome-executable-packing]] · [[pe-protector]] · [[static-runtime-evidence]] · [[research-rigor]]