---
title: CustomDpapi
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/EvilBytecode__CustomDpapi.md
updated: 2026-08-25
confidence: medium
---

# CustomDpapi

**CustomDpapi** (EvilBytecode) is a **C++ proof-of-concept** that calls the **undocumented DPAPI RPC interface** directly, bypassing the standard `CryptUnprotectData` API. It demonstrates invoking **`NdrClientCall3`** with parameters derived from reverse engineering **`dpapi.dll`** internals to perform data decryption through the **lsass `protected_storage` RPC endpoint**. (source: wiki/sources/descriptions/EvilBytecode__CustomDpapi.md)

Primary use case is **authorized security research** on Windows credential protection, DPAPI internals, and RPC-based attack surfaces — complementary to post-dump DPAPI key recovery via [[kvcforensic]] and browser credential harvest tooling such as [[pillager]].

README category: Call undocumented DPAPI RPC interface directly via NdrClientCall3 to lsass protected_storage; no CryptUnprotectData.

## Links

- Repo: https://github.com/EvilBytecode/CustomDpapi

## Related

[[kvcforensic]] · [[pillager]] · [[idontlikefilelocks]] · [[lsass-dump-that-lsass]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
