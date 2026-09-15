---
title: Nuitka Themida Unpacker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/DimaReverse__nuitka-themida-unpacker.md
  - wiki/sources/README-categories.md
updated: 2026-09-15
confidence: medium
---

# Nuitka Themida Unpacker

**nuitka-themida-unpacker** (DimaReverse) is a Python two-stage unpacking pipeline for Windows executables that combine Themida or WinLicense protection with Nuitka onefile packaging. Stage one dynamically strips the Themida layer via [[unlicense]]; stage two statically extracts the embedded Nuitka KAX/KAY payload with nuthem (uncompressed or zstd-compressed archives, optional checksum fields, path-traversal-safe extraction, SHA-256 manifests). An optional third stage can chain to companion tools to recover Python artifacts from the inner compiled binary. Targets reverse engineers analyzing doubly protected Nuitka applications—malware samples or hardened game-related tools where no single unpacker handles both layers. (source: wiki/sources/descriptions/DimaReverse__nuitka-themida-unpacker.md)

## Capabilities

- **Themida/WinLicense strip** — dynamic unpack via unlicense integration.
- **Nuitka onefile extract** — KAX/KAY static extraction with compression and checksum handling.
- **Safe file restore** — path-traversal-safe writes with SHA-256 manifests.
- **Optional Python recovery** — third-stage chaining for inner compiled-binary artifacts.

Peers with [[themida-unmutate]], [[magicmida]], [[magicmida-rs]], and [[bobalkkagi]] in the Cheat Fix Themida lane.

## Links

- Repo: https://github.com/DimaReverse/nuitka-themida-unpacker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unlicense]] · [[unpacker]] · [[disrobe]] · [[themida-unmutate]] · [[magicmida]] · [[control-flow-flattening]]
