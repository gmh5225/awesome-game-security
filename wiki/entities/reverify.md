---
title: reverify
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/2akouwu__reverify.md
  - wiki/sources/README-categories.md
updated: 2026-09-05
confidence: medium
---

# reverify

**reverify** (2akouwu/reverify) is a **Python toolkit** that grounds AI-assisted reverse engineering by checking language-model claims about binaries against the actual bytes instead of trusting model output alone. It targets authorized RE workflows—malware analysis, CTF work, and interoperability research—where AI reconstructions must be validated against real binary data. (source: wiki/sources/descriptions/2akouwu__reverify.md)

## Capabilities

- **Binary parsing:** PE, ELF, and Mach-O via pure-Python core with **LIEF** backend extensions
- **Analysis primitives:** disassembly (**Capstone**), CPU emulation (**Unicorn**), pattern scanning, protocol parsing, **Frida** hook generation
- **Claim verifier:** deterministic checks return **VERIFIED**, **REFUTED**, or **INCONCLUSIVE** with observed evidence
- **Reconstruction agent:** closed feedback loop where a model proposes checkable hypotheses, the verifier refutes hallucinations, and an **established-facts ledger** carries forward only tool-grounded results; optional behavioral-equivalence checks via Unicorn emulation
- **Agent bridge:** **MCP server** plus CLI expose the toolkit to coding agents

Complements MCP RE hosts such as [[ida-pro-mcp]] and LLM rename/explain plugins such as [[binarylens]] by adding a byte-level verification gate—similar in spirit to read-only harnesses like [[re-harness]] and file-export bridges like [[ida-no-mcp]] that anchor agent output to tool evidence rather than model speculation.

## Role in the README map

Listed under **Cheat → RE Tools** beside agent-native labs such as [[open-reverselab]] and cross-platform pipelines such as [[n0xis]]. Emphasizes verification gates over unconstrained model output.

## Links

- Repo: https://github.com/2akouwu/reverify

## Related

[[research-rigor]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[open-reverselab]] · [[n0xis]] · [[ida-pro-mcp]] · [[binarylens]] · [[re-harness]] · [[ida-no-mcp]] · [[frida]]
