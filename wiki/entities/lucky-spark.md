---
title: Lucky Spark
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Schich__Lucky-Spark.md
updated: 2026-08-21
confidence: medium
---

# Lucky Spark

Windows **shellcode loader** that stages payloads over HTTP/HTTPS with stealth-oriented execution tradecraft comparable to Sliver-style loaders. Uses **fiber-based** scheduling, **JIT decryption**, custom cipher routines, and **WinHTTP** download staging; resolves APIs manually via **PEB walking** instead of static imports. Listed as a stealthy loader for remote shellcode delivery—not an anti-cheat product. (source: wiki/sources/descriptions/Schich__Lucky-Spark.md)

Complements injection-testing samples such as [[jektor]] (CreateFiber + dynamic resolve) and research loaders such as [[nocturneldr]] (PEB-based API resolution) in the shellcode-loader / injection evaluation lane.

## Links

- Repo: https://github.com/Schich/Lucky-Spark

## Related

[[jektor]] · [[nocturneldr]] · [[rs-ldr]] · [[super-mega]] · [[windows-process-injection]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
