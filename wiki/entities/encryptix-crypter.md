---
title: Encryptix Crypter
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Ezmatehw__Encryptix-Crypter.md
updated: 2026-08-25
confidence: medium
---

# Encryptix Crypter

**Ezmatehw** Windows **GUI crypter and packer** that encrypts **PE payloads** and rebuilds them into standalone executables using a **configurable stub template**. Written in **C#** for **.NET Framework 4.8** with WinForms and Guna UI, it supports **AES** and **XOR** encryption, **runtime process injection** via RegAsm, RegSvcs, MSBuild, and related **LOLBins**, plus optional **persistence**, **anti-VM** checks, **sleep delays**, and **assembly metadata cloning**. The project includes a **dnlib-based obfuscator** with randomization and booster modules, **KeyAuth** license gating, and a builder that embeds encrypted resources and **compiles the stub at build time**. Aimed at game security researchers, reverse engineers, and anti-cheat analysts studying crypter construction, payload packing, and evasion techniques. Listed under Anti Cheat → Binary Packer (open-source .NET/native PE crypter with AES256, startup/injection options, and AntiVM/AntiCRACK features). (source: wiki/sources/descriptions/Ezmatehw__Encryptix-Crypter.md)

Useful as an educational .NET PE crypter reference alongside [[netcrypt]], [[evader]], and [[polyengine]]—not a full commercial protector or unpacker.

## Links

- Repo: https://github.com/Ezmatehw/Encryptix-Crypter

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[netcrypt]] · [[evader]] · [[polyengine]] · [[pe-packer]] · [[hm-pe-packer]] · [[packer-tutorial]] · [[windows-process-injection]] · [[unpacker]]
