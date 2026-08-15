---
title: ida-genpatch
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/frasten__ida-genpatch.md
updated: 2026-08-15
confidence: medium
---

# ida-genpatch

IDA PatchGen is an IDAPython plugin that exports byte-level edits made during interactive patching into reusable patch code. Triggered with Alt-F8, it scans the database for patched bytes, groups contiguous changes, and prints file offsets with original and modified values. For each patch group it also shows disassembly of the affected instructions and emits C# `SinglePatchHunk` statements for custom binary patchers. (source: wiki/sources/descriptions/frasten__ida-genpatch.md)

Scoped as IDA-side patch export—not live process patching or a standalone patcher runtime. Complements [[genpatch]] (Python patch-script generator) and [[ida2obj]] (COFF/ELF object export) when the workflow is interactive IDA byte edits → external patch logic.

## Links

- Repo: https://github.com/frasten/ida-genpatch

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[genpatch]] · [[ida2obj]] · [[happyida]] · [[genmc]]
