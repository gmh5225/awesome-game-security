---
title: hXOR-Packer
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/akuafif__hXOR-Packer.md
updated: 2026-08-18
confidence: medium
---

# hXOR-Packer

C++ Windows PE packer and unpacker that compresses and encrypts executables, then rebuilds them as self-unpacking files. Combines Huffman compression with simple XOR encryption; CLI supports compression only, encryption only, or both. The unpacking stub restores the payload and executes it directly from memory instead of writing an unpacked file to disk. Listed under Anti Cheat → Binary Packer (`[PE XOR]`). Mainly useful for learning PE internals, runtime loading techniques, and packer behavior in malware and anti-malware research. (source: wiki/sources/descriptions/akuafif__hXOR-Packer.md)

Useful as an educational Huffman+XOR PE packer reference alongside [[exe-packer]], [[xorpacker]], and [[x64-exe-packer]]—not a full unpacker or commercial protector.

## Links

- Repo: https://github.com/akuafif/hXOR-Packer

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[exe-packer]] · [[xorpacker]] · [[x64-exe-packer]] · [[pe-packer]] · [[unpacker]] · [[awesome-executable-packing]]
