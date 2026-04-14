---
name: awesome-game-security-overview
description: Guide for understanding and contributing to the awesome-game-security curated resource list. Use this skill when adding new resources, organizing categories, mapping topics across anti-cheat, Windows kernel, DMA, reverse engineering, and game-engine research, or maintaining README.md format consistency.
---

# Awesome Game Security - Project Overview

## Purpose

This is a curated collection of resources related to game security, covering both offensive (game hacking, cheating) and defensive (anti-cheat) aspects. The project serves as a comprehensive reference for security researchers, game developers, and enthusiasts, especially where Windows internals, driver trust, reverse engineering, DMA, and modern anti-cheat defenses intersect.

## README Coverage

- Top-level engines and rendering: `Game Engine`, `Renderer`, `DirectX`, `OpenGL`, `Vulkan`
- Offensive research: `Cheat`
- Defensive research: `Anti Cheat`
- Platform hardening: `Windows Security Features`
- Platform-specific ecosystems: `Android Emulator`, `IOS Emulator`, `Windows Emulator`, `Linux Emulator`
- Supporting infrastructure: `Mathematics`, `3D Graphics`, `AI`, `Image Codec`, `Wavefront Obj`, `Task Scheduler`, `Game Network`, `PhysX SDK`, `Game Develop`, `Game Assets`, `Game Hot Patch`, `Game Testing`, `Game Tools`, `Game Manager`, `Game CI`
- Platform subsystems: `WSL`, `WSA`
- Console emulation: `Game Boy`, `Nintendo Switch`, `Xbox`, `PlayStation`
- Tips and tricks: `Some Tricks`

## Project Structure

```
awesome-game-security/
├── README.md           # Main resource list
├── LICENSE             # MIT License
├── awesome-image.webp  # Project banner
└── scripts/
    ├── generate-toc.py  # Generate table of contents
    └── remove-forks.py  # Clean up forked repos
```

## README.md Format Convention

### Category Structure

Each category follows this format:

```markdown
## Category Name
> Subcategory (optional)
- https://github.com/user/repo [Brief description]
- https://github.com/user/repo [Another description]
```

### Link Format

- Always use full GitHub URLs for repositories
- Non-GitHub links are also supported (blog posts, articles, documentation sites)
- Add brief descriptions in square brackets `[description]`
- Use consistent spacing and formatting
- Group related resources under subcategories with `>`

### Example Entry

```markdown
## Game Engine
> Guide
- https://github.com/example/guide [Comprehensive game dev guide]

> Source
- https://github.com/example/engine [Open source game engine]
```

## Skill Routing Guide

When an AI agent receives a query, use this table to select the best skill:

| Query topic | Primary skill | Related skills |
|---|---|---|
| EAC, BattlEye, Vanguard, detection, heartbeat, screenshot | anti-cheat | windows-kernel |
| pcileech, FPGA, DMA, IOMMU, Thunderbolt | dma-attack | anti-cheat |
| Unreal SDK, Unity IL2CPP, engine structs, Godot, Lumix | game-engine | game-hacking |
| Memory hacking, injection, overlays, driver comm, HWID spoof | game-hacking | graphics-api |
| D3D/Vulkan/OpenGL hooks, Present hook, shader interception | graphics-api | game-hacking |
| Android root, Frida, iOS jailbreak, KernelSU, APatch | mobile-security | game-hacking |
| IDA, Ghidra, DBI, deobfuscation, binary diffing, MCP RE tools, trap-and-emulate CFT, WHP tracing | reverse-engineering | anti-cheat, windows-kernel |
| Drivers, callbacks, PatchGuard, HVCI, ETW, pool forensics, WHP API | windows-kernel | anti-cheat, reverse-engineering |
| Adding resources, README format, link validation | overview | (any) |

## Main Categories

All 27 top-level `##` sections in README.md:

1. **Game Engine**: Engines, source code, plugins (Unreal/Unity/Godot/Lumix), detectors
2. **Mathematics**: Linear algebra, physics libraries
3. **Renderer**: Software renderers, ray tracing
4. **3D Graphics**: 3D modeling and graphics resources
5. **AI**: Machine learning for games
6. **Image Codec**: Image processing libraries
7. **Wavefront Obj**: OBJ file parsers
8. **Task Scheduler**: Job/task scheduling systems
9. **Game Network**: Networking, KCP, JWT, geolocation
10. **PhysX SDK**: NVIDIA PhysX resources
11. **Game Develop**: Development guides, source code, MCP servers, AI agents
12. **Game Assets / Hot Patch / Testing / Tools / Manager / CI**: Supporting infrastructure
13. **DirectX**: Guides, hooks, tools, emulation, overlays
14. **OpenGL**: Guides, source, hooks
15. **Vulkan**: API, guides, hooks
16. **Cheat**: Offensive research (debugging, injection, hooking, DMA, overlays, driver comm, EFI, anti-forensics, game-specific)
17. **Anti Cheat**: Defensive research (protection, detection, callbacks, forensics, signature scanning)
18. **Some Tricks**: Ring0/Ring3/Linux/Android tricks and techniques
19. **Windows Security Features**: DSE, PatchGuard, VBS, HVCI, Secure Boot
20. **WSL / WSA**: Windows Subsystem for Linux/Android
21. **Windows / Linux / Android / IOS Emulator**: Platform emulators
22. **Game Boy / Nintendo Switch / Xbox / PlayStation**: Console emulators and research

## Contributing Guidelines

1. **Check for duplicates** before adding new resources
2. **Verify links** are working and point to original repos
3. **Add descriptions** that clearly explain the resource's purpose
4. **Place in correct category** based on primary functionality
5. **Follow existing format** for consistency

## Quality Criteria

- Resource should be actively maintained or historically significant
- Should provide unique value not covered by existing entries
- Prefer original repos over forks unless fork adds significant value
- Include language/platform tags when helpful (e.g., `[Rust]`, `[Unity]`)

## Scripts Usage

### Generate Table of Contents
```bash
python scripts/generate-toc.py
```

### Remove Fork References
```bash
python scripts/remove-forks.py
```

---

## Data Source

**Important**: This skill provides conceptual guidance and overview information. For detailed information use the following sources:

### 1. Project Overview & Resource Index

Fetch the main README for the full curated list of repositories, tools, and descriptions:

```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md
```

The main README contains thousands of curated links organized by category. When users ask for specific tools, projects, or implementations, retrieve and reference the appropriate sections from this source.

### 2. Repository Code Details (Archive)

For detailed repository information (file structure, source code, implementation details), the project maintains a local archive. If a repository has been archived, **always prefer fetching from the archive** over cloning or browsing GitHub directly.

**Archive URL format:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/{owner}/{repo}.txt
```

**Examples:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/ufrisk/pcileech.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/000-aki-000/GameDebugMenu.txt
```

**How to use:**
1. Identify the GitHub repository the user is asking about (owner and repo name from the URL).
2. Construct the archive URL: replace `{owner}` with the GitHub username/org and `{repo}` with the repository name (no `.git` suffix).
3. Fetch the archive file — it contains a full code snapshot with file trees and source code generated by `code2prompt`.
4. If the fetch returns a 404, the repository has not been archived yet; fall back to the README or direct GitHub browsing.

### 3. Repository Descriptions

For a concise English summary of what a repository does, the project maintains auto-generated description files.

**Description URL format:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/{owner}/{repo}/description_en.txt
```

**Examples:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/00christian00/UnityDecompiled/description_en.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/ufrisk/pcileech/description_en.txt
```

**How to use:**
1. Identify the GitHub repository the user is asking about (owner and repo name from the URL).
2. Construct the description URL: replace `{owner}` with the GitHub username/org and `{repo}` with the repository name.
3. Fetch the description file — it contains a short, human-readable summary of the repository's purpose and contents.
4. If the fetch returns a 404, the description has not been generated yet; fall back to the README entry or the archive.

**Priority order when answering questions about a specific repository:**
1. Description (quick summary) — fetch first for concise context
2. Archive (full code snapshot) — fetch when deeper implementation details are needed
3. README entry — fallback when neither description nor archive is available
