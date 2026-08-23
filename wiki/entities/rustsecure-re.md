---
title: rustsecure-re
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Leeksov__rustsecure-re.md
updated: 2026-08-23
confidence: medium
---

# rustsecure-re

Static reverse-engineering documentation of **RustSecure**, a client-side anti-cheat agent used with Facepunch **Rust**. Maps the loader, encrypted payload delivery, native CLR bridge, and Core DLL architecture, including thirteen detection modules covering anti-debug, anti-VM, direct NT syscalls, HWID collection, BepInEx and [[kdmapper]] detection, screenshot capture, and WebSocket telemetry. Includes Python and C# tooling for string decryption, deobfuscation, and payload analysis, plus detailed bypass write-ups and optional static and runtime patch utilities for disabling detections during research. Work is performed entirely through static analysis with tools such as ILSpy, dnfile, and IDA Pro rather than executing the original binaries. Intended for game security researchers studying anti-cheat design, client-side protection mechanisms, and enforcement techniques. (source: wiki/sources/descriptions/Leeksov__rustsecure-re.md)

Complements offensive Rust cheat samples such as [[lord-abbot-rust-external-cheat]] and [[rust-rustinternal]] with a defensive client-agent architecture map for the same [[easy-anti-cheat]]-protected title.

## Links

- Repo: https://github.com/Leeksov/rustsecure-re

## Related

[[easy-anti-cheat]] · [[kdmapper]] · [[bepinex-il2cppbase]] · [[il2cpp]] · [[al-khaser]] · [[lord-abbot-rust-external-cheat]] · [[rust-rustinternal]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
