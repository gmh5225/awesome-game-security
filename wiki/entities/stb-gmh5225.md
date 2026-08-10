---
title: STB
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__STB.md
updated: 2026-08-10
confidence: medium
---

# STB

**STB** (gmh5225/STB) is a **compile-time conversion library** that turns **IDA-style string literals into byte arrays** at build time — a helper for researchers embedding string or shellcode blobs without leaving plaintext in `.rdata`. The curated description also frames it in the **stack trace building / call-stack spoofing** lane: manipulating return addresses or constructing synthetic frames to evade thread stack walks used by anti-cheat and EDR. (source: wiki/sources/descriptions/gmh5225__STB.md)

Listed under README `Cheat > Compile Time` beside other constexpr obfuscation helpers; complements gmh5225 stack-spoof tooling such as [[spoof-stack-safecall]] and [[stack-spoofer-macro]] in the broader `Cheat > Spoof Stack` research corpus. Distinct from [[stb]] (nothings/stb single-header image/font/audio utilities).

## Links

- Repo: https://github.com/gmh5225/STB

## Related

[[stack-spoofing]] · [[spoof-stack-safecall]] · [[stack-spoofer-macro]] · [[return-address-spoofer]] · [[thread-stack-spoofer]] · [[silent-moonwalk]] · [[skcrypter]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
