"""What the home page header shows, read from the source files.

The header is the banner's stat tiles, the Version line, the "What's new" box
and its "Version X" line. build.py writes it from these functions, and
check_home.py uses the same functions to fail a pull request (or a push to
main) whose header no longer matches the source. Standard library only, so
the check runs without installing anything.
"""
import datetime
import os
import re
import unicodedata

NOTES = "09_Reference/19_Update_Notes.md"


def slug(text):
    """The heading anchor Python-Markdown's toc extension makes (separator "-")."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2)


def source_pages(src):
    """{path relative to src, with / separators: (meta, body)} for every Markdown page."""
    pages = {}
    for dirpath, dirs, files in os.walk(src):
        dirs.sort()
        for f in sorted(files):
            if f.endswith(".md"):
                path = os.path.join(dirpath, f)
                rel = os.path.relpath(path, src).replace(os.sep, "/")
                pages[rel] = front_matter(open(path, encoding="utf-8").read())
    return pages


def stats(src, pages=None):
    """The banner's tiles, in the order shown: [(number, label)]."""
    pages = pages or source_pages(src)
    text = "\n".join(body for _, body in pages.values())
    return [
        (len(re.findall(r"^### TC-[LD]\d\d-\d{3}:", text, re.M)), "Test Cases"),
        (len(re.findall(r"^#### AI-CTRL-\d{3}:", text, re.M)), "Control Objectives"),
        (len(re.findall(r"^### AI-R\d\d: ", text, re.M)), "Register Risks"),
        # A regional section is a top-level section (no parent) whose header names a group.
        (sum(1 for rel, (meta, _) in pages.items() if rel != "index.md" and not meta.get("parent") and meta.get("group")),
         "Regional Sections"),
        (sum(1 for rel in pages if rel.startswith("23_Framework_Crosswalks/") and not rel.endswith("index.md")),
         "Framework Crosswalks"),
        (len(pages), "Pages"),
    ]


def version_history(notes_body):
    """Rows of the Update Notes' full version history, newest first: [(version, date)]."""
    part = notes_body.split("\n## Full version history", 1)
    if len(part) < 2:
        return []
    return re.findall(r"^\| (\d+\.\d+) \| (\d{4}-\d{2}-\d{2}) \|", part[1], re.M)


def note_headings(notes_body):
    """Every update note heading, newest first: [(full heading, title)]."""
    notes = notes_body.split("\n## Full version history", 1)[0]
    return re.findall(r"^## ((?:Week ending )?\d{1,2} [A-Z][a-z]+ \d{4}: (.+))$", notes, re.M)


def long_date(iso):
    day = datetime.date.fromisoformat(iso)
    return f"{day.day} {day:%B %Y}"


def latest(notes_body):
    """The "What's new" box: the newest day in the version history, every update note of that day
    as (heading, label shown), and that day's version numbers.

    A note belongs to the day if its heading carries that date, or if one of that day's version rows
    links to it. The second rule covers a weekly note ("Week ending 21 November 2026") that goes live
    before the Saturday it is named after.
    """
    history = version_history(notes_body)
    if not history:
        raise SystemExit(f"{NOTES}: no rows in the full version history")
    day = max(d for _, d in history)
    numbers = [v for v, d in history if d == day]
    heading = long_date(day)
    rows = notes_body.split("\n## Full version history", 1)[1]
    linked = set()
    for line in re.findall(rf"^\| \d+\.\d+ \| {day} \|.*$", rows, re.M):
        linked.update(re.findall(r"\(#([\w-]+)\)", line))
    entries = []
    for full, title in note_headings(notes_body):
        if re.fullmatch(rf"(?:Week ending )?{re.escape(heading)}: .+", full) or slug(full) in linked:
            label = title[0].upper() + title[1:]
            if not full.endswith(f"{heading}: {title}"):
                label += ", " + full.split(": ", 1)[0][0].lower() + full.split(": ", 1)[0][1:]  # a note named after another day says which
            entries.append((full, label))
    return heading, entries, numbers
