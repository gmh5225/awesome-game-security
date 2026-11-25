"""Check that update-wiki-cli.py tracks every skill folder under .claude/skills/."""

from __future__ import annotations

import importlib.util
import sys
import types
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_update_wiki():
    if str(SCRIPTS_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPTS_DIR))

    stub = types.ModuleType("cursor_sdk_agent")
    stub.DEFAULT_MODEL = "stub"
    stub.get_api_key = lambda: ""
    stub.run_agent = lambda *args, **kwargs: 0

    prev = sys.modules.get("cursor_sdk_agent")
    sys.modules["cursor_sdk_agent"] = stub
    try:
        spec = importlib.util.spec_from_file_location(
            "update_wiki_cli", SCRIPTS_DIR / "update-wiki-cli.py"
        )
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        if prev is None:
            sys.modules.pop("cursor_sdk_agent", None)
        else:
            sys.modules["cursor_sdk_agent"] = prev


class UpdateWikiSkillTopicsTests(unittest.TestCase):
    def test_skill_topics_cover_all_skill_directories(self):
        mod = _load_update_wiki()
        skill_dirs = sorted(
            p.parent.name for p in (ROOT_DIR / ".claude" / "skills").glob("*/SKILL.md")
        )
        self.assertGreater(len(skill_dirs), 0)
        missing = sorted(set(skill_dirs) - set(mod.SKILL_TOPICS))
        self.assertEqual(missing, [])
        self.assertEqual(mod.parse_topics(",".join(skill_dirs)), skill_dirs)


if __name__ == "__main__":
    unittest.main()
