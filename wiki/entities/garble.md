---
title: garble
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/burrowers__garble.md
updated: 2026-08-17
confidence: medium
---

# garble

**Go build-time obfuscator** that wraps the Go toolchain so you can build, test, and run programs with as little recoverable source information left in the binary as possible. Replaces identifiers, package paths, and position data with short hashes; strips build, module, and debug metadata; and optionally obfuscates string and other literals. Offers a **tiny** mode that further shrinks binaries by removing panic and debug runtime details, plus experimental control-flow obfuscation, while remaining deterministic and integrated with `cmd/go` modules and build caching. A **`garble reverse`** command maps obfuscated stack traces back to original names when source is available. Aimed at developers who need to discourage reverse engineering of distributed Go binaries or private libraries—including software protection and anti-analysis use cases. (source: wiki/sources/descriptions/burrowers__garble.md)

Broader than compile-time Go string crypters such as [[obfuscatxor]]; complements Rust source-level obfuscators such as [[rust-obfuscator]] and curated obfuscation indexes such as [[awesome-obfuscations]].

## Links

- Repo: https://github.com/burrowers/garble

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[obfuscatxor]] · [[rust-obfuscator]] · [[control-flow-flattening]] · [[awesome-obfuscations]]
