#!/usr/bin/env python3
"""Link and identifier check.

Every relative link in the Markdown under source/ must point to a file that
exists, and to a heading or anchor that exists in it. Every risk, control and
test case identifier that a page cites must be defined, and none may be
defined twice.

Usage: python3 check_links.py [--root DIR] [--external]
  --root      the site to check (default: this folder)
  --external  also request every external URL and report the ones that no
              longer exist. Slow, and needs network access.
"""
import argparse
import collections
import os
import re
import sys
import urllib.error
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("--root", default=os.path.dirname(os.path.abspath(__file__)))
parser.add_argument("--external", action="store_true")
args = parser.parse_args()
SRC = os.path.join(os.path.abspath(args.root), "source")
errors = []

# Where each kind of identifier is defined: a heading such as "### TC-L07-001: Title".
IDS = {
    "risk": (r"AI-R\d{2}", "02_Risk_Management/02B_Enterprise_AI_Risk_Register.md"),
    "control": (r"AI-CTRL-\d{3}", "03_Control_Library/03_AI_Security_Control_Objectives_Library.md"),
    "test case": (r"TC-[LD]\d{2}-\d{3}", "10_Test_Case_Library/"),
}

pages = {}
for dirpath, _, files in os.walk(SRC):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(dirpath, f)
            pages[os.path.relpath(path, SRC).replace(os.sep, "/")] = open(path, encoding="utf-8").read()


def slug(heading):
    """The anchor build.py gives a heading."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def without_code(text):
    return re.sub(r"`[^`\n]*`", "", re.sub(r"^```.*?^```", "", text, flags=re.S | re.M))


anchors = {}
for path, text in pages.items():
    found = set(re.findall(r'<a id="([^"]+)"', text))
    seen = collections.Counter()
    for heading in re.findall(r"^#{1,6}\s+(.*?)\s*$", without_code(text), re.M):
        base = slug(heading)
        found.add(base if not seen[base] else f"{base}_{seen[base]}")
        seen[base] += 1
    anchors[path] = found

# Relative links and anchors.
external = collections.defaultdict(list)
for path, text in sorted(pages.items()):
    for target in re.findall(r"\]\(\s*<?([^)\s>]+)", without_code(text)):
        if re.match(r"https?:", target):
            external[target.rstrip(".,;")].append(path)
            continue
        if target.startswith("mailto:"):
            continue
        file, _, fragment = target.partition("#")
        dest = os.path.normpath(os.path.join(os.path.dirname(path), file)).replace(os.sep, "/") if file else path
        if not os.path.exists(os.path.join(SRC, dest)):
            errors.append(f"source/{path}: link to missing file {target}")
        elif fragment and dest in anchors and fragment not in anchors[dest]:
            errors.append(f"source/{path}: link to missing heading {target}")

# Identifiers.
counts = {}
for kind, (pattern, home) in IDS.items():
    defined = collections.Counter()
    for path, text in pages.items():
        if path.startswith(home):
            defined.update(re.findall(rf"^#+\s+({pattern}):", text, re.M))
    counts[kind] = len(defined)
    for name, times in sorted(defined.items()):
        if times > 1:
            errors.append(f"{name}: {kind} is defined {times} times")
    for path, text in sorted(pages.items()):
        for name in sorted(set(re.findall(rf"\b{pattern}\b", text)) - set(defined)):
            errors.append(f"source/{path}: cites {name}, but no such {kind} is defined")

# Standard fields. Wording that cases share lives in standard-fields.json; a case may
# show such a field only when its text differs from the standard.
import json
sf_path = os.path.join(SRC, "10_Test_Case_Library", "standard-fields.json")
if os.path.exists(sf_path):
    sf = json.load(open(sf_path, encoding="utf-8"))
    KEY = {"all": lambda l, m, k: "all", "shape": lambda l, m, k: k, "method-shape": lambda l, m, k: f"{m.lower()}-{k}", "layer": lambda l, m, k: l}
    for path, text in sorted(pages.items()):
        layer = re.match(r"10_Test_Case_Library/([LD]\d\d)-", path)
        if not layer:
            continue
        for block in re.split(r"(?m)^(?=### TC-[LD]\d\d-\d{3}:)", text)[1:]:
            name = block.split(":", 1)[0].replace("### ", "")
            method = re.search(r"\| \*\*Test Method\*\* \| ([^|]*) \|", block)
            if not method:
                errors.append(f"source/{path}: {name} has no Test Method")
                continue
            shape = "detect" if "**Expected Detection.**" in block else "result"
            for field, standards in sf["standards"].items():
                key = KEY[sf["keys"][field]](layer.group(1), method.group(1).strip(), shape)
                shown = re.search(rf"(?m)^\*\*{re.escape(field)}\.\*\* (.*)$", block)
                if shown and standards.get(key) == shown.group(1):
                    errors.append(f"source/{path}: {name} repeats the standard {field}; remove it (see Standard Fields)")

# Control tiers. Every control record states Baseline or Advanced, and the controls the
# Builder Track relies on must be Baseline.
_lib = open(os.path.join("source", "03_Control_Library", "03_AI_Security_Control_Objectives_Library.md"), encoding="utf-8").read()
_tier = {}
for _rec in re.split(r"^#### (?=AI-CTRL-\d{3}:)", _lib, flags=re.M)[1:]:
    _tm = re.search(r"^\| \*\*Tier\*\* \| (\w+) \|", _rec.split("\n#### ")[0], re.M)
    _tier[_rec[:11]] = _tm.group(1) if _tm else None
for _c, _t in _tier.items():
    if _t not in ("Baseline", "Advanced"):
        errors.append(f"source/03_Control_Library: {_c} has no valid Tier (Baseline or Advanced)")
_builder = open(os.path.join("source", "24_Builder_Track", "01_Secure_Your_First_Agent.md"), encoding="utf-8").read()
for _c in sorted(set(re.findall(r"AI-CTRL-\d{3}", _builder.split("## The ten controls at a glance")[1].split("Do the steps in order")[0]))):
    if _tier.get(_c) != "Baseline":
        errors.append(f"source/24_Builder_Track: {_c} is used by the Builder Track but is not Baseline")

# External URLs. Only a URL that is gone counts as an error: many sites refuse
# automated requests, and that says nothing about the page.
unchecked = []
if args.external:
    for url, cited_in in sorted(external.items()):
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (AI-Security-Wiki link check)"})
        try:
            urllib.request.urlopen(request, timeout=20).close()
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                errors.append(f"source/{cited_in[0]}: external link returns {e.code}: {url}")
            else:
                unchecked.append(f"{url} (HTTP {e.code})")
        except Exception as e:
            unchecked.append(f"{url} ({type(e).__name__})")
    if unchecked:
        print(f"Could not check {len(unchecked)} external links:")
        for u in unchecked:
            print("  - " + u)

if errors:
    print("Link check FAILED:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print(f"Link check passed ({len(pages)} pages, {counts['risk']} risks, {counts['control']} controls, "
      f"{counts['test case']} test cases" + (f", {len(external)} external links)." if args.external else ")."))
