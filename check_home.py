#!/usr/bin/env python3
"""Home page header check.

Fails when the home page header is out of date: the stat tiles, the Version
line, the "What's new" box and its "Version X" line. Run on every pull request
and on every push to main, so whatever goes live shows the current numbers
and every update of the day.

It checks three things:

1. The source agrees with itself: the home page's `version:`, its
   "**Version:**" line, the top row of its Version History table and the
   newest row of the Update Notes' full version history name the same
   version, and the home table holds the three newest rows.
2. With --base (the files on main), the change record moves with the content:
   a change to the update notes needs a new version row, earlier version rows
   are never rewritten, and every new update note is dated the same day as a
   new version row or linked from one, so it shows under "What's new".
3. The committed index.html matches what build.py would write from the
   source: the tiles, the Version line and the "What's new" box.

Usage: python3 check_home.py [--root DIR] [--base DIR]
Standard library only. It reads the files under --root and never runs them.
"""
import argparse
import datetime
import html
import os
import re
import sys

import home_header as hh

parser = argparse.ArgumentParser()
parser.add_argument("--root", default=os.path.dirname(os.path.abspath(__file__)))
parser.add_argument("--base", help="a checkout of main, to compare the change record with")
args = parser.parse_args()
errors = []
FIX = "Run python3 build.py and commit index.html."


def load(root):
    src = os.path.join(root, "source")
    home_meta, home_body = hh.front_matter(open(os.path.join(src, "index.md"), encoding="utf-8").read())
    _, notes = hh.front_matter(open(os.path.join(src, hh.NOTES), encoding="utf-8").read())
    return src, home_meta, home_body, notes


def key(version):
    return tuple(int(x) for x in version.split("."))


src, home_meta, home_body, notes = load(args.root)
history = hh.version_history(notes)
if not history:
    sys.exit(f"source/{hh.NOTES}: no rows in the full version history")
newest = history[0][0]

# 1. The source agrees with itself.
header = re.search(r"^> \*\*Version:\*\* (\S+)", home_body, re.M)
for where, value in (("`version:` in its header", home_meta.get("version")),
                     ("the **Version:** line", header.group(1) if header else None)):
    if value != newest:
        errors.append(f"source/index.md: {where} is {value}, but the newest row of the full version history is {newest}")
table = home_body.split("## 20. Version History", 1)[-1].split("\n## ", 1)[0]
shown = re.findall(r"^\| (\d+\.\d+) \| (\d{4}-\d{2}-\d{2}) \|", table, re.M)
if shown != history[:3]:
    errors.append("source/index.md: the Version History table must hold the three newest rows of the full version history, "
                  f"newest first: {', '.join(v for v, _ in history[:3])} (it has {', '.join(v for v, _ in shown) or 'none'})")
for (v1, d1), (v2, d2) in zip(history, history[1:]):
    if key(v1) <= key(v2) or d1 < d2:
        errors.append(f"source/{hh.NOTES}: full version history is not newest first at {v1} ({d1}) then {v2} ({d2})")
tomorrow = (datetime.datetime.now(datetime.timezone.utc).date() + datetime.timedelta(days=1)).isoformat()
if history[0][1] > tomorrow:
    errors.append(f"source/{hh.NOTES}: version {newest} is dated {history[0][1]}, which is in the future; "
                  "date the row on the day it goes live")

# 2. The change record moves with the content.
if args.base:
    _, _, _, base_notes = load(args.base)
    rows = lambda body: re.findall(r"^\| \d+\.\d+ \| \d{4}-\d{2}-\d{2} \|.*$", body.split("\n## Full version history", 1)[-1], re.M)
    base_rows, rows_now = rows(base_notes), rows(notes)
    for row in base_rows:
        if row not in rows_now:
            errors.append(f"source/{hh.NOTES}: version row {row.split(' | ')[0][2:]} on main was changed or removed; "
                          "the history is append-only, so record a correction as a new row")
    base_versions = {v for v, _ in hh.version_history(base_notes)}
    new_rows = [r for r in rows_now if r.split(" | ")[0][2:] not in base_versions]
    if notes.split("\n## Full version history", 1)[0] != base_notes.split("\n## Full version history", 1)[0] and not new_rows:
        errors.append(f"source/{hh.NOTES}: the update notes changed but no version row was added. Add the next version "
                      f"after {max(base_versions, key=key)} to the full version history, dated the day it goes live, "
                      "and put it on the home page (version:, the Version line and the Version History table)")
    base_heads = {full for full, _ in hh.note_headings(base_notes)}
    new_days = {hh.long_date(r.split(" | ")[1]) for r in new_rows}
    new_links = {a for r in new_rows for a in re.findall(r"\(#([\w-]+)\)", r)}
    for full, _ in hh.note_headings(notes):
        if full in base_heads or not new_rows:
            continue  # with no new row, the error above already applies
        day = re.match(r"(?:Week ending )?(.+?): ", full).group(1)
        if day not in new_days and hh.slug(full) not in new_links:
            errors.append(f'source/{hh.NOTES}: the new note "{full}" is not dated the same day as a new version row '
                          f"and no new row links to it (#{hh.slug(full)}), so it would not show under What's new")

# 3. The committed index.html matches the source.
page = open(os.path.join(args.root, "index.html"), encoding="utf-8").read()
tiles = [(int(n), html.unescape(label)) for n, label in re.findall(r'<div class="stat"><b>(\d+)</b><span>([^<]*)</span></div>', page)]
expected = hh.stats(src)
if tiles != expected:
    have = {label: n for n, label in tiles}
    diff = "; ".join(f"{label} shows {have.get(label, 'nothing')}, should be {n}" for n, label in expected if have.get(label) != n)
    errors.append(f"index.html: the stat tiles are out of date ({diff or 'tiles differ'}). {FIX}")
shown_version = re.search(r"<strong>Version:</strong> ([^<\s]+)", page)
if not shown_version or shown_version.group(1) != newest:
    errors.append(f"index.html: the Version line shows {shown_version.group(1) if shown_version else 'nothing'}, "
                  f"the source says {newest}. {FIX}")
heading, entries, numbers = hh.latest(notes)
box = re.search(r"<p><strong>What's new: ([^<]+)</strong></p>\s*<ul>(.*?)</ul>\s*<p>Versions? ([^;]+);", page, re.S)
if not box:
    errors.append(f"index.html: no \"What's new\" box. {FIX}")
else:
    listed = [html.unescape(re.sub(r"<[^>]+>", "", li)).strip() for li in re.findall(r"<li>(.*?)</li>", box.group(2), re.S)]
    want = [label for _, label in entries]
    span = numbers[0] if len(numbers) == 1 else f"{numbers[-1]} to {numbers[0]}"
    if html.unescape(box.group(1)) != heading:
        errors.append(f"index.html: What's new shows {box.group(1)}, the newest version is dated {heading}. {FIX}")
    if listed != want:
        errors.append(f"index.html: What's new lists {listed}, but the updates of {heading} are {want}. {FIX}")
    if box.group(3).strip() != span:
        errors.append(f"index.html: What's new says Version {box.group(3).strip()}, the source says {span}. {FIX}")
if not entries:
    errors.append(f"source/{hh.NOTES}: no update note belongs to {heading}, the date of version {newest}. Date the note's "
                  "heading that day, or link the version row to the note (#anchor)")

for e in errors:
    print(e)
if errors:
    print(f"\n{len(errors)} problem(s) with the home page header.")
    sys.exit(1)
print(f"Home page header is current: version {newest}, What's new {heading} ({len(entries)} update(s)), "
      + ", ".join(f"{n} {label}" for n, label in expected))
