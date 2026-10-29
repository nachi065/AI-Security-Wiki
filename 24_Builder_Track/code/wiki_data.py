"""Offline look-ups over the wiki's CSV data files: controls, risks, the risk to
control mapping and test cases. The CSVs are rebuilt from the wiki pages on
every build, so these answers match the pages; the pages stay authoritative.

Standard library only; works on Linux, macOS and Windows.

    python wiki_data.py control AI-CTRL-024
    python wiki_data.py risk AI-R23
    python wiki_data.py test TC-L06-008
    python wiki_data.py search "kill switch"
    options: --data DIR (default: the wiki's 25_Templates/data folder, or $AIWIKI_DATA) --json
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from functools import cached_property
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_DATA = HERE.parent.parent / "25_Templates" / "data"
SITE = "https://nachi065.github.io/AI-Security-Wiki/"
CONTROL_PAGE = "03_Control_Library/03_AI_Security_Control_Objectives_Library.html"
RISK_PAGE = "02_Risk_Management/02B_Enterprise_AI_Risk_Register.html"
TEST_DIR = "10_Test_Case_Library/"
ID = re.compile(r"\b(AI-CTRL-\d{3}|AI-R\d{2,3}|TC-[A-Z]\d{2}-\d{3})\b")


def _ids(text: str) -> list[str]:
    return ID.findall(text or "")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


class WikiData:
    def __init__(self, data_dir: str | os.PathLike | None = None):
        self.dir = Path(data_dir or os.environ.get("AIWIKI_DATA") or DEFAULT_DATA)
        if not (self.dir / "controls.csv").is_file():
            raise FileNotFoundError(f"wiki CSV files not found in {self.dir}; download them from "
                                    f"{SITE}25_Templates/ and pass --data")

    def _read(self, name: str) -> list[dict]:
        with open(self.dir / name, newline="", encoding="utf-8") as f:
            return [{k: (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f)]

    @cached_property
    def controls(self) -> dict[str, dict]:
        return {r["Control ID"]: r for r in self._read("controls.csv")}

    @cached_property
    def risks(self) -> dict[str, dict]:
        return {r["Risk ID"]: r for r in self._read("risk_register.csv")}

    @cached_property
    def mapping(self) -> dict[str, dict]:
        return {r["Risk ID"]: r for r in self._read("risk_to_control.csv")}

    @cached_property
    def tests(self) -> dict[str, dict]:
        return {r["Test Case ID"]: r for r in self._read("test_cases.csv")}

    @cached_property
    def _test_pages(self) -> dict[str, str]:
        """Layer or domain code (L06, D09) -> page file name, read from the library folder when present."""
        lib = self.dir.parent.parent / "10_Test_Case_Library"
        pages = {}
        for f in sorted(lib.glob("*-*.*")) if lib.is_dir() else []:
            m = re.match(r"([LD]\d{2})-", f.name)
            if m and f.suffix in (".md", ".html"):
                pages[m.group(1)] = f.stem + ".html"
        return pages

    # ---- links -------------------------------------------------------------
    def control_url(self, cid: str) -> str:
        return f"{SITE}{CONTROL_PAGE}#{cid.lower()}"

    def risk_url(self, rid: str) -> str:
        name = self.risks.get(rid, {}).get("Risk Area", "")
        return f"{SITE}{RISK_PAGE}#{slug(rid + ' ' + name)}"

    def test_url(self, tid: str) -> str:
        page = self._test_pages.get(tid.split("-")[1]) if tid.count("-") == 2 else None
        return f"{SITE}{TEST_DIR}{page}#{tid.lower()}" if page else f"{SITE}{TEST_DIR}index.html"

    # ---- look-ups ----------------------------------------------------------
    def tests_for_control(self, cid: str) -> list[str]:
        return [t for t, r in self.tests.items() if cid in _ids(r["Controls"])]

    def controls_for_risk(self, rid: str) -> list[str]:
        return _ids(self.mapping.get(rid, {}).get("Control IDs", ""))

    def risks_for_control(self, cid: str) -> list[str]:
        return [r for r, m in self.mapping.items() if cid in _ids(m["Control IDs"])]

    def control(self, cid: str) -> dict | None:
        r = self.controls.get(cid.upper())
        if not r:
            return None
        cid = r["Control ID"]
        return {"id": cid, "name": r["Name"], "objective": r["Control Objective"], "tier": r["Tier"],
                "appliesTo": r["Applies To"], "risks": self.risks_for_control(cid),
                "testCases": self.tests_for_control(cid), "url": self.control_url(cid)}

    def risk(self, rid: str) -> dict | None:
        r = self.risks.get(rid.upper())
        if not r:
            return None
        rid, m = r["Risk ID"], self.mapping.get(r["Risk ID"], {})
        return {"id": rid, "name": r["Risk Area"], "narrative": r["Narrative"],
                "exampleResidualRisk": r["Example Residual Risk"], "controls": self.controls_for_risk(rid),
                "primaryControls": m.get("Primary Controls", ""), "evidenceRequired": m.get("Evidence Required", ""),
                "url": self.risk_url(rid)}

    def test_case(self, tid: str) -> dict | None:
        r = self.tests.get(tid.upper())
        if not r:
            return None
        return {"id": r["Test Case ID"], "title": r["Title"], "severity": r["Severity"], "method": r["Method"],
                "controls": _ids(r["Controls"]), "layer": r["Layer or Domain"], "url": self.test_url(r["Test Case ID"])}

    def get(self, any_id: str) -> dict | None:
        i = any_id.strip().upper()
        return self.control(i) if i.startswith("AI-CTRL") else self.risk(i) if i.startswith("AI-R") else self.test_case(i)

    def search(self, query: str, kind: str = "all", limit: int = 20) -> list[dict]:
        """Every query word must appear in the item's ID, name or description (case-insensitive)."""
        words = [w for w in query.lower().split() if w]
        if not words:
            return []
        pools = []
        if kind in ("all", "control"):
            pools += [("control", k, f"{k} {r['Name']} {r['Control Objective']}", r["Name"]) for k, r in self.controls.items()]
        if kind in ("all", "risk"):
            pools += [("risk", k, f"{k} {r['Risk Area']} {r['Narrative']}", r["Risk Area"]) for k, r in self.risks.items()]
        if kind in ("all", "test"):
            pools += [("test", k, f"{k} {r['Title']}", r["Title"]) for k, r in self.tests.items()]
        hits = []
        for typ, key, text, name in pools:
            low = text.lower()
            if all(w in low for w in words):
                in_name = sum(w in name.lower() for w in words)
                hits.append((-in_name, typ, key, name))
        hits.sort()
        return [{"type": t, "id": k, "name": n} for _, t, k, n in hits[:limit]]


def _print(obj, as_json: bool) -> None:
    if as_json or not isinstance(obj, dict):
        print(json.dumps(obj, indent=2, ensure_ascii=False))
        return
    for k, v in obj.items():
        print(f"{k:>20}: {', '.join(v) if isinstance(v, list) else v}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="wiki_data", description="Look up wiki controls, risks and test cases offline.")
    ap.add_argument("what", choices=["control", "risk", "test", "get", "search"])
    ap.add_argument("query")
    ap.add_argument("--kind", default="all", choices=["all", "control", "risk", "test"])
    ap.add_argument("--data")
    ap.add_argument("--json", action="store_true")
    try:
        a = ap.parse_args(argv)
        wd = WikiData(a.data)
    except SystemExit as e:
        return 0 if e.code == 0 else 2
    except FileNotFoundError as e:
        print(f"wiki_data: {e}", file=sys.stderr)
        return 2
    if a.what == "search":
        _print(wd.search(a.query, a.kind), True)
        return 0
    item = {"control": wd.control, "risk": wd.risk, "test": wd.test_case, "get": wd.get}[a.what](a.query)
    if item is None:
        print(f"wiki_data: {a.query} not found", file=sys.stderr)
        return 1
    _print(item, a.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
