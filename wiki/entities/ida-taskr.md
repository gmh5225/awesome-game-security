---
title: IDA Taskr
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mahmoudimus__ida-taskr.md
updated: 2026-07-31
confidence: medium
---

# IDA Taskr

Pure Python library for IDA Pro–related parallel computing. Combines Qt (built into IDA) with Python `multiprocessing` to offload CPU-heavy IDAPython work to worker processes without freezing the IDA UI. Aimed at game-security researchers and reverse engineers in the cheat / IDA Plugins lane. (source: wiki/sources/descriptions/mahmoudimus__ida-taskr.md)

Not a disassembler or analysis plugin itself—a concurrency helper for long-running IDA-side batch jobs (scans, xref walks, decompilation batches).

## Links

- Repo: https://github.com/mahmoudimus/ida-taskr

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[sark]] · [[idac]] · [[ida-pro-mcp]] · [[ripr]] · [[xrefsext]]
