#!/usr/bin/env python3
"""Author check.

Every page names its author, with optional co-authors. Credit can be added
but never taken away: compared with the main branch, no page may lose a name,
have its author replaced, or be removed or renamed.

Usage: python3 check_author.py [--root DIR] [--base DIR]
  --root  the site to check (default: this folder)
  --base  a checkout of the main branch to compare against. Without it, only
          the page-level checks run.
"""
import argparse
import os
import re
import sys

ORIGINAL_AUTHOR = "Nachiket Sathaye"
parser = argparse.ArgumentParser()
parser.add_argument("--root", default=os.path.dirname(os.path.abspath(__file__)))
parser.add_argument("--base")
args = parser.parse_args()
ROOT = os.path.abspath(args.root)
errors = []


def read(root, path):
    return open(os.path.join(root, path), encoding="utf-8").read()


def source_pages(root):
    found = []
    for dirpath, _, files in os.walk(os.path.join(root, "source")):
        found += [os.path.relpath(os.path.join(dirpath, f), root) for f in files if f.endswith(".md")]
    return sorted(found)


def credits(root, source_path):
    """(author, [co-authors]) from a page header."""
    header = re.match(r"^---\n(.*?)\n---\n", read(root, source_path), re.S)
    values = {}
    for key in ("author", "coauthors"):
        found = re.search(rf"^{key}:(.*)$", header.group(1), re.M) if header else None
        values[key] = [n.strip().strip('"') for n in found.group(1).split(",") if n.strip().strip('"')] if found else []
    author = values["author"][0] if values["author"] else ""
    return author, values["author"][1:] + values["coauthors"]


# The wiki as a whole keeps its original author credit.
if read(ROOT, "AUTHORS").splitlines()[0].strip() != f"Original author: {ORIGINAL_AUTHOR}":
    errors.append('AUTHORS: first line must be "Original author: ' + ORIGINAL_AUTHOR + '"')
for path in ("README.md", "CONTRIBUTING.md"):
    if f"**{ORIGINAL_AUTHOR}**" not in read(ROOT, path):
        errors.append(f"{path}: original author credit missing")

# Every page: has a named author, and the published HTML shows the same names.
pages = source_pages(ROOT)
for source_path in pages:
    author, coauthors = credits(ROOT, source_path)
    if not author:
        errors.append(f"{source_path}: add an 'author:' line to the page header")
        continue
    names = [author] + coauthors
    html_path = os.path.relpath(source_path, "source")[:-3] + ".html"
    if not os.path.exists(os.path.join(ROOT, html_path)):
        errors.append(f"{html_path}: page has not been built (run build.py)")
        continue
    page = read(ROOT, html_path)
    label = ("Authors: " if len(names) > 1 else "Author: ") + ", ".join(names)
    if f'<meta name="author" content="{", ".join(names)}">' not in page or label not in page:
        errors.append(f"{html_path}: author shown does not match {source_path} (run build.py)")

# Against main: nobody's existing credit may be removed or replaced.
protected = 0
if args.base:
    BASE = os.path.abspath(args.base)
    base_authors_line = read(BASE, "AUTHORS").splitlines()
    kept = set(read(ROOT, "AUTHORS").splitlines())
    for line in base_authors_line:
        if line.strip() and line not in kept:
            errors.append(f"AUTHORS: existing line was removed or changed: {line.strip()!r}")
    for source_path in source_pages(BASE):
        base_author, base_co = credits(BASE, source_path)
        if not base_author:
            continue
        protected += 1
        if not os.path.exists(os.path.join(ROOT, source_path)):
            errors.append(f"{source_path}: page credited to {base_author} was removed or renamed")
            continue
        author, coauthors = credits(ROOT, source_path)
        if author != base_author:
            errors.append(f"{source_path}: author must stay {base_author} (found {author or 'none'}); add yourself under 'coauthors:' instead")
        for name in base_co:
            if name not in coauthors:
                errors.append(f"{source_path}: co-author {name} was removed")

if errors:
    print("Author check FAILED:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print(f"Author check passed ({len(pages)} pages" + (f", {protected} existing credits verified against main)." if args.base else ")."))
