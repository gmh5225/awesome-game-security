---
title: wrappe
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Systemcluster__wrappe.md
updated: 2026-08-20
confidence: medium
---

# wrappe

Cross-platform Rust packer that bundles an executable plus its resource directory into a single self-contained binary. Uses Zstandard compression with parallel packing and unpacking, streaming decompression, and metadata/resource transfer support. Designed to simplify portable one-file deployment for desktop applications and tools while keeping startup overhead and artifact size practical. Listed under Anti Cheat → Binary Packer (`[Rust]`); useful for studying application bundling and compressed self-extracting distribution patterns rather than PE-specific runtime protection. (source: wiki/sources/descriptions/Systemcluster__wrappe.md)

Useful as a cross-platform Rust bundler reference alongside [[oxide]], [[2pack]], and [[papaw]] (zstd)—not a full unpacker or debugger.

## Links

- Repo: https://github.com/Systemcluster/wrappe

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[oxide]] · [[2pack]] · [[papaw]] · [[awesome-executable-packing]]
