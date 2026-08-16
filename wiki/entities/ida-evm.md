---
title: ida-evm
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/crytic__ida-evm.md
updated: 2026-08-16
confidence: medium
---

# ida-evm

**ida-evm** is an IDA Pro **processor module** for disassembling Ethereum Virtual Machine (EVM) bytecode. It adds EVM instruction decoding—opcodes such as `PUSH`, `POP`, `SLOAD`, `SSTORE`, `CALL`, and `JUMPI`—with proper operand formatting and cross-reference generation. A Python plugin enables smart-contract bytecode analysis inside IDA's familiar disassembly environment, aimed at blockchain security auditors and smart-contract researchers performing EVM bytecode reverse engineering. (source: wiki/sources/descriptions/crytic__ida-evm.md)

Not a standalone EVM emulator—scoped to IDA processor-module EVM ISA support and on-chain contract bytecode RE.

Complements Binary Ninja EVM tooling such as [[ethersplay]] and other non-x86 IDA architecture plugins such as [[yaravm]] (compiled YARA bytecode) and [[idaxex]] (Xbox 360 XEX).

## Links

- Repo: https://github.com/crytic/ida-evm

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ethersplay]] · [[ida-sdk]] · [[yaravm]] · [[blc]]
