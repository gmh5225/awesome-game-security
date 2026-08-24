---
title: dnSpy.Extension.HoLLy
kind: entity
topics: [reverse-engineering, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/HoLLy-HaCKeR__dnSpy.Extension.HoLLy.md
updated: 2026-08-24
confidence: medium
---

# dnSpy.Extension.HoLLy

**dnSpy.Extension.HoLLy** is a **C# extension for dnSpyEx** that extends managed-binary RE when obfuscators degrade decompiler output. Capabilities include **source-map-style renaming**, **managed DLL injection during debugging**, **native disassembly support**, **control-flow graph (CFG) visualization**, and utility commands for extension development. Targets reverse engineers, malware analysts, and game modders working with **protected .NET** — including **Unity Mono** clients where renamed or flattened control flow hides intent. Listed in the README under **For Unity**. (source: wiki/sources/descriptions/HoLLy-HaCKeR__dnSpy.Extension.HoLLy.md)

Complements the core [[dnspy]] debugger/decompiler and Unity soft-debugger stack ([[dnspy-unity-mono]], [[mono-debugger-soft]]); pairs with deobfuscation tooling such as [[de4dot]], [[confuserex-idapython]], and [[obfuscation-methods]] when reversing packers on managed game assemblies.

## Links

- Repo: https://github.com/HoLLy-HaCKeR/dnSpy.Extension.HoLLy [For Unity]

## Related

[[dnspy]] · [[dnspy-unity-mono]] · [[mono-debugger-soft]] · [[ilspy]] · [[dncil]] · [[confuserex]] · [[obfuscation-methods]] · [[il2cpp]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
