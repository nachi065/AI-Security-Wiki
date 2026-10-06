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
SITE_URL = "https://nachi065.github.io/AI-Security-Wiki"
HOME_TITLE = "AI Security Wiki: Governance, Risk, Standards and Test Cases"
# The original author is fixed. check_author.py fails the build if this changes.
ORIGINAL_AUTHOR = "Nachiket Sathaye"


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


CASE_SNIPPET = 700  # characters of each test case kept in the search index


def plain(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def shorten(text, limit=158):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def describe(page):
    """Search-result description: explicit front matter first, then derived from the page itself."""
    meta, body, title = page["meta"], page["body"], page["meta"]["title"]
    if meta.get("description"):
        return meta["description"]
    focus = re.search(r"^\*\*Primary test focus:\*\* (.+)$", body, re.M)
    count = re.search(r"^\*\*Cases:\*\* (\d+)", body, re.M)
    if focus and count:
        lead = f"{count.group(1)} AI security test cases for the {title[4:]}: {focus.group(1)}."
        full = lead + " Each with procedure, expected results and pass criteria."
        return full if len(full) <= 158 else shorten(lead)
    if title.startswith("Vendor Profile"):
        vendor = title.split("—", 1)[1].strip()
        return shorten(f"{vendor} AI security vendor profile: best-fit use case, summary assessment, evaluation checklist and PoC evidence requirements.")
    purpose = re.search(r"^> \*\*Purpose:\*\* (.+)$", body, re.M)
    if purpose:
        return shorten(f"{title}: {purpose.group(1)}")
    first = next((p for p in re.split(r"\n\s*\n", body) if p.strip() and not p.lstrip().startswith(("#", ">", "|", "<"))), title)
    return shorten(re.sub(r"[*`\[\]]|\([^)]*\.md[^)]*\)", "", first))


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="author" content="{author}">
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
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
<footer class="site-footer">Original author: {author} &middot; <a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener license">CC BY 4.0</a> &middot; <a href="{repo}/edit/main/source/{src}" rel="noopener">Suggest an edit to this page</a> &middot; <a href="{repo}/blob/main/CONTRIBUTING.md" rel="noopener">How to contribute</a></footer>
</main>
</div>
<script>window.SITE_BASE = "{base}";</script>
<script src="{base}assets/search-index.js"></script>
<script src="{base}assets/site.js"></script>
</body>
</html>
"""

def canonical(page):
    out = page["out"].replace(os.sep, "/")
    out = out[:-len("index.html")] if out.endswith("index.html") else out
    return f"{SITE_URL}/{out}"


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
        title=html.escape(HOME_TITLE if page is home else f"{title} | {SITE_TITLE}"),
        description=html.escape(describe(page), quote=True), canonical=canonical(page),
        og_type="website" if page is home else "article",
        site=SITE_TITLE, repo=REPO_URL, author=ORIGINAL_AUTHOR, src=page["src"].replace(os.sep, "/"), base=base, nav=nav(page), crumbs=crumbs,
        content=content, pager='<nav class="pager" aria-label="Previous and next page">' + "".join(links) + "</nav>",
    )
    dest = os.path.join(ROOT, page["out"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(doc)
    section = parent["meta"]["title"] if parent else ""
    cases = re.split(r'<a id="(tc-l\d\d-\d{3})"></a>', content)
    # A test case layer page is indexed as its intro plus one entry per case.
    index.append({"t": title, "s": section, "u": page["out"], "c": plain(cases[0])})
    for anchor, chunk in zip(cases[1::2], cases[2::2]):
        heading = re.search(r"<h3[^>]*>(.*?)</h3>", chunk, re.S)
        body = plain(chunk.split("</table></div>", 1)[-1])
        index.append({"t": plain(heading.group(1)) if heading else anchor.upper(), "s": title,
                      "u": page["out"] + "#" + anchor, "c": body[:CASE_SNIPPET]})

open(os.path.join(ROOT, "assets", "search-index.js"), "w", encoding="utf-8").write(
    "window.SEARCH_INDEX = " + json.dumps(index, ensure_ascii=False) + ";\n")
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{canonical(p)}</loc></url>\n" for p in order) + "</urlset>\n")
print(f"Built {len(order)} pages")
