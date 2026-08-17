---
title: pawtrace
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cocomelonc__pawtrace.md
updated: 2026-08-17
confidence: medium
---

# pawtrace

Lightweight **Linux process tracer** built on **ptrace**. Attaches to running processes or spawns new ones, decodes **x86_64 syscalls** with argument inspection, and can trace remotely over a **TCP socket**. Decodes syscall arguments and socket addresses, records **W^X memory** events, snapshots **`/proc/maps`**, and emits **JSONL** output—aimed at reverse engineers and game-security researchers who need scripted syscall forensics on Linux without a full GUI debugger. Implemented in **C + assembly**. (source: wiki/sources/descriptions/cocomelonc__pawtrace.md)

Complements graphical ptrace debuggers such as [[edb-debugger]] and GDB front-ends such as [[pince]], `/proc/pid/mem` scanners such as [[mempeek]], `/proc/maps` parsers such as [[procmap]], ptrace injectors such as [[mandibule]], and sibling cocomelonc tooling such as [[peekaboo]].

## Links

- Repo: https://github.com/cocomelonc/pawtrace

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[edb-debugger]] · [[pince]] · [[mempeek]] · [[procmap]] · [[mandibule]] · [[ptrace-read-teb]] · [[peekaboo]]
