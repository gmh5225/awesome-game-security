---
title: PePacker (SamLarenN)
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/SamLarenN__PePacker.md
updated: 2026-08-21
confidence: medium
---

# PePacker (SamLarenN)

Simple C++ PE packer that encrypts the `.text` section of Windows executables and appends a decryption stub. Implements custom PE parsing components for exploring and rewriting sections. Default protection uses XOR encryption as a lightweight demonstration replaceable with stronger algorithms. Mainly useful for reverse-engineering practice, packer development learning, and basic obfuscation research in game security contexts. (source: wiki/sources/descriptions/SamLarenN__PePacker.md)

Useful as an educational minimal PE packer reference alongside [[pe-packer]], [[exe-packer]], and [[xorpacker]]—not a full protector or unpacker.

## Links

- Repo: https://github.com/SamLarenN/PePacker

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[pe-packer]] · [[exe-packer]] · [[xorpacker]] · [[packer-tutorial]] · [[pepacker]] · [[unpacker]]
