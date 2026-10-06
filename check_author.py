#!/usr/bin/env python3
"""Author check.

Every page names its author. Pages listed in AUTHOR_LOCK.txt were written or
co-written by the original author, and his name must stay on them. Pages that
are not listed belong to whoever is named as their author and are not locked.

Usage: python3 check_author.py [--root DIR] [--lock FILE]
  --root  the site to check (default: this folder)
  --lock  the trusted list of locked pages (default: ROOT/AUTHOR_LOCK.txt)
"""
import argparse
import os
import re
import sys

AUTHOR = "Nachiket Sathaye"
parser = argparse.ArgumentParser()
parser.add_argument("--root", default=os.path.dirname(os.path.abspath(__file__)))
parser.add_argument("--lock")
args = parser.parse_args()
ROOT = os.path.abspath(args.root)
LOCK = args.lock or os.path.join(ROOT, "AUTHOR_LOCK.txt")
errors = []


def text(path):
    return open(os.path.join(ROOT, path), encoding="utf-8").read()


def page_authors(source_path):
    """Names from the author and coauthors lines of a page header."""
    header = re.match(r"^---\n(.*?)\n---\n", text(source_path), re.S)
    names = []
    if header:
        for key in ("author", "coauthors"):
            found = re.search(rf"^{key}:(.*)$", header.group(1), re.M)
            if found:
                names += [n.strip().strip('"') for n in found.group(1).split(",") if n.strip().strip('"')]
    return names


# The wiki as a whole keeps its original author credit.
if text("AUTHORS").splitlines()[0].strip() != f"Original author: {AUTHOR}":
    errors.append('AUTHORS: first line must be "Original author: ' + AUTHOR + '"')
for path in ("README.md", "CONTRIBUTING.md"):
    if f"**{AUTHOR}**" not in text(path):
        errors.append(f"{path}: original author credit missing")

# Locked pages: the original author must remain author or co-author.
locked = [line.strip() for line in open(LOCK, encoding="utf-8") if line.strip() and not line.startswith("#")]
for source_path in locked:
    if not os.path.exists(os.path.join(ROOT, source_path)):
        errors.append(f"{source_path}: locked page was removed or renamed")
    elif AUTHOR not in page_authors(source_path):
        errors.append(f"{source_path}: {AUTHOR} must remain author or co-author of this page")

# Every page: has a named author, and the published HTML shows the same names.
pages = 0
for dirpath, dirs, files in os.walk(os.path.join(ROOT, "source")):
    for name in files:
        if not name.endswith(".md"):
            continue
        pages += 1
        source_path = os.path.relpath(os.path.join(dirpath, name), ROOT)
        html_path = os.path.relpath(source_path, "source")[:-3] + ".html"
        names = page_authors(source_path)
        if not names:
            errors.append(f"{source_path}: add an 'author:' line to the page header")
            continue
        if not os.path.exists(os.path.join(ROOT, html_path)):
            errors.append(f"{html_path}: page has not been built (run build.py)")
            continue
        page = text(html_path)
        label = ("Authors: " if len(names) > 1 else "Author: ") + ", ".join(names)
        if f'<meta name="author" content="{", ".join(names)}">' not in page or label not in page:
            errors.append(f"{html_path}: author shown does not match {source_path} (run build.py)")

if errors:
    print("Author check FAILED:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print(f"Author check passed ({pages} pages, {len(locked)} locked to {AUTHOR}).")
