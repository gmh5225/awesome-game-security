---
title: Schema
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/mas-bandwidth__schema.md
updated: 2026-11-21
confidence: medium
---

# Schema

**Go-based compiler and data-definition language** (mas-bandwidth) in which you describe constants, enums, types, tables, and network message layouts in `.schema` files and emit matching serializers across many target languages. Its codegen pipeline generates bit-packed packet and table codecs with dedicated runtimes for C, C++, C#, Dart, Elixir, Go, Java, JavaScript, Lobster, Lua, Luau, Python, Ruby, Rust, Squirrel, and related ports, backed by large conformance, fuzz, and hostile-wire regression suites. Ships a cross-language bench harness for read/write profiling, plus editor tooling and examples covering versioning, fixed records, and wire integrity checks. Targets game and realtime networking developers who need fast, deterministic binary formats with strict parsing behavior for client-server protocols and security-sensitive deserialization paths. (source: wiki/sources/descriptions/mas-bandwidth__schema.md)

Sits in the README **Game Network** lane beside the mas-bandwidth C++ client/server stack [[yojimbo]] and cross-language netcode references such as [[ggpo]], [[ggrs]], and [[game-networking-sockets]]. Security-relevant surfaces include strict parse behavior on hostile wire input, fuzz/conformance regression coverage, and schema-versioned record layouts—relevant when hardening protocol deserialization, studying malformed-packet handling, or aligning packet layouts across client and server builds. Distinct from Roblox [[cheeto]]'s separate schema-driven Luau networking compiler.

## Links

- Repo: https://github.com/mas-bandwidth/schema (README: Schema language and compiler generating bit-packed serializers for game packets, saves, and cooked assets across many languages)

## Related

[[yojimbo]] · [[game-networking-sockets]] · [[ggpo]] · [[ggrs]] · [[cheeto]] · [[game-networking-resources]] · [[overviews/game-engine]]