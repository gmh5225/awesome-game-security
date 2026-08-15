---
title: BE Shellcode Tester
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/es3n1n__be-shellcode-tester.md
updated: 2026-08-15
confidence: medium
---

# BE Shellcode Tester

C++ testing environment (es3n1n) for executing and analyzing [[battleye]] **shellcode scanning modules** in a controlled sandbox. Loads dumped BE scanning payloads, emulates the expected runtime environment, and logs behavior including memory scans, hash checks, and detection routines—helping researchers map BE detection coverage without a live protected game. (source: wiki/sources/descriptions/es3n1n__be-shellcode-tester.md)

Complements dump/capture tools [[be-shellcode-dump]] and [[battleye-shellcode-dumper]] (offline module acquisition) and study scaffolds such as [[be-battleye-shellcode]] / [[be-shellcode]] by focusing on **sandbox execution and trace logging** of already-dumped BE shellcode.

## Links

- Repo: https://github.com/es3n1n/be-shellcode-tester

## Related

[[battleye]] · [[be-shellcode-dump]] · [[battleye-shellcode-dumper]] · [[be-battleye-shellcode]] · [[be-shellcode]] · [[battleye-region-walking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
