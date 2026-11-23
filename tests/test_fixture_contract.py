"""检查采集资料的身份、形状和可交叉引用性。"""

import json
from pathlib import Path
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def read_fixture(name):
    return json.loads((ROOT / "fixtures" / name).read_text(encoding="utf-8"))


class FixtureContractTests(unittest.TestCase):
    def test_record_manifest(self):
        manifest = read_fixture("manifest.json")
        primary = read_fixture("primary.json")
        revision = read_fixture("revision.json")
        self.assertEqual(manifest["fixture"], "orthogonal_mix")
        self.assertEqual(manifest["records"], ["primary.json", "revision.json"])
        self.assertTrue(manifest["synthetic"])
        self.assertEqual(revision["replaces"], primary["capture"])
        self.assertNotEqual(revision["capture"], primary["capture"])

    def test_related_input_records(self):
        primary = read_fixture("primary.json")
        revision = read_fixture("revision.json")
        by_name = {factor["id"]: factor for factor in primary["factors"]}
        width = len(primary["input"][0])
        for factor in primary["factors"] + revision["factor_updates"]:
            self.assertEqual(len(factor["vector"]), width)
            self.assertGreater(np.linalg.norm(factor["vector"]), 0)
            self.assertIn(factor["id"], by_name)
        for head in primary["heads"]:
            self.assertTrue(set(head["channels"]).isdisjoint(head["side"]))
            self.assertTrue(all(0 <= i < width for i in head["channels"] + head["side"]))
        self.assertTrue(any(None in values for values in primary["input"]))
