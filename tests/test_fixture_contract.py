import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FixtureContractTests(unittest.TestCase):
    def test_fixture_manifest_and_records_are_readable(self):
        manifest = json.loads((ROOT / "fixtures" / "manifest.json").read_text(encoding="utf-8"))
        primary = json.loads((ROOT / "fixtures" / "primary.json").read_text(encoding="utf-8"))
        revision = json.loads((ROOT / "fixtures" / "revision.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["format"], 1)
        self.assertTrue(manifest["synthetic"])
        self.assertEqual(manifest["fixture"], "orthogonal_mix")
        self.assertEqual(len(manifest["records"]), 2)
        self.assertIsInstance(primary, dict)
        self.assertIsInstance(revision, dict)
        self.assertEqual(revision["revision"], "synthetic-revision-2")
        self.assertIn("numpy", __import__("tomllib").loads((ROOT / "pyproject.toml").read_text())["project"]["dependencies"][0])
