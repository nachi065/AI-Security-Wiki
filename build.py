#!/usr/bin/env python3
"""Build the static HTML site from the Markdown files in source/.

Usage:  pip install markdown && python3 build.py
"""
import html, json, os, re
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "source")
SITE_TITLE = "AI Security Wiki"
REPO_URL = "https://github.com/nachi065/AI-Security-Wiki"


def read(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2)


# Collect pages: (output path relative to site root, meta, markdown body)
pages = []
for dirpath, dirs, files in os.walk(SRC):
    dirs.sort()
    for f in sorted(files):
        if f.endswith(".md"):
            rel = os.path.relpath(os.path.join(dirpath, f), SRC)
            meta, body = read(os.path.join(dirpath, f))
            pages.append({"src": rel, "out": rel[:-3] + ".html", "meta": meta, "body": body})

home = next(p for p in pages if p["src"] == "index.md")
sections = sorted((p for p in pages if p["meta"].get("has_children")), key=lambda p: int(p["meta"]["nav_order"]))
for s in sections:
    s["children"] = sorted(
        (p for p in pages if p["meta"].get("parent") == s["meta"]["title"]),
        key=lambda p: int(p["meta"]["nav_order"]),
    )


def rel(from_out, to_out):
    return os.path.relpath(to_out, os.path.dirname(from_out) or ".").replace(os.sep, "/")


def nav(page):
    out = ['<ul class="nav">']
    cur = ' class="current"' if page is home else ""
    out.append(f'<li><a{cur} href="{rel(page["out"], home["out"])}">Home</a></li>')
    for s in sections:
        active = page is s or page in s["children"]
        cur = ' class="current"' if page is s else ""
        out.append(f'<li><details{" open" if active else ""}><summary><a{cur} href="{rel(page["out"], s["out"])}">'
                   f'{html.escape(s["meta"]["title"])}</a></summary><ul>')
        for c in s["children"]:
            cur = ' class="current"' if page is c else ""
            out.append(f'<li><a{cur} href="{rel(page["out"], c["out"])}">{html.escape(c["meta"]["title"])}</a></li>')
        out.append("</ul></details></li>")
    out.append("</ul>")
    return "\n".join(out)


def render(page):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc"])
    body = page["body"]
    if page.get("children"):
        body += "\n## Pages in this section\n\n" + "\n".join(
            f'- [{c["meta"]["title"]}]({os.path.basename(c["src"])})' for c in page["children"]) + "\n"
    content = md.convert(body)
    # Point links at the generated .html pages and make wide tables scrollable.
    content = re.sub(r'href="(?!https?:|#|mailto:)([^"#]+)\.md(#[^"]*)?"', lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', content)
    content = content.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    content = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener"', content)
    return content


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="A vendor-neutral reference for AI security governance, risk management, engineering standards, vendor evaluation and assurance.">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
<header class="topbar">
  <button class="menu-btn" id="menu-btn" aria-label="Toggle navigation" aria-expanded="false">&#9776;</button>
  <a class="brand" href="{base}index.html">{site}</a>
  <div class="search">
    <input id="search-input" type="search" placeholder="Search the wiki" aria-label="Search the wiki" autocomplete="off">
    <ul id="search-results" hidden></ul>
  </div>
  <a class="repo-link" href="{repo}" rel="noopener">GitHub</a>
</header>
<div class="layout">
<nav class="sidebar" id="sidebar" aria-label="Wiki sections">
{nav}
</nav>
<main>
{crumbs}
<article>
{content}
</article>
{pager}
</main>
</div>
<script>window.SITE_BASE = "{base}";</script>
<script src="{base}assets/search-index.js"></script>
<script src="{base}assets/site.js"></script>
</body>
</html>
"""

order = [home] + [p for s in sections for p in [s] + s["children"]]
index = []
for i, page in enumerate(order):
    base = rel(page["out"], "x")[:-1]  # "" at the root, "../" one level down
    title = page["meta"]["title"]
    crumbs = ""
    parent = next((s for s in sections if page in s["children"]), None)
    if page is not home:
        trail = [f'<a href="{rel(page["out"], home["out"])}">Home</a>']
        if parent:
            trail.append(f'<a href="{rel(page["out"], parent["out"])}">{html.escape(parent["meta"]["title"])}</a>')
        trail.append(f"<span>{html.escape(title)}</span>")
        crumbs = '<p class="crumbs">' + " / ".join(trail) + "</p>"
    links = []
    if i > 0:
        links.append(f'<a class="prev" href="{rel(page["out"], order[i-1]["out"])}">&larr; {html.escape(order[i-1]["meta"]["title"])}</a>')
    if i < len(order) - 1:
        links.append(f'<a class="next" href="{rel(page["out"], order[i+1]["out"])}">{html.escape(order[i+1]["meta"]["title"])} &rarr;</a>')
    content = render(page)
    doc = TEMPLATE.format(
        title=html.escape(SITE_TITLE if page is home else f"{title} | {SITE_TITLE}"),
        site=SITE_TITLE, repo=REPO_URL, base=base, nav=nav(page), crumbs=crumbs,
        content=content, pager='<nav class="pager" aria-label="Previous and next page">' + "".join(links) + "</nav>",
    )
    dest = os.path.join(ROOT, page["out"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(doc)
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", content))).strip()
    index.append({"t": title, "s": parent["meta"]["title"] if parent else "", "u": page["out"], "c": text})

open(os.path.join(ROOT, "assets", "search-index.js"), "w", encoding="utf-8").write(
    "window.SEARCH_INDEX = " + json.dumps(index, ensure_ascii=False) + ";\n")
print(f"Built {len(order)} pages")
