"""Turn what the Builder Track tools produce into rows for the wiki's Excel
templates, so a builder can hand evidence to a risk owner or auditor.

Inputs (any mix):
  --audit-log FILE   the guard's hash-chained JSON lines log (guard.AuditLog)
  --sarif FILE       SARIF from aiwiki_check.py, or any tool that tags results with wiki control IDs

Outputs (CSV, UTF-8):
  --controls FILE    one row per control, in the column names of the
                     AI Security Audit and Evidence Checklist (Controls sheet)
  --tests FILE       one row per wiki test case the evidence relates to, in the
                     column names of the AI Security Test Case Tracker

    python evidence_export.py --audit-log audit.jsonl --sarif aiwiki.sarif --controls controls.csv --tests tests.csv

The rows record what was observed, not a verdict. A denied call in the log
shows the control acted at least once; it does not show the control is
effective. The Result and Score columns are left for the reviewer.
Standard library only; works on Linux, macOS and Windows.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

# Guard decision reason -> (control, wiki test cases that check it). Matches the
# Prove it table on Secure Your First Agent.
REASONS = {
    "DENY_TOKEN": ("AI-CTRL-015", ["TC-L09-001", "TC-L09-003"]),
    "DENY_SCOPE": ("AI-CTRL-016", ["TC-L09-004", "TC-L06-017"]),
    "DENY_NOT_ALLOWED": ("AI-CTRL-024", ["TC-L06-006", "TC-L06-013"]),
    "DENY_DEFINITION_CHANGED": ("AI-CTRL-024", ["TC-L06-008"]),
    "DENY_ARGS": ("AI-CTRL-022", ["TC-L06-014", "TC-L06-019", "TC-L07-008"]),
    "PENDING_APPROVAL": ("AI-CTRL-023", ["TC-L06-015", "TC-L06-016"]),
    "DENY_APPROVAL": ("AI-CTRL-023", ["TC-L06-015", "TC-L06-016"]),
    "DENY_RATE": ("AI-CTRL-025", ["TC-L06-021"]),
    "DENY_KILL": ("AI-CTRL-025", ["TC-L06-022", "TC-L06-023", "TC-L06-024"]),
}
LOG_CONTROL, LOG_TESTS = "AI-CTRL-008", ["TC-L06-028", "TC-L17-004", "TC-L17-020"]

CONTROL_COLUMNS = ["Control ID", "Control", "Result", "Evidence Ref", "Evidence Collection Date", "Auditor Notes"]
# Evidence Source is left out: the tracker limits it to vendor-evaluation values.
TEST_COLUMNS = ["Test Case ID", "Date Run", "Evidence Ref", "Notes"]


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def verify_chain(lines: list[dict]) -> tuple[bool, int]:
    """Same check as guard.AuditLog.verify, repeated here so this tool needs no guard import."""
    prev = "0" * 64
    for n, entry in enumerate(lines):
        entry = dict(entry)
        claimed = entry.pop("hash", None)
        expect = hashlib.sha256(json.dumps(entry, sort_keys=True, default=str).encode()).hexdigest()
        if entry.get("prev") != prev or claimed != expect:
            return False, n
        prev = claimed
    return True, len(lines)


def from_audit_log(path: Path) -> list[dict]:
    """Evidence items from the guard's log: one per (control, reason) with counts."""
    entries = [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    ok, n = verify_chain(entries)
    ref = f"{path.name} sha256:{_sha(path)}"
    day = _day(entries[-1]["ts"]) if entries else _today()
    counts: dict[str, int] = defaultdict(int)
    for e in entries:
        reason = e.get("reason") or ("PENDING_APPROVAL" if e.get("event") == "approval_requested" else None)
        if reason:
            counts[reason] += 1
    items = [{"control": LOG_CONTROL, "tests": LOG_TESTS, "ref": ref, "date": day, "source": "Log",
              "note": (f"Hash chain verified over {n} entries." if ok else
                       f"Hash chain BROKEN at entry {n}: the log was edited or truncated.") + f" {len(entries)} entries in total."}]
    for reason, count in sorted(counts.items()):
        if reason in REASONS:
            control, tests = REASONS[reason]
            items.append({"control": control, "tests": tests, "ref": ref, "date": day, "source": "Log",
                          "note": f"{count} decision(s) with reason {reason} recorded by the guard."})
    return items


def from_sarif(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    ref, day, items = f"{path.name} sha256:{_sha(path)}", _today(), []
    for run in data.get("runs", []):
        tool = run.get("tool", {}).get("driver", {}).get("name", "scanner")
        per: dict[str, list] = defaultdict(list)
        for res in run.get("results", []):
            props = res.get("properties", {})
            for c in props.get("controls", []):
                per[c].append((res.get("ruleId", "?"), props.get("testCases", [])))
        for control, hits in sorted(per.items()):
            rules = sorted({r for r, _ in hits})
            tests = sorted({t for _, ts in hits for t in ts})
            items.append({"control": control, "tests": tests, "ref": ref, "date": day, "source": "Scan",
                          "note": f"{tool}: {len(hits)} open finding(s) ({', '.join(rules)}). Resolve or record an exception."})
    return items


def _day(ts: float) -> str:
    return datetime.datetime.fromtimestamp(float(ts), datetime.timezone.utc).date().isoformat()


def _today() -> str:
    return datetime.datetime.now(datetime.timezone.utc).date().isoformat()


def control_rows(items: list[dict], names: dict[str, str]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for it in items:
        grouped[it["control"]].append(it)
    return [{"Control ID": c, "Control": names.get(c, ""), "Result": "",
             "Evidence Ref": "; ".join(sorted({i["ref"] for i in its})),
             "Evidence Collection Date": max(i["date"] for i in its),
             "Auditor Notes": " ".join(i["note"] for i in its)} for c, its in sorted(grouped.items())]


def test_rows(items: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for it in items:
        for t in it["tests"]:
            grouped[t].append(it)
    return [{"Test Case ID": t, "Date Run": max(i["date"] for i in its),
             "Evidence Ref": "; ".join(sorted({i["ref"] for i in its})),
             "Notes": " ".join(sorted({f'{i["source"]}: {i["note"]}' for i in its}))} for t, its in sorted(grouped.items())]


def _write(path: str, columns: list[str], rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columns, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def _control_names() -> dict[str, str]:
    try:
        from wiki_data import WikiData
        return {k: v["Name"] for k, v in WikiData().controls.items()}
    except (ImportError, FileNotFoundError):
        return {}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="evidence_export", description="Builder Track evidence -> template rows.")
    ap.add_argument("--audit-log", action="append", default=[])
    ap.add_argument("--sarif", action="append", default=[])
    ap.add_argument("--controls", help="CSV for the Audit and Evidence Checklist")
    ap.add_argument("--tests", help="CSV for the Test Case Tracker")
    a = ap.parse_args(argv)
    if not (a.audit_log or a.sarif) or not (a.controls or a.tests):
        ap.print_usage(sys.stderr)
        return 2
    try:
        items = [i for p in a.audit_log for i in from_audit_log(Path(p))]
        items += [i for p in a.sarif for i in from_sarif(Path(p))]
    except (OSError, ValueError, KeyError) as e:
        print(f"evidence_export: error: {e}", file=sys.stderr)
        return 2
    if a.controls:
        _write(a.controls, CONTROL_COLUMNS, control_rows(items, _control_names()))
    if a.tests:
        _write(a.tests, TEST_COLUMNS, test_rows(items))
    broken = any("BROKEN" in i["note"] for i in items)
    print(f"evidence_export: {len(items)} evidence item(s)" + ("; WARNING: an audit log failed verification" if broken else ""))
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
