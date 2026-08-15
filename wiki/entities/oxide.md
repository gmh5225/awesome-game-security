---
title: oxide
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/frank2__oxide.md
updated: 2026-08-15
confidence: medium
---

# oxide

Rust-based PE binary packer that uses the `exe-rs` crate to parse and rewrite Portable Executable files, embedding a compressed payload with a trampoline-based unpacking stub. The stub uses TLS callback entry points (x86 and x64 NASM sources) to decompress and execute the original binary at runtime. Architecture is intentionally extensible for adding obfuscation or anti-reversing passes beyond simple compression. Listed under Anti Cheat → Binary Packer (`[Written by Rust]`); aimed at software protection researchers studying PE packing techniques rather than shipping as an AC product. (source: wiki/sources/descriptions/frank2__oxide.md)

Useful as a Rust PE packer reference alongside [[2pack]], [[atom-pe-packer]], and [[packer-tutorial]]—not a full unpacker or debugger.

## Links

- Repo: https://github.com/frank2/oxide

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[2pack]] · [[atom-pe-packer]] · [[x64-exe-packer]] · [[packer-tutorial]] · [[awesome-executable-packing]]
