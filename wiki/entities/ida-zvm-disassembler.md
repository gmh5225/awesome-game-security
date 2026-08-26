---
title: IDA ZVM Disassembler
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Duntss__IDA-ZVM-Disassembler.md
updated: 2026-08-25
confidence: medium
---

# IDA ZVM Disassembler

**IDA Pro processor module and loader** for **Zeus VM (ZVM)** custom bytecode, derived from the OALabs ZVM research lineage. Decodes a 69-instruction virtual ISA inside IDA's native disassembly environment, with **XOR key-chain decryption**, **cross-references for branch targets**, and **auto-comments** describing instruction semantics. (source: wiki/sources/descriptions/Duntss__IDA-ZVM-Disassembler.md)

Targets reverse engineers analyzing malware or protected binaries that embed Zeus VM bytecode—complementary to generic custom-VM analysis plugins such as [[vmattack]] rather than commercial-protector devirtualizers.

## Capabilities

- **Processor module + loader** — lift encrypted ZVM bytecode blobs into IDA-readable disassembly.
- **69-instruction ISA** — full Zeus VM opcode coverage with semantic annotation.
- **XOR key-chain decryption** — recover plaintext bytecode before decode.
- **Branch-target xrefs** — materialize control-flow edges standard analysis may miss on VM dispatch/branch opcodes.

## Links

- Repo: https://github.com/Duntss/IDA-ZVM-Disassembler

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmattack]] · [[ida-evm]] · [[hashdb-ida]] · [[bytecodevm]] · [[binary-shield]] · [[cerberus]] · [[ida-sdk]]
