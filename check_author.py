#!/usr/bin/env python3
"""Fail if the original author credit has been changed or removed anywhere."""
import os
import re
import sys

AUTHOR = "Nachiket Sathaye"
ROOT = os.path.dirname(os.path.abspath(__file__))
errors = []


def text(path):
    return open(os.path.join(ROOT, path), encoding="utf-8").read()


def require(path, needle, what):
    if needle not in text(path):
        errors.append(f"{path}: {what}")


if text("AUTHORS").splitlines()[0].strip() != f"Original author: {AUTHOR}":
    errors.append('AUTHORS: first line must be "Original author: ' + AUTHOR + '"')
require("build.py", f'ORIGINAL_AUTHOR = "{AUTHOR}"', "ORIGINAL_AUTHOR was changed")
require("README.md", f"Original author: **{AUTHOR}**", "original author credit missing")
require("CONTRIBUTING.md", f"**{AUTHOR}**", "original author credit missing")
home = text("source/index.md")
for needle, what in [
    (f"\nauthor: {AUTHOR}\n", "author field in the page header"),
    (f"> **Original author:** {AUTHOR}", "original author line under the title"),
    (f"| Original author | {AUTHOR} |", "original author row in Document Governance"),
    (f"| 1.0 | Initial release | {AUTHOR} |", "author of version 1.0 in Version History"),
]:
    if needle not in home:
        errors.append(f"source/index.md: missing or changed {what}")
if len(re.findall(r"(?im)^author:", home)) != 1:
    errors.append("source/index.md: there must be exactly one author field")

pages = 0
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in (".git", "source")]
    for name in files:
        if name.endswith(".html") and name != "404.html":
            pages += 1
            rel = os.path.relpath(os.path.join(dirpath, name), ROOT)
            page = text(rel)
            if f'<meta name="author" content="{AUTHOR}">' not in page:
                errors.append(f"{rel}: author meta tag missing or changed")
            if f"Original author: {AUTHOR}" not in page:
                errors.append(f"{rel}: original author footer missing or changed")

if errors:
    print("Original author check FAILED:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print(f"Original author check passed ({pages} pages).")
