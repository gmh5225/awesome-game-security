---
title: IDA Better Information
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/FPSZ__ida-better-information.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: high
---

# IDA Better Information

**IDA Better Information** (FPSZ/ida-better-information) is a single-file **IDA Pro** plugin and standalone Python CLI that automatically recovers libc or compiler runtime context from binaries before manual analysis. It detects glibc, musl, Go, and MSVC runtime versions—including stripped, statically linked Linux targets—via embedded byte fingerprints and can apply matching FLIRT signatures to restore library function names. The tool adds libc purpose comments at call sites and Hex-Rays decompiler notes that interpret real arguments and the plain-math meaning of MMX and SSE intrinsics, with bilingual UI, one-click undo, and fully offline operation. Aimed at reverse engineers and CTF analysts who need faster orientation on obfuscated or stripped game and native binaries in IDA. (source: wiki/sources/descriptions/FPSZ__ida-better-information.md)

## Catalog lane

Cheat / IDA Plugins — pre-analysis runtime context and FLIRT-assisted naming (not LLM renaming). (source: wiki/sources/descriptions/FPSZ__ida-better-information.md)

## Mechanism

1. **Fingerprint** embedded libc/compiler runtime bytes (glibc, musl, Go, MSVC) on stripped or static Linux/Windows targets.
2. **Optional FLIRT** — apply matching signature libraries to recover library function names.
3. **Annotate** — libc role comments at call sites; Hex-Rays notes for MMX/SSE intrinsics as plain math/arguments.
4. **Revert** — one-click undo; no network dependency.

## Evidence model

- **Runtime fingerprinting** — glibc/musl/Go/MSVC identification before deep manual RE.
- **FLIRT-assisted naming** — library symbol recovery on stripped/static Linux builds.
- **Decompiler annotations** — MMX/SSE math intent at call sites; undoable, offline.

## Positioning

Sits in the Cheat / IDA Plugins lane beside triage plugins such as [[ida-plugin-lens]] and LLM assistants such as [[binarylens]]—deterministic runtime context rather than speculative renaming. Complements library-ID tools [[idenlib]] (stripped PE VC++/STL) and [[sig-database]] (Linux FLIRT packs) by auto-detecting runtime flavor before manual signature work.

## Peers

[[ida-plugin-lens]] · [[idenlib]] · [[sig-database]] · [[binarylens]] · [[ida-pro-agent]] · [[dereferencing]]

## Links

- Repo: https://github.com/FPSZ/ida-better-information
