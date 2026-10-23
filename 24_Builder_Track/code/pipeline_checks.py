"""Reference developer-pipeline checks for code written with AI assistants and coding agents.

Standard library only, Python 3.10 or later. One file, four uses:

  pre-commit   scan the staged diff for secrets and for personal data written
               to logs                          -> scan_secrets, scan_log_lines
  commit-msg   require an AI-Assistance trailer that says how the change was
               made                             -> check_trailer
  scan         scan text on stdin (for a coding agent's pre-write hook)
  ci <base>    the same checks over every commit since <base>, for the pipeline

The point is that the same checks run in three places: on the developer's
machine, inside the coding agent before it writes a file, and in CI, where they
cannot be skipped. A local hook can be bypassed (git commit --no-verify), so CI
is the control; the local hooks only make failures cheap.

This is a teaching reference, not a replacement for a maintained secret
scanner. Its patterns catch common, high-confidence formats only. Run a
maintained scanner in CI as well, and treat a clean result here as "nothing
obvious", not "no secrets".
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).parent

# --------------------------------------------------------------------------
# Secrets
# --------------------------------------------------------------------------

# High-confidence formats. Each is a Python regular expression, so a pattern
# that starts with dashes is a pattern and never mistaken for an option.
SECRET_PATTERNS = {
    "private key block": r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP |ENCRYPTED )?PRIVATE KEY-----",
    "AWS access key ID": r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b",
    "GitHub token": r"\bgh[pousr]_[A-Za-z0-9]{36,}\b",
    "Slack token": r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b",
    "Google API key": r"\bAIza[0-9A-Za-z_\-]{35}\b",
    "provider API key (sk- form)": r"\bsk-(?:[A-Za-z0-9_\-]{2,20}-)?[A-Za-z0-9_\-]{32,}\b",
    "JSON web token": r"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\b",
    "credential assigned to a literal": (
        r"(?i)\b[\w.\-]*(?:api[_\-]?key|secret|passw(?:or)?d|token|credential)[\w.\-]*\b"
        r"\s*[:=]\s*[\"'][^\"'\s]{16,}[\"']"
    ),
}
_SECRETS = {name: re.compile(p) for name, p in SECRET_PATTERNS.items()}

# Placeholders that look like credentials but are not.
_PLACEHOLDER = re.compile(r"(?i)(example|placeholder|changeme|dummy|your[_\-]?|x{8,}|<[^>]+>|\$\{[^}]+\})")


@dataclass
class Finding:
    check: str        # secret, personal-data-in-log, trailer
    where: str        # file:line, "commit message" or "stdin"
    detail: str

    def __str__(self) -> str:
        return f"{self.where}: {self.check}: {self.detail}"


def scan_secrets(text: str, where: str = "stdin") -> list[Finding]:
    findings = []
    for n, line in enumerate(text.splitlines(), 1):
        for name, rx in _SECRETS.items():
            m = rx.search(line)
            if m and not _PLACEHOLDER.search(m.group(0)):
                findings.append(Finding("secret", f"{where}:{n}", name))
    return findings


# --------------------------------------------------------------------------
# Personal data written to logs
# --------------------------------------------------------------------------

LOG_CALL = re.compile(
    r"\b(?:console\.(?:log|info|warn|error|debug)|logger\.\w+|logging\.\w+|log\.\w+|print|println|fmt\.Print\w*)\s*\("
)


def personal_fields(map_path: Path) -> set[str]:
    """Field names the data map classifies as personal or sensitive. The map is
    the single place where a team says which fields are personal; the same file
    drives redaction in privacy.py."""
    data = json.loads(Path(map_path).read_text())
    return {f for c in data["categories"] if c["sensitivity"] != "not-personal" for f in c["fields"]}


def scan_log_lines(text: str, fields: set[str], where: str = "stdin") -> list[Finding]:
    """Flag a log call whose arguments name a personal field. A name match is a
    prompt to route the call through a redacting logger, not proof of a leak."""
    if not fields:
        return []
    names = re.compile(r"\b(" + "|".join(sorted(map(re.escape, fields))) + r")\b")
    findings = []
    for n, line in enumerate(text.splitlines(), 1):
        call = LOG_CALL.search(line)
        if call and (m := names.search(line, call.end())):
            findings.append(Finding("personal-data-in-log", f"{where}:{n}",
                                    f"log call names '{m.group(1)}'; use the redacting logger"))
    return findings


# --------------------------------------------------------------------------
# AI-Assistance trailer
# --------------------------------------------------------------------------

# This wiki's convention, not a standard: one trailer line per commit saying how
# the change was made, so that review rules and metrics can use it (TC-L14-021).
TRAILER = re.compile(r"(?mi)^AI-Assistance:\s*(none|suggestions|agent)\s*$")


def check_trailer(message: str) -> list[Finding]:
    body = "\n".join(l for l in message.splitlines() if not l.startswith("#"))
    if TRAILER.search(body):
        return []
    return [Finding("trailer", "commit message",
                    "add a line 'AI-Assistance: none', 'AI-Assistance: suggestions' or 'AI-Assistance: agent'")]


# --------------------------------------------------------------------------
# Diffs
# --------------------------------------------------------------------------

def added_lines(diff: str) -> dict[str, str]:
    """Map each file in a unified diff to the text of its added lines, so that
    checks see only what this change introduces."""
    out: dict[str, list[str]] = {}
    current = None
    for line in diff.splitlines():
        if line.startswith("+++ "):
            current = None if line[4:] == "/dev/null" else re.sub(r"^b/", "", line[4:])
            if current:
                out.setdefault(current, [])
        elif current and line.startswith("+") and not line.startswith("+++"):
            out[current].append(line[1:])
    return {f: "\n".join(lines) for f, lines in out.items()}


SKIP = re.compile(r"(?:^|/)(?:package-lock\.json|pnpm-lock\.yaml|yarn\.lock|poetry\.lock|Cargo\.lock)$")


def scan_diff(diff: str, fields: set[str]) -> list[Finding]:
    findings = []
    for path, text in added_lines(diff).items():
        if SKIP.search(path):
            continue
        findings += scan_secrets(text, path)
        findings += scan_log_lines(text, fields, path)
    return findings


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


# --------------------------------------------------------------------------
# Command line
# --------------------------------------------------------------------------

def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    mode, rest = argv[0], argv[1:]
    map_path = HERE / "privacy_map.json"
    fields = personal_fields(map_path) if map_path.exists() else set()
    if mode == "pre-commit":
        findings = scan_diff(_git("diff", "--cached", "--unified=0", "--no-color"), fields)
    elif mode == "commit-msg":
        findings = check_trailer(Path(rest[0]).read_text())
    elif mode == "scan":
        text = sys.stdin.read()
        findings = scan_secrets(text) + scan_log_lines(text, fields)
    elif mode == "ci":
        base = rest[0]
        findings = scan_diff(_git("diff", "--unified=0", "--no-color", f"{base}...HEAD"), fields)
        for sha in _git("rev-list", "--no-merges", f"{base}..HEAD").split():
            for f in check_trailer(_git("log", "-1", "--format=%B", sha)):
                findings.append(Finding(f.check, f"commit {sha[:12]}", f.detail))
    else:
        print(f"unknown mode: {mode}", file=sys.stderr)
        return 2
    for f in findings:
        print(f, file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
