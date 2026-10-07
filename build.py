#!/usr/bin/env python3
"""Build the static HTML site from the Markdown files in source/.

Usage:  pip install markdown && python3 build.py
"""
import html, json, os, re, shutil
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "source")
SITE_TITLE = "AI Security Wiki"
REPO_URL = "https://github.com/nachi065/AI-Security-Wiki"
SITE_URL = "https://nachi065.github.io/AI-Security-Wiki"
HOME_TITLE = "AI Security Wiki: Governance, Risk, Standards and Test Cases"


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
# Top-level entries in the sidebar: sections (which have child pages) and standalone pages.
sections = sorted((p for p in pages if p is not home and not p["meta"].get("parent")), key=lambda p: int(p["meta"]["nav_order"]))
for s in sections:
    s["children"] = sorted(
        (p for p in pages if p["meta"].get("parent") == s["meta"]["title"]),
        key=lambda p: int(p["meta"]["nav_order"]),
    )


# Visual identity: each section has a hue (used as its accent colour) and an icon; its pages inherit both.
LOOKS = {
    "00_Foundations": (255, '<path d="M3 5h7a2 2 0 0 1 2 2v12a2 2 0 0 0-2-2H3zM21 5h-7a2 2 0 0 0-2 2v12a2 2 0 0 1 2-2h7z"/>'),
    "01_Strategy_and_Market": (205, '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>'),
    "02_Risk_Management": (8, '<path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17v.5"/>'),
    "03_Control_Library": (165, '<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>'),
    "04_Domain_Standards": (280, '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 12l9 5 9-5M3 16l9 5 9-5"/>'),
    "05_Vendor_Evaluation": (32, '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>'),
    "06_Testing_and_Assurance": (325, '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M7.5 15h9"/>'),
    "07_Role_Based_Playbooks": (188, '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2c2.8.3 5 2.7 5 5.8"/>'),
    "08_Governance": (228, '<path d="M3 9l9-5 9 5M5 9v9M9.5 9v9M14.5 9v9M19 9v9M3 20h18"/>'),
    "09_Reference": (215, '<path d="M6 3h12v18l-6-4-6 4z"/>'),
    "11_GCC_AI_Compliance": (60, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "12_EU_AI_Compliance": (100, '<circle cx="12" cy="12" r="9"/><path d="M12 6.5v.5M12 17v.5M6.5 12h.5M17 12h.5M8.1 8.1l.4.4M15.5 15.5l.4.4M15.9 8.1l-.4.4M8.5 15.5l-.4.4"/>'),
    "13_Australia_AI_Compliance": (45, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "14_Brazil_AI_Compliance": (130, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "15_Canada_AI_Compliance": (355, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "16_China_AI_Compliance": (20, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "17_India_AI_Compliance": (80, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "18_Japan_AI_Compliance": (340, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "19_Singapore_AI_Compliance": (175, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "20_South_Korea_AI_Compliance": (240, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "21_UK_AI_Compliance": (265, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "10_Test_Case_Library": (145, '<path d="M4 6l1.5 1.5L8 5M4 12l1.5 1.5L8 11M4 18l1.5 1.5L8 17M11 6h9M11 12h9M11 18h9"/>'),
}
DEFAULT_LOOK = (215, '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>')


def look(page):
    """(hue, icon) of the section a page belongs to."""
    return LOOKS.get(page["src"].split(os.sep)[0], DEFAULT_LOOK)


def icon(page):
    return ('<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{look(page)[1]}</svg>')


def rel(from_out, to_out):
    return os.path.relpath(to_out, os.path.dirname(from_out) or ".").replace(os.sep, "/")


def nav(page):
    out = ['<ul class="nav">']
    cur = ' class="current"' if page is home else ""
    out.append(f'<li><a{cur} href="{rel(page["out"], home["out"])}">Home</a></li>')
    for s in sections:
        active = page is s or page in s["children"]
        cur = ' class="current"' if page is s else ""
        if not s["children"]:
            out.append(f'<li><a{cur} href="{rel(page["out"], s["out"])}">{html.escape(s["meta"]["title"])}</a></li>')
            continue
        out.append(f'<li style="--h:{look(s)[0]}"><details{" open" if active else ""}><summary><a{cur} href="{rel(page["out"], s["out"])}">'
                   f'{icon(s)}{html.escape(s["meta"]["title"])}</a></summary><ul>')
        for c in s["children"]:
            cur = ' class="current"' if page is c else ""
            out.append(f'<li><a{cur} href="{rel(page["out"], c["out"])}">{html.escape(c["meta"]["title"])}</a></li>')
        out.append("</ul></details></li>")
    out.append("</ul>")
    return "\n".join(out)


def render(page):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc"])
    content = md.convert(page["body"])
    if page.get("children"):
        content += '\n<h2 id="pages-in-this-section">Pages in this section</h2>\n' + cards(page, page["children"])
    # Point links at the generated .html pages and make wide tables scrollable.
    content = re.sub(r'href="(?!https?:|#|mailto:)([^"#]+)\.md(#[^"]*)?"', lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', content)
    content = content.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    content = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener"', content)
    return decorate(content)


def cards(page, targets):
    """A grid of link cards, one per target page, coloured by the target's section."""
    out = ['<div class="cards">']
    for c in targets:
        text = describe(c).removeprefix(c["meta"]["title"] + ": ")  # the card already shows the title
        n = len(c.get("children") or [])
        count = f'<span class="card-count">{n} page{"" if n == 1 else "s"}</span>' if n else ""
        out.append(f'<a class="card" style="--h:{look(c)[0]}" href="{rel(page["out"], c["out"])}">'
                   f'<span class="card-icon">{icon(c)}</span><span class="card-title">{html.escape(c["meta"]["title"])}</span>'
                   f'<span class="card-text">{html.escape(text[:1].upper() + text[1:])}</span>{count}</a>')
    out.append("</div>")
    return "\n".join(out)


CALLOUTS = {"note": ("Purpose", "Audience", "How to use", "How this relates", "Document type"),
            "caution": ("Verify before use", "Verification required", "Illustrative example", "Status"),
            "danger": ("Safety boundary",)}


def decorate(content):
    """Add the classes the stylesheet uses for severity badges, ID chips and callout boxes."""
    content = re.sub(r"<td>(Critical|High|Medium-High|Medium|Low)</td>",
                     lambda m: f'<td><span class="badge sev-{m.group(1).lower()}">{m.group(1)}</span></td>', content)
    content = re.sub(r"<td>(Technical|Evidence|Attestation)</td>",
                     lambda m: f'<td><span class="badge method">{m.group(1)}</span></td>', content)
    content = re.sub(r'<a (href="[^"]*")>((?:AI-CTRL-\d{3}|AI-R\d\d|TC-[LD]\d\d-\d{3}))</a>', r'<a class="chip" \1>\2</a>', content)
    for kind, labels in CALLOUTS.items():
        content = re.sub(r"<blockquote>(\s*<p><strong>(?:" + "|".join(labels) + "))", rf'<blockquote class="callout {kind}">\1', content)
    return content


def hero(page, details=""):
    """The banner on the home page: headline, live counts, the document details and a card for every section."""
    text = "\n".join(p["body"] for p in pages)
    stats = [(len(re.findall(r"^### TC-[LD]\d\d-\d{3}:", text, re.M)), "test cases"),
             (len(re.findall(r"^#### AI-CTRL-\d{3}:", text, re.M)), "control objectives"),
             (len(re.findall(r"^### AI-R\d\d: ", text, re.M)), "register risks"),
             (len(pages), "pages")]
    tiles = "".join(f'<div class="stat"><b>{n}</b><span>{html.escape(label)}</span></div>' for n, label in stats)
    return (f'<section class="hero"><p class="hero-kicker">Open &middot; Vendor-neutral &middot; CC BY 4.0</p>'
            f'<h1>{SITE_TITLE}</h1><p class="hero-lead">{html.escape(page["meta"]["description"])}</p>'
            f'<div class="stats">{tiles}</div></section>\n'
            + (f'<article class="hero-details">{details}</article>\n' if details else "") +
            f'<h2 class="hero-sections">Explore the wiki</h2>\n{cards(page, sections)}')


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
    focus = re.search(r"^\*\*(?:Primary test focus|Focus):\*\* (.+)$", body, re.M)
    count = re.search(r"^\*\*Cases:\*\* (\d+)", body, re.M)
    if focus and count:
        scope = focus.group(1).split(": ", 1)[-1] if title.startswith("D") else focus.group(1)
        lead = f"{count.group(1)} AI security test cases for {'' if title.startswith('D') else 'the '}{title[4:]}: {scope}."
        full = lead + " Each with procedure, expected results and pass criteria."
        return full if len(full) <= 158 else shorten(lead)
    if title.startswith("Vendor Profile"):
        vendor = title.split(":", 1)[1].strip()
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
<body style="--h:{hue}">
<header class="topbar">
  <button class="menu-btn" id="menu-btn" aria-label="Toggle navigation" aria-expanded="false">&#9776;</button>
  <a class="brand" href="{base}index.html"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/></svg>{site}</a>
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
{hero}<article>
{content}
</article>
{pager}
<footer class="site-footer">{byline} &middot; <a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener license">CC BY 4.0</a> &middot; <a href="{repo}/edit/main/source/{src}" rel="noopener">Suggest an edit to this page</a> &middot; <a href="{base}community-rules.html">Community rules</a> &middot; <a href="{repo}/blob/main/CONTRIBUTING.md" rel="noopener">How to contribute</a>
{notice}</footer>
</main>
</div>
<script>window.SITE_BASE = "{base}";</script>
<script src="{base}assets/search-index.js"></script>
<script src="{base}assets/site.js"></script>
</body>
</html>
"""

# Shown in the footer of every page.
NOTICE = """<div class="site-notice">
<p><strong>Disclaimer.</strong> This wiki is an open, community driven educational reference, not legal, regulatory or professional advice. Regional regulatory content is compiled from secondary sources and its verification status is shown per row; verify against primary sources before relying on it. Content is provided "as is" without warranty. Named products and companies belong to their owners; statements about them reflect public information at the date shown. Views are the author's own.</p>
<p><strong>Privacy.</strong> This site does not use cookies or analytics and collects no personal data itself. It is hosted on GitHub Pages; GitHub may process technical data such as IP addresses under its own <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">privacy statement</a>. If you contribute through GitHub, your contribution and username are public under GitHub's terms.</p>
</div>
"""


def authors(page):
    """The page's author followed by any co-authors, from its front matter."""
    names = [page["meta"].get("author", "")] + page["meta"].get("coauthors", "").split(",")
    names = [n.strip() for n in names if n.strip()]
    if not names:
        raise SystemExit(f"{page['src']}: add an 'author:' line to the page header")
    return names


def byline(page):
    names = authors(page)
    return ("Authors: " if len(names) > 1 else "Author: ") + html.escape(", ".join(names))


def canonical(page):
    out = page["out"].replace(os.sep, "/")
    if out == "index.html" or out.endswith("/index.html"):
        out = out[:-len("index.html")]
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
    banner = ""
    if page is home:
        content = re.sub(r"<h1[^>]*>.*?</h1>", "", content, count=1, flags=re.S)
        # The document details box that opens the page is shown above the section cards.
        details = re.match(r"\s*(<blockquote.*?</blockquote>)\s*", content, re.S)
        if details:
            content = content[details.end():]
        banner = hero(page, details.group(1) if details else "")
    doc = TEMPLATE.format(
        hue=look(page)[0], hero=banner,
        title=html.escape(HOME_TITLE if page is home else f"{title} | {SITE_TITLE}"),
        description=html.escape(describe(page), quote=True), canonical=canonical(page),
        og_type="website" if page is home else "article",
        site=SITE_TITLE, repo=REPO_URL, author=html.escape(", ".join(authors(page)), quote=True), byline=byline(page), src=page["src"].replace(os.sep, "/"), base=base, nav=nav(page), crumbs=crumbs, notice=NOTICE,
        content=content, pager='<nav class="pager" aria-label="Previous and next page">' + "".join(links) + "</nav>",
    )
    dest = os.path.join(ROOT, page["out"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(doc)
    section = parent["meta"]["title"] if parent else ""
    cases = re.split(r'<a id="(tc-[ld]\d\d-\d{3})"></a>', content)
    # A test case layer page is indexed as its intro plus one entry per case.
    index.append({"t": title, "s": section, "u": page["out"], "c": plain(cases[0])})
    for anchor, chunk in zip(cases[1::2], cases[2::2]):
        heading = re.search(r"<h3[^>]*>(.*?)</h3>", chunk, re.S)
        body = plain(chunk.split("</table></div>", 1)[-1])
        index.append({"t": plain(heading.group(1)) if heading else anchor.upper(), "s": title,
                      "u": page["out"] + "#" + anchor, "c": body[:CASE_SNIPPET]})

# Data files that pages link to (for example CSV downloads) are copied next to the generated pages.
for dirpath, dirs, files in os.walk(SRC):
    for f in files:
        if not f.endswith(".md") and not f.startswith("."):
            dest = os.path.join(ROOT, os.path.relpath(os.path.join(dirpath, f), SRC))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copyfile(os.path.join(dirpath, f), dest)

open(os.path.join(ROOT, "assets", "search-index.js"), "w", encoding="utf-8").write(
    "window.SEARCH_INDEX = " + json.dumps(index, ensure_ascii=False) + ";\n")
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{canonical(p)}</loc></url>\n" for p in order) + "</urlset>\n")
print(f"Built {len(order)} pages")
