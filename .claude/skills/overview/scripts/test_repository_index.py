"""Functional checks for local discovery; no network, archived code or maintenance jobs."""

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import repository_index as index


class RepositoryIndexTests(unittest.TestCase):
    def test_fences_do_not_create_categories_or_entries(self):
        fence = "\x60" * 4
        text = (
            "## First\n> Source\n- https://github.com/Owner/One\n"
            + fence + "markdown\n## Fake\n- https://github.com/No/Entry\n"
            + "\x60" * 3 + "\n## Also Fake\n"
            + fence + "\n## Second\n- https://github.com/Owner/Two\n"
        )
        sections, entries = index.parse_readme(text)
        self.assertEqual([s["title"] for s in sections], ["First", "Second"])
        self.assertEqual([e["repo"] for e in entries], ["Owner/One", "Owner/Two"])
        self.assertEqual(entries[1]["subsection"], None)
        self.assertEqual(sections[0]["end_line"], sections[1]["line"] - 1)

    def test_deep_link_and_multiple_occurrences_keep_identity(self):
        text = (
            "## Tools\n> Source\n"
            "- [Example](https://github.com/Owner/Repo/blob/abc/file.cc#L2)\n"
            "- https://github.com/owner/repo.git\n"
        )
        _, entries = index.parse_readme(text)
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]["repo"], "Owner/Repo")
        self.assertTrue(entries[0]["url"].endswith("/blob/abc/file.cc#L2"))
        self.assertEqual(entries[1]["repo"], "owner/repo")

    def test_organization_navigation_and_non_github_are_not_repos(self):
        text = (
            "## Tools\n- https://github.com/game-ci\n"
            "- https://github.com/stars/someone/lists/debugger\n"
            "- https://github.com/orgs/example/repositories\n"
            "- https://example.org/Owner/Repo\n"
            "- https://github.com/Owner/Repo\n"
        )
        _, entries = index.parse_readme(text)
        self.assertEqual([e["repo"] for e in entries], ["Owner/Repo"])

    def test_invalid_identity_is_rejected(self):
        for value in ("../repo", "owner/..", "owner/repo/extra",
                      "https://example.org/owner/repo", "stars/someone"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                index.repo_slug(value)

    def test_layers_resolve_independently_and_preserve_actual_case(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            desc = root / "description/Owner/Repo/description_en.txt"
            archive = root / "archive/OWNER/REPO.txt"
            desc.parent.mkdir(parents=True)
            archive.parent.mkdir(parents=True)
            desc.write_text("summary", encoding="utf-8")
            archive.write_text("snapshot", encoding="utf-8")
            result = index.layer_paths(root, "owner/repo")
            self.assertEqual(result["description"]["paths"], ["description/Owner/Repo/description_en.txt"])
            self.assertEqual(result["archive"]["paths"], ["archive/OWNER/REPO.txt"])
            self.assertEqual(index.layer_paths(root, "owner/missing")["archive"]["status"], "missing")

    def test_cli_limit_hash_and_no_checkout_mutation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = b"## Tools\n> Source\n- https://github.com/One/Repo\n- https://github.com/Two/Repo\n"
            (root / "README.md").write_bytes(raw)
            script = Path(index.__file__).resolve()
            run = subprocess.run(
                [sys.executable, str(script), "--root", str(root), "--section", "tools",
                 "--subsection", "source", "--limit", "1"],
                capture_output=True, text=True, check=True,
            )
            report = json.loads(run.stdout)
            self.assertEqual(report["readme_sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(report["total_matches"], 2)
            self.assertTrue(report["truncated"])
            self.assertEqual(len(report["entries"]), 1)
            self.assertEqual(list(root.iterdir()), [root / "README.md"])
            self.assertEqual((root / "README.md").read_bytes(), raw)
            invalid = subprocess.run(
                [sys.executable, str(script), "--root", str(root), "--section", "missing"],
                capture_output=True, text=True,
            )
            self.assertNotEqual(invalid.returncode, 0)
            self.assertIn("Unknown section", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
