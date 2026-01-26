---
name: awesome-game-security-overview
description: Guide for understanding and contributing to the awesome-game-security curated resource list. Use this skill when adding new resources, organizing categories, understanding project structure, or maintaining the README.md format consistency.
---

# Awesome Game Security - Project Overview

## Purpose

This is a curated collection of resources related to game security, covering both offensive (game hacking, cheating) and defensive (anti-cheat) aspects. The project serves as a comprehensive reference for security researchers, game developers, and enthusiasts.

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

- Always use full GitHub URLs
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

## Main Categories

1. **Game Development**: Engines, renderers, networking, physics
2. **Graphics APIs**: DirectX, OpenGL, Vulkan hooks and tools
3. **Cheat/Hacking**: Memory manipulation, injection, bypasses
4. **Anti-Cheat**: Protection systems, detection methods
5. **Reverse Engineering**: Debuggers, disassemblers, analysis tools
6. **Windows Kernel**: Drivers, callbacks, security features
7. **Web3 Security**: Blockchain, smart contracts, DeFi
8. **Emulators**: Windows, Linux, Android, iOS, consoles

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

**Important**: This skill provides conceptual guidance and overview information. For detailed information including:
- Specific GitHub repository links
- Complete project lists with descriptions
- Up-to-date tools and resources
- Code examples and implementations

**Please fetch the complete data from the main repository:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md
```

The main README contains thousands of curated links organized by category. When users ask for specific tools, projects, or implementations, retrieve and reference the appropriate sections from this source.
