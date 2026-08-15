---
title: phantom-client
kind: entity
topics: [game-hacking, anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/inpeacedTeams__phantom-client.md
updated: 2026-08-10
confidence: medium
---

# phantom-client

Windows injectable **internal DLL** cheat for **Lunar Client** Minecraft **1.8.9** that attaches to the running JVM and manipulates the game from native C++20 code. Uses **JNI** and **JVMTI** to resolve obfuscated Minecraft classes and fields, hooks **`wglSwapBuffers`** with **MinHook** for a **Dear ImGui** overlay, and organizes combat, movement, and visual modules (kill aura, velocity, fly, speed, ESP, backtrack) in a header-only architecture. Evasion-oriented design includes a dedicated click scheduler for human-like CPS timing, keybind-based input simulation, and server-specific profiles tuned for different anti-cheat environments. Primarily useful for game security research into Minecraft client injection, JNI hooking, obfuscated class discovery, and anti-cheat bypass techniques. (source: wiki/sources/descriptions/inpeacedTeams__phantom-client.md)

## Architecture

- **JVM attach** — JNI/JVMTI from native code into obfuscated 1.8.9 client classes.
- **Render hook** — OpenGL `wglSwapBuffers` + MinHook → ImGui overlay.
- **Modules** — header-only combat/movement/visual feature set with evasion helpers.

Complements server-side Java AC such as [[avaanticheat]] and [[minecraft-anticheatai]], passive client-side Forge monitors such as [[local-anticheat-1-8-9]], Bedrock proxy [[oomph]], server backend [[minecpp]], and Fabric mod-loader clients such as [[lenrete-mod]] in the Minecraft game-security lane.

## Links

- Repo: https://github.com/inpeacedTeams/phantom-client

## Related

[[minecpp]] · [[minecraft-anticheatai]] · [[avaanticheat]] · [[local-anticheat-1-8-9]] · [[oomph]] · [[lenrete-mod]] · [[present-hook]] · [[ntminhook]] · [[imgui]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/graphics-api]]
