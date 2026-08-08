---
title: JS Debugger Bypass UserScript
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__js-debugger-bypass-script.md
updated: 2026-08-08
confidence: medium
---

# JS Debugger Bypass UserScript

JavaScript UserScript collection that bypasses browser-based debugger detection so researchers can analyze JavaScript-heavy web applications with DevTools open. It neutralizes common anti-debugging measures including `debugger` statements, DevTools-open detection, `console.log` timing checks, and window-size monitoring that sites use to detect when developer tools are active. (source: wiki/sources/descriptions/gmh5225__js-debugger-bypass-script.md)

Aimed at web security researchers and reverse engineers studying client-side protections — the offensive counterpart to obfuscators such as [[javascript-obfuscator]] that embed debug-protection helpers. Listed under README `[JS Debugger Bypass UserScript]`.

## Links

- Repo: https://github.com/gmh5225/js-debugger-bypass-script

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[javascript-obfuscator]] · [[gh-anti-debug-bypass-practice-tool]] · [[steam-anti-anti-debug]]
