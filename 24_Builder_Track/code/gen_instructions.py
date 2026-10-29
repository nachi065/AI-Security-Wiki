"""Write the Builder Track's AI security rules into a repository as the
instruction file each coding assistant reads, all from one source
(agent_instructions.txt), so every assistant gets the same rules.

    python gen_instructions.py --out PATH/TO/YOUR/REPO            # all of them
    python gen_instructions.py --out . --only AGENTS.md GEMINI.md  # some of them
    python gen_instructions.py --out . --check                     # exit 1 if any is missing or out of date

Existing files are left alone unless you pass --force, because they may hold
your own instructions; merge the rules into them by hand instead.
The locations below are the ones each tool documented as of mid-2026. Check
each tool's current documentation, because they change.
Standard library only; works on Linux, macOS and Windows.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "agent_instructions.txt"

# target name -> (path in the repository, front matter or None)
TARGETS = {
    "AGENTS.md": ("AGENTS.md", None),
    "CLAUDE.md": ("CLAUDE.md", None),
    "GEMINI.md": ("GEMINI.md", None),
    "copilot": (".github/copilot-instructions.md", None),
    "cursor": (".cursor/rules/ai-security-wiki.mdc",
               "---\ndescription: AI security rules from the AI Security Wiki Builder Track\nglobs:\nalwaysApply: true\n---\n"),
}


def render(name: str) -> str:
    _, front = TARGETS[name]
    note = "<!-- Generated from the AI Security Wiki Builder Track (gen_instructions.py). Regenerate rather than edit. -->\n\n"
    return (front or "") + note + SOURCE.read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="gen_instructions", description="Write coding-assistant instruction files.")
    ap.add_argument("--out", required=True, help="the repository to write into")
    ap.add_argument("--only", nargs="+", choices=list(TARGETS))
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if a file is missing or differs")
    a = ap.parse_args(argv)
    root, status = Path(a.out), 0
    for name in a.only or TARGETS:
        path, text = root / TARGETS[name][0], render(name)
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            print(f"up to date  {path}")
        elif a.check:
            print(f"{'differs' if current is not None else 'missing':<11} {path}")
            status = 1
        elif current is not None and not a.force:
            print(f"skipped     {path} (exists; use --force or merge by hand)")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
            print(f"wrote       {path}")
    return status


if __name__ == "__main__":
    sys.exit(main())
