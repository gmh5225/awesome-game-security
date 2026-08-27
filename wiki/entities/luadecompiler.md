---
title: LuaDecompiler
kind: entity
topics: [reverse-engineering, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/Coldzer0__LuaDecompiler.md
updated: 2026-08-27
confidence: medium
---

# LuaDecompiler

Pascal **Lua bytecode disassembler and decompiler** covering **Lua 5.1 through 5.5** binary chunks. Uses **SSA-based analysis**, control-flow reconstruction, and boolean expression recovery to lift compiled Lua back toward readable source. Supports **custom opcode tables** for game-modified Lua VMs—common when titles ship patched interpreters or obfuscated script bytecode rather than plain PUC-Rio Lua. (source: wiki/sources/descriptions/Coldzer0__LuaDecompiler.md)

Complements live-script bridges such as [[xlua]], [[luamachine]], and [[vscript-lua51]] when RE must start from dumped `.luac` blobs or in-memory bytecode rather than engine APIs. Pairs with Luau/Lua obfuscators such as [[lua-obfuscator-clyde-protection]] on the protect-vs-recover axis.

## Links

- Repo: https://github.com/Coldzer0/LuaDecompiler

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[xlua]] · [[luamachine]] · [[vscript-lua51]] · [[lua-obfuscator-clyde-protection]] · [[bytecode-viewer]]
