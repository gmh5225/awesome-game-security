---
title: Plugin Lens
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/AlonSoko__ida-plugin-lens.md
  - wiki/sources/README-categories.md
updated: 2026-10-10
confidence: medium
---

# Plugin Lens

**Plugin Lens** (AlonSoko) is a Python **IDA Pro** GUI plugin (**IDA 9.0+**) that reorganizes **Edit › Plugins** for reverse engineers, malware analysts, and game-security researchers who rely on large **hcli** and **ida-plugin.json** plugin stacks.

## Capabilities

- **Icons:** from each plugin’s `ida-plugin.json` logo, bundled artwork for built-in entries, or custom images in the user `plugin-lens` folder—without overwriting icons a plugin already sets.
- **Grouping:** built-in plugins, hcli-installed plugins (by repository), and manually installed plugins.
- **Version visibility:** superscript version numbers and tags when hcli reports newer releases.
- **Updates:** a menu action runs hcli’s upgrade flow inside IDA for selected plugins.

(source: wiki/sources/descriptions/AlonSoko__ida-plugin-lens.md)

Workflow infrastructure—not decompilation or automation. Complements [[ida-settings]] configuration management and [[ida-plugin-repository]] manifest discovery.

## Links

- Repo: https://github.com/AlonSoko/ida-plugin-lens (Cheat / RE Tools)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-settings]] · [[ida-plugin-repository]] · [[karta-x-configs]] · [[list-of-ida-plugins]]
