"""AI-specific checks for code and agent configuration, with results in text,
JSON or SARIF 2.1.0. The rules live in ai_rules.json; each one names the wiki
controls it supports and the test cases that prove the fix.

It needs only the Python standard library and runs the same on Linux, macOS
and Windows, from a terminal, a git hook, CI or any AI assistant that can run
a command. The result does not depend on which model or tool wrote the code.

Usage:
    python aiwiki_check.py [PATH ...]                   # files or folders, default "."
    python aiwiki_check.py --staged                     # only lines added in the staged change
    python aiwiki_check.py --diff origin/main           # only lines added since a base (CI)
    python aiwiki_check.py --stdin --filename app.py    # content about to be written
    options: --format text|json|sarif  --output FILE  --fail-on HIGH|MEDIUM|LOW|NONE  --rules FILE

Exit codes: 0 no findings at or above --fail-on (default HIGH), 1 findings, 2 usage or runtime error.
Suppress one line with a comment containing "aiwiki: ignore" or "aiwiki: ignore AIW-004".
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve().parent
RULES = HERE / "ai_rules.json"
WIKI = "https://nachi065.github.io/AI-Security-Wiki/"
LIBRARY = WIKI + "03_Control_Library/03_AI_Security_Control_Objectives_Library.html#"
SEVERITY = {"HIGH": 3, "MEDIUM": 2, "LOW": 1, "NONE": 99}
SARIF_LEVEL = {"HIGH": "error", "MEDIUM": "warning", "LOW": "note"}
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".tox", ".mypy_cache"}
MCP_CONFIG_NAMES = {"mcp.json", ".mcp.json", "mcp_config.json", "claude_desktop_config.json", "settings.json", "cline_mcp_settings.json"}
LOOPBACK = {"localhost", "127.0.0.1", "::1", "[::1]"}
RUNNERS = {"npx": "npm", "pnpx": "npm", "bunx": "npm", "uvx": "py", "pipx": "py"}
DOCKER_VALUE_FLAGS = {"-e", "--env", "-v", "--volume", "-p", "--publish", "--name", "--network", "-w", "--workdir",
                      "--entrypoint", "--mount", "-u", "--user", "--env-file", "-l", "--label", "--platform"}


@dataclass
class Finding:
    rule: str
    severity: str
    path: str
    line: int
    message: str
    controls: list[str] = field(default_factory=list)
    testCases: list[str] = field(default_factory=list)


def load_rules(path: Path = RULES) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    token = data.get("modelOutputTokens", "")
    for r in data["rules"]:
        for key in ("pattern", "mustAlsoMatch", "unlessLine"):
            if r.get(key):
                r["_" + key] = re.compile(r[key].replace("{{modelOutput}}", token), re.I if key == "mustAlsoMatch" else 0)
    return data


def _applies(rule: dict, name: str) -> bool:
    return any(name.endswith(s) or name == s for s in rule.get("files", []))


def _suppressed(line: str, rule_id: str) -> bool:
    m = re.search(r"aiwiki:\s*ignore\b([A-Z0-9\-, ]*)", line)
    return bool(m) and (not m.group(1).strip() or rule_id in m.group(1))


def _finding(rule: dict, path: str, line: int, detail: str = "") -> Finding:
    msg = rule["message"] + (f" ({detail})" if detail else "")
    return Finding(rule["id"], rule["severity"], path, line, msg, rule.get("controls", []), rule.get("testCases", []))


def scan_lines(text: str, path: str, rules: dict) -> list[Finding]:
    name = PurePosixPath(path).name
    out = []
    active = [r for r in rules["rules"] if r["kind"] == "line" and _applies(r, name)]
    for n, line in enumerate(text.splitlines(), 1):
        for r in active:
            if not r["_pattern"].search(line):
                continue
            if r.get("_mustAlsoMatch") and not r["_mustAlsoMatch"].search(line):
                continue
            if r.get("_unlessLine") and r["_unlessLine"].search(line):
                continue
            if not _suppressed(line, r["id"]):
                out.append(_finding(r, path, n))
    return out


def _line_of(text: str, needle: str) -> int:
    i = text.find(needle)
    return text.count("\n", 0, i) + 1 if i >= 0 else 1


def _unpinned(command: str, args: list[str]) -> str | None:
    """Return a description of the unpinned package, or None if it is pinned."""
    base = PurePosixPath(command.replace("\\", "/")).name.lower().removesuffix(".cmd").removesuffix(".exe")
    rest = [a for a in args if isinstance(a, str)]
    if base in ("docker", "podman") and "run" in rest:
        after, skip = rest[rest.index("run") + 1:], False
        for a in after:
            if skip:
                skip = False
            elif a in DOCKER_VALUE_FLAGS:
                skip = True
            elif not a.startswith("-"):
                return None if "@sha256:" in a else f"image {a} is not pinned by digest"
        return None
    if base not in RUNNERS:
        return None
    if base == "pipx" and rest[:1] == ["run"]:
        rest = rest[1:]
    if "--from" in rest and rest.index("--from") + 1 < len(rest):
        pkg = rest[rest.index("--from") + 1]
    else:
        pkg = next((a for a in rest if not a.startswith("-")), "")
    if not pkg:
        return None
    if RUNNERS[base] == "npm":
        version = pkg[1:].partition("@")[2] if pkg.startswith("@") else pkg.partition("@")[2]
    else:
        version = re.split(r"==|@", pkg, maxsplit=1)[1] if re.search(r"==|@", pkg) else ""
    if not version or version in ("latest", "next") or not re.match(r"v?\d", version):
        return f"{base} {pkg}"
    return None


def scan_mcp_config(text: str, path: str, rules: dict) -> list[Finding]:
    try:
        data = json.loads(text)
    except ValueError:
        return []
    if not isinstance(data, dict):
        return []
    servers = {}
    for key in ("mcpServers", "servers", "mcp_servers"):
        if isinstance(data.get(key), dict):
            servers.update(data[key])
    if isinstance(data.get("mcp"), dict) and isinstance(data["mcp"].get("servers"), dict):
        servers.update(data["mcp"]["servers"])
    by_id = {r["id"]: r for r in rules["rules"]}
    lines = text.splitlines()
    out = []
    for name, spec in servers.items():
        if not isinstance(spec, dict):
            continue
        n = _line_of(text, json.dumps(name))
        if _suppressed(lines[n - 1] if n <= len(lines) else "", ""):
            continue
        what = _unpinned(str(spec.get("command", "")), spec.get("args", []) or [])
        if what:
            out.append(_finding(by_id["AIW-007"], path, n, f"server {name}: {what}"))
        url = str(spec.get("url") or spec.get("serverUrl") or spec.get("httpUrl") or "")
        m = re.match(r"http://(\[[^\]]+\]|[^/:]+)", url, re.I)
        if m and m.group(1).lower() not in LOOPBACK:
            out.append(_finding(by_id["AIW-008"], path, n, f"server {name}: {url}"))
        auto = [k for k in ("autoApprove", "alwaysAllow", "trust") if spec.get(k) not in (None, False, [], "")]
        if auto:
            out.append(_finding(by_id["AIW-009"], path, n, f"server {name}: {', '.join(auto)}"))
    return out


def scan_text(text: str, path: str, rules: dict | None = None) -> list[Finding]:
    rules = rules or load_rules()
    found = scan_lines(text, path, rules)
    name = PurePosixPath(path).name
    if name in MCP_CONFIG_NAMES or (name.endswith(".json") and ("mcpServers" in text or '"servers"' in text)):
        found += scan_mcp_config(text, path, rules)
    return found


def _files(paths: list[str]):
    for p in map(Path, paths):
        if p.is_file():
            yield p
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.is_file() and not SKIP_DIRS.intersection(f.relative_to(p).parts[:-1]):
                    yield f


def _rel(p: Path) -> str:
    try:
        return p.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return p.as_posix()


def scan_paths(paths: list[str], rules: dict) -> list[Finding]:
    out = []
    for f in _files(paths):
        if f.name == RULES.name:  # the rules file quotes every pattern it looks for
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        out += scan_text(text, _rel(f), rules)
    return out


def added_lines(diff: str) -> dict[str, set[int]]:
    """Map each file in a unified diff (-U0) to the line numbers it adds."""
    files: dict[str, set[int]] = {}
    current = None
    for line in diff.splitlines():
        if line.startswith("+++ "):
            current = None if line[4:].strip() == "/dev/null" else line[4:].strip().removeprefix("b/")
            if current:
                files.setdefault(current, set())
        elif line.startswith("@@") and current:
            m = re.search(r"\+(\d+)(?:,(\d+))?", line)
            start, count = int(m.group(1)), int(m.group(2) or 1)
            files[current].update(range(start, start + count))
    return files


def scan_diff(diff_args: list[str], rules: dict) -> list[Finding]:
    diff = subprocess.run(["git", "diff", "-U0", "--no-color", *diff_args], capture_output=True, text=True,
                          encoding="utf-8", check=True).stdout
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
    out = []
    for path, lines in added_lines(diff).items():
        f = Path(root) / path
        if not f.is_file():
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        out += [x for x in scan_text(text, path, rules) if x.line in lines]
    return out


def to_sarif(findings: list[Finding], rules: dict) -> dict:
    used = sorted({f.rule for f in findings})
    meta = {r["id"]: r for r in rules["rules"]}
    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {
                "name": "aiwiki-check",
                "informationUri": WIKI + "24_Builder_Track/05_Builder_Toolkit.html",
                "rules": [{
                    "id": rid,
                    "name": meta[rid]["title"],
                    "shortDescription": {"text": meta[rid]["title"]},
                    "fullDescription": {"text": meta[rid]["message"]},
                    "help": {"text": meta[rid]["remediation"]},
                    "helpUri": LIBRARY + meta[rid]["controls"][0].lower(),
                    "defaultConfiguration": {"level": SARIF_LEVEL[meta[rid]["severity"]]},
                    "properties": {"tags": ["security", "ai"] + meta[rid]["controls"],
                                   "controls": meta[rid]["controls"], "risks": meta[rid].get("risks", []),
                                   "testCases": meta[rid]["testCases"]},
                } for rid in used],
            }},
            "results": [{
                "ruleId": f.rule,
                "level": SARIF_LEVEL[f.severity],
                "message": {"text": f.message},
                "locations": [{"physicalLocation": {"artifactLocation": {"uri": f.path}, "region": {"startLine": f.line}}}],
                "properties": {"controls": f.controls, "testCases": f.testCases},
            } for f in findings],
        }],
    }


def render(findings: list[Finding], fmt: str, rules: dict) -> str:
    if fmt == "json":
        return json.dumps([asdict(f) for f in findings], indent=2)
    if fmt == "sarif":
        return json.dumps(to_sarif(findings, rules), indent=2)
    if not findings:
        return "aiwiki-check: no findings"
    rows = [f"{f.path}:{f.line}: {f.severity} {f.rule} {f.message} [controls: {', '.join(f.controls)}; "
            f"prove with: {', '.join(f.testCases)}]" for f in findings]
    return "\n".join(rows + [f"aiwiki-check: {len(findings)} finding(s)"])


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="aiwiki_check", description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="*")
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--staged", action="store_true")
    src.add_argument("--diff", metavar="BASE")
    src.add_argument("--stdin", action="store_true")
    ap.add_argument("--filename", default="stdin")
    ap.add_argument("--format", choices=["text", "json", "sarif"], default="text")
    ap.add_argument("--output")
    ap.add_argument("--fail-on", default="HIGH", type=str.upper, choices=list(SEVERITY))
    ap.add_argument("--rules", default=str(RULES))
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return 0 if e.code == 0 else 2
    try:
        rules = load_rules(Path(a.rules))
        if a.stdin:
            findings = scan_text(sys.stdin.read(), a.filename, rules)
        elif a.staged:
            findings = scan_diff(["--cached"], rules)
        elif a.diff:
            findings = scan_diff([f"{a.diff}...HEAD"], rules)
        else:
            findings = scan_paths(a.paths or ["."], rules)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as e:
        print(f"aiwiki-check: error: {e}", file=sys.stderr)
        return 2
    report = render(findings, a.format, rules)
    if a.output:
        Path(a.output).write_text(report + "\n", encoding="utf-8")
    else:
        print(report)
    worst = max((SEVERITY[f.severity] for f in findings), default=0)
    return 1 if worst >= SEVERITY[a.fail_on] else 0


if __name__ == "__main__":
    sys.exit(main())
