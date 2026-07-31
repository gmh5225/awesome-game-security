---
title: ghidra-svr-bridge
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mutinylaboratories__ghidra_svr_bridge.md
updated: 2026-07-31
confidence: medium
---

# ghidra-svr-bridge

Binary Ninja plugin that connects to a Ghidra Server repository and bidirectionally synchronizes reverse-engineering analysis between Binary Ninja and Ghidra on the same binary. A C++/Qt6 sidebar plugin talks to a Java 17 bridge subprocess over local TCP JSON; the bridge holds the Ghidra Server RMI connection. Sync covers symbols, function names, comments, signatures, parameters, data types, equates, bookmarks, and typed data items so teams can import Ghidra project work into Binary Ninja or push changes back without manual copy-paste. Writes go through Ghidra’s high-level program-model APIs to avoid database corruption. Aimed at reverse engineers and game security researchers combining Binary Ninja’s workflow with collaborative Ghidra Server repositories. (source: wiki/sources/descriptions/mutinylaboratories__ghidra_svr_bridge.md)

Not a standalone disassembler—scoped to BN↔Ghidra Server collaborative analysis sync (Cheat Binary Ninja Plugins lane).

## Links

- Repo: https://github.com/mutinylaboratories/ghidra_svr_bridge

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[binaryninja-pcode]] · [[ghidra-headless-mcp]] · [[symbridge]] · [[x64dbgbinja]]
