---
title: shellcode-plain-sight
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/LloydLabs__shellcode-plain-sight.md
updated: 2026-08-23
confidence: medium
---

# shellcode-plain-sight

C demonstration of **hiding shellcode inside a large randomized memory region** before execution. Allocates oversized read-write memory, fills it with random bytes, places payload data at a random offset, then flips protection to executable. Includes cleanup logic to zero memory before freeing so post-runtime artifacts are reduced. Primary use case: evasion research and testing memory-analysis or anti-cheat detection strategies against concealed payload placement. (source: wiki/sources/descriptions/LloydLabs__shellcode-plain-sight.md)

Complements in-memory page-protection evasion such as [[shellcode-fluctuation]] (RW↔RX fluctuation), entropy reduction via [[shellcode-entropyfix]], and defensive shellcode discovery such as [[cfg-find-hidden-shellcode]] and [[rwxfinder]].

## Links

- Repo: https://github.com/LloydLabs/shellcode-plain-sight (README: Hiding shellcode in plain sight within a large memory region)

## Related

[[shellcode-fluctuation]] · [[shellcode-entropyfix]] · [[scfw]] · [[cfg-find-hidden-shellcode]] · [[rwxfinder]] · [[wsb-detect]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
