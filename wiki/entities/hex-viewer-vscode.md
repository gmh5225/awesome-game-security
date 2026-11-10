---
title: Hex Viewer (VS Code)
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/theluckystrike__hex-viewer-vscode.md
updated: 2026-11-10
confidence: medium
---

# Hex Viewer (VS Code)

Visual Studio Code extension that views and edits raw binary files as hex inside the editor. JavaScript on the standard VS Code extension and webview APIs; **range-based reads** and on-demand row rendering keep **multi-gigabyte** firmware images, memory dumps, and ROMs usable without loading the whole file into RAM. Offline operation with no telemetry. (source: wiki/sources/descriptions/theluckystrike__hex-viewer-vscode.md)

Core workflow features include go-to-offset navigation, hex and text search (with wildcards), a data inspector for integers, floats, GUIDs, and common time formats, copy/export as hex, C arrays, Python `bytes`, or base64, overwrite-mode byte editing with undo, and quick PE, ELF, PNG, and ZIP recognition from headers.

Complements standalone workbenches such as [[imhex]] and [[hexwalk]], Ghidra plugins such as [[ghidra-hexeditor]], and IDE-native mobile tooling such as [[vscode-frida]]—aimed at reverse engineers, malware analysts, and game-security practitioners who want dump triage in the same editor as scripts and docs.

## Links

- Repo: https://github.com/theluckystrike/hex-viewer-vscode

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[imhex]] · [[hexwalk]] · [[ghidra-hexeditor]] · [[vscode-frida]] · [[totalpe2]] · [[binary-evidence]]
