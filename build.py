#!/usr/bin/env python3
"""Build the static HTML site from the Markdown files in source/.

Usage:  pip install markdown && python3 build.py
"""
import datetime, hashlib, html, json, os, re, shutil, subprocess
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
    "12_EU_AI_Compliance": (225, '<circle cx="12" cy="12" r="9"/><path d="M12 6.5v.5M12 17v.5M6.5 12h.5M17 12h.5M8.1 8.1l.4.4M15.5 15.5l.4.4M15.9 8.1l-.4.4M8.5 15.5l-.4.4"/>'),
    "13_Australia_AI_Compliance": (195, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "14_Brazil_AI_Compliance": (135, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "15_Canada_AI_Compliance": (355, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "16_China_AI_Compliance": (25, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "17_India_AI_Compliance": (95, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "18_Japan_AI_Compliance": (335, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "19_Singapore_AI_Compliance": (172, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "20_South_Korea_AI_Compliance": (250, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "21_UK_AI_Compliance": (278, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "22_US_AI_Compliance": (310, '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
    "23_Framework_Crosswalks": (120, '<path d="M4 8h14l-3-3M20 16H6l3 3"/>'),
    "10_Test_Case_Library": (145, '<path d="M4 6l1.5 1.5L8 5M4 12l1.5 1.5L8 11M4 18l1.5 1.5L8 17M11 6h9M11 12h9M11 18h9"/>'),
}
DEFAULT_LOOK = (215, '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>')


# Country sections show a small flag in place of the line icon. Each flag is drawn on a 20 by 14 canvas.
FLAGS = {
    "12_EU_AI_Compliance": '<rect width="20" height="14" fill="#003399"/><circle cx="14.3" cy="7" r=".75" fill="#ffcc00"/><circle cx="13.72" cy="9.15" r=".75" fill="#ffcc00"/><circle cx="12.15" cy="10.72" r=".75" fill="#ffcc00"/><circle cx="10" cy="11.3" r=".75" fill="#ffcc00"/><circle cx="7.85" cy="10.72" r=".75" fill="#ffcc00"/><circle cx="6.28" cy="9.15" r=".75" fill="#ffcc00"/><circle cx="5.7" cy="7" r=".75" fill="#ffcc00"/><circle cx="6.28" cy="4.85" r=".75" fill="#ffcc00"/><circle cx="7.85" cy="3.28" r=".75" fill="#ffcc00"/><circle cx="10" cy="2.7" r=".75" fill="#ffcc00"/><circle cx="12.15" cy="3.28" r=".75" fill="#ffcc00"/><circle cx="13.72" cy="4.85" r=".75" fill="#ffcc00"/>',
    "13_Australia_AI_Compliance": '<rect width="20" height="14" fill="#012169"/><path d="M0 3.5h10M5 0v7" stroke="#fff" stroke-width="1.9"/><path d="M0 3.5h10M5 0v7" stroke="#e4002b" stroke-width=".9"/><circle cx="5" cy="10.5" r="1.3" fill="#fff"/><circle cx="15" cy="3" r=".8" fill="#fff"/><circle cx="17.5" cy="5.5" r=".8" fill="#fff"/><circle cx="15" cy="10.5" r=".8" fill="#fff"/><circle cx="12.8" cy="6.5" r=".8" fill="#fff"/><circle cx="16.2" cy="7.6" r=".5" fill="#fff"/>',
    "14_Brazil_AI_Compliance": '<rect width="20" height="14" fill="#009739"/><path d="M10 1.6L18.2 7 10 12.4 1.8 7z" fill="#fedd00"/><circle cx="10" cy="7" r="3" fill="#012169"/>',
    "15_Canada_AI_Compliance": '<rect width="20" height="14" fill="#fff"/><path d="M0 0h5v14H0zM15 0h5v14h-5z" fill="#d80621"/><path d="M10 2.5l1 2.1 1.6-.6-.5 2.2 1.7.4-1.6 1.6.4 1-2.2-.3v2.4h-.8V8.9l-2.2.3.4-1-1.6-1.6 1.7-.4L7.4 4l1.6.6z" fill="#d80621"/>',
    "16_China_AI_Compliance": '<rect width="20" height="14" fill="#de2910"/><polygon points="4.5,2 5.09,3.69 6.88,3.73 5.45,4.81 5.97,6.52 4.5,5.5 3.03,6.52 3.55,4.81 2.12,3.73 3.91,3.69" fill="#ffde00"/><circle cx="8.2" cy="1.9" r=".55" fill="#ffde00"/><circle cx="9.6" cy="3.4" r=".55" fill="#ffde00"/><circle cx="9.6" cy="5.4" r=".55" fill="#ffde00"/><circle cx="8.2" cy="6.9" r=".55" fill="#ffde00"/>',
    "17_India_AI_Compliance": '<rect width="20" height="14" fill="#fff"/><rect width="20" height="4.67" fill="#ff9933"/><rect y="9.33" width="20" height="4.67" fill="#138808"/><circle cx="10" cy="7" r="1.7" fill="none" stroke="#000080" stroke-width=".5"/><circle cx="10" cy="7" r=".4" fill="#000080"/>',
    "18_Japan_AI_Compliance": '<rect width="20" height="14" fill="#fff"/><circle cx="10" cy="7" r="4.1" fill="#bc002d"/>',
    "19_Singapore_AI_Compliance": '<rect width="20" height="14" fill="#fff"/><rect width="20" height="7" fill="#ed2939"/><circle cx="4.8" cy="3.5" r="2.2" fill="#fff"/><circle cx="5.7" cy="3.5" r="2.2" fill="#ed2939"/><circle cx="7.9" cy="2.1" r=".42" fill="#fff"/><circle cx="6.9" cy="2.9" r=".42" fill="#fff"/><circle cx="8.9" cy="2.9" r=".42" fill="#fff"/><circle cx="7.3" cy="4.1" r=".42" fill="#fff"/><circle cx="8.5" cy="4.1" r=".42" fill="#fff"/>',
    "20_South_Korea_AI_Compliance": '<rect width="20" height="14" fill="#fff"/><path d="M6.5 7a3.5 3.5 0 0 1 7 0z" fill="#cd2e3a"/><path d="M6.5 7a3.5 3.5 0 0 0 7 0z" fill="#0047a0"/><path d="M2.2 3.6l2.2-2.2M3 4.4l2.2-2.2M3.8 5.2L6 3M14 11l2.2-2.2M14.8 11.8l2.2-2.2M15.6 12.6l2.2-2.2M15.6 1.4l2.2 2.2M14.8 2.2l2.2 2.2M14 3l2.2 2.2M2.2 10.4l2.2 2.2M3 9.6l2.2 2.2M3.8 8.8L6 11" stroke="#000" stroke-width=".7"/>',
    "21_UK_AI_Compliance": '<rect width="20" height="14" fill="#012169"/><path d="M0 0l20 14M20 0L0 14" stroke="#fff" stroke-width="2.8"/><path d="M0 0l20 14M20 0L0 14" stroke="#c8102e" stroke-width="1"/><path d="M10 0v14M0 7h20" stroke="#fff" stroke-width="4.4"/><path d="M10 0v14M0 7h20" stroke="#c8102e" stroke-width="2.6"/>',
    "22_US_AI_Compliance": '<rect width="20" height="14" fill="#fff"/><rect y="0" width="20" height="1.08" fill="#b22234"/><rect y="2.15" width="20" height="1.08" fill="#b22234"/><rect y="4.31" width="20" height="1.08" fill="#b22234"/><rect y="6.46" width="20" height="1.08" fill="#b22234"/><rect y="8.62" width="20" height="1.08" fill="#b22234"/><rect y="10.77" width="20" height="1.08" fill="#b22234"/><rect y="12.92" width="20" height="1.08" fill="#b22234"/><rect width="8.5" height="7.54" fill="#3c3b6e"/><circle cx="1.4" cy="1.3" r=".35" fill="#fff"/><circle cx="3.3" cy="1.3" r=".35" fill="#fff"/><circle cx="5.2" cy="1.3" r=".35" fill="#fff"/><circle cx="7.1" cy="1.3" r=".35" fill="#fff"/><circle cx="1.4" cy="2.95" r=".35" fill="#fff"/><circle cx="3.3" cy="2.95" r=".35" fill="#fff"/><circle cx="5.2" cy="2.95" r=".35" fill="#fff"/><circle cx="7.1" cy="2.95" r=".35" fill="#fff"/><circle cx="1.4" cy="4.6" r=".35" fill="#fff"/><circle cx="3.3" cy="4.6" r=".35" fill="#fff"/><circle cx="5.2" cy="4.6" r=".35" fill="#fff"/><circle cx="7.1" cy="4.6" r=".35" fill="#fff"/><circle cx="1.4" cy="6.25" r=".35" fill="#fff"/><circle cx="3.3" cy="6.25" r=".35" fill="#fff"/><circle cx="5.2" cy="6.25" r=".35" fill="#fff"/><circle cx="7.1" cy="6.25" r=".35" fill="#fff"/>',
}


def look(page):
    """(hue, icon) of the section a page belongs to."""
    return LOOKS.get(page["src"].split(os.sep)[0], DEFAULT_LOOK)


# Sections whose icon is an image in assets/, drawn by the stylesheet class named here.
EMBLEMS = {"11_GCC_AI_Compliance": "emblem-gcc"}


def line_icon(shape):
    return ('<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{shape}</svg>')


def icon(page):
    folder = page["src"].split(os.sep)[0]
    if folder in EMBLEMS:
        return f'<span class="icon {EMBLEMS[folder]}" aria-hidden="true"></span>'
    flag = FLAGS.get(folder)
    if flag:
        return ('<svg class="icon flag" viewBox="0 0 24 24" aria-hidden="true"><svg x="2" y="5" width="20" height="14" viewBox="0 0 20 14">'
                f'{flag}</svg><rect x="2" y="5" width="20" height="14" fill="none" stroke="#000" stroke-opacity=".3" stroke-width=".6"/></svg>')
    return line_icon(look(page)[1])


def version(asset):
    """Short content hash of a file in assets/, added to its link so that a change reaches browsers that cached the old file."""
    return hashlib.md5(open(os.path.join(ROOT, "assets", asset), "rb").read().replace(b"\r\n", b"\n")).hexdigest()[:8]


def rel(from_out, to_out):
    return os.path.relpath(to_out, os.path.dirname(from_out) or ".").replace(os.sep, "/")


def nav(page):
    out = ['<ul class="nav">']
    cur = ' class="current"' if page is home else ""
    out.append(f'<li><a{cur} href="{rel(page["out"], home["out"])}">Home</a></li>')
    group = None  # sections that share a 'group:' in their header are nested under one sidebar entry
    for s in sections:
        active = page is s or page in s["children"]
        cur = ' class="current"' if page is s else ""
        name = s["meta"].get("group")
        if name != group:
            if group:
                out.append("</ul></details></li>")
            if name:
                inside = any(page is m or page in m["children"] for m in sections if m["meta"].get("group") == name)
                out.append(f'<li><details{" open" if inside else ""}><summary><span class="nav-group">{line_icon(look(s)[1])}{html.escape(name)}</span></summary><ul>')
            group = name
        if not s["children"]:
            out.append(f'<li><a{cur} href="{rel(page["out"], s["out"])}">{html.escape(s["meta"]["title"])}</a></li>')
            continue
        out.append(f'<li style="--h:{look(s)[0]}"><details{" open" if active else ""}><summary><a{cur} href="{rel(page["out"], s["out"])}">'
                   f'{icon(s)}{html.escape(s["meta"]["title"])}</a></summary><ul>')
        for c in s["children"]:
            cur = ' class="current"' if page is c else ""
            out.append(f'<li><a{cur} href="{rel(page["out"], c["out"])}">{html.escape(c["meta"]["title"])}</a></li>')
        out.append("</ul></details></li>")
    if group:
        out.append("</ul></details></li>")
    out.append("</ul>")
    return "\n".join(out)


def render(page):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc"])
    content = md.convert(page["body"])
    if page.get("children"):
        content += '\n<h2 id="pages-in-this-section">Pages in This Section</h2>\n' + cards(page, page["children"])
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
        count = f'<span class="card-count">{n} Page{"" if n == 1 else "s"}</span>' if n else ""
        out.append(f'<a class="card" style="--h:{look(c)[0]}" href="{rel(page["out"], c["out"])}">'
                   f'<span class="card-icon">{icon(c)}</span><span class="card-title">{html.escape(c["meta"]["title"])}</span>'
                   f'<span class="card-text">{html.escape(text[:1].upper() + text[1:])}</span>{count}</a>')
    out.append("</div>")
    return "\n".join(out)


CALLOUTS = {"note": ("Purpose", "Audience", "How to use", "How this relates", "Document type", "Document Type"),
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
    stats = [(len(re.findall(r"^### TC-[LD]\d\d-\d{3}:", text, re.M)), "Test Cases"),
             (len(re.findall(r"^#### AI-CTRL-\d{3}:", text, re.M)), "Control Objectives"),
             (len(re.findall(r"^### AI-R\d\d: ", text, re.M)), "Register Risks"),
             (sum(1 for s in sections if s["meta"].get("group")), "Regional Sections"),
             (len(pages), "Pages")]
    tiles = "".join(f'<div class="stat"><b>{n}</b><span>{html.escape(label)}</span></div>' for n, label in stats)
    return (f'<section class="hero"><p class="hero-kicker">Open &middot; Vendor-neutral &middot; {LICENCE_LINK}</p>'
            f'<h1>{SITE_TITLE}</h1><p class="hero-lead">{html.escape(page["meta"]["description"])}</p>'
            f'<div class="stats">{tiles}</div></section>\n'
            + (f'<article class="hero-details">{details}</article>\n' if details else "") +
            f'<h2 class="hero-sections">Explore the Wiki</h2>\n{cards(page, sections)}')


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
<link rel="stylesheet" href="{base}assets/style.css?v={css_v}">
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
<script src="{base}assets/site.js?v={js_v}"></script>
</body>
</html>
"""

# The Creative Commons and Attribution marks, drawn in the surrounding text colour.
CC_MARK = ('<svg class="cc-icon" viewBox="5.5 -3.5 64 64" aria-hidden="true"><path d="M37.441-3.5c8.951,0,16.572,3.125,22.857,9.372c3.008,3.009,5.295,6.448,6.857,10.314 c1.561,3.867,2.344,7.971,2.344,12.314c0,4.381-0.773,8.486-2.314,12.313c-1.543,3.828-3.82,7.21-6.828,10.143 c-3.123,3.085-6.666,5.448-10.629,7.086c-3.961,1.638-8.057,2.457-12.285,2.457s-8.276-0.808-12.143-2.429 c-3.866-1.618-7.333-3.961-10.4-7.027c-3.067-3.066-5.4-6.524-7-10.372S5.5,32.767,5.5,28.5c0-4.229,0.809-8.295,2.428-12.2 c1.619-3.905,3.972-7.4,7.057-10.486C21.08-0.394,28.565-3.5,37.441-3.5z M37.557,2.272c-7.314,0-13.467,2.553-18.458,7.657 c-2.515,2.553-4.448,5.419-5.8,8.6c-1.354,3.181-2.029,6.505-2.029,9.972c0,3.429,0.675,6.734,2.029,9.913 c1.353,3.183,3.285,6.021,5.8,8.516c2.514,2.496,5.351,4.399,8.515,5.715c3.161,1.314,6.476,1.971,9.943,1.971 c3.428,0,6.75-0.665,9.973-1.999c3.219-1.335,6.121-3.257,8.713-5.771c4.99-4.876,7.484-10.99,7.484-18.344 c0-3.543-0.648-6.895-1.943-10.057c-1.293-3.162-3.18-5.98-5.654-8.458C50.984,4.844,44.795,2.272,37.557,2.272z M37.156,23.187 l-4.287,2.229c-0.458-0.951-1.019-1.619-1.685-2c-0.667-0.38-1.286-0.571-1.858-0.571c-2.856,0-4.286,1.885-4.286,5.657 c0,1.714,0.362,3.084,1.085,4.113c0.724,1.029,1.791,1.544,3.201,1.544c1.867,0,3.181-0.915,3.944-2.743l3.942,2 c-0.838,1.563-2,2.791-3.486,3.686c-1.484,0.896-3.123,1.343-4.914,1.343c-2.857,0-5.163-0.875-6.915-2.629 c-1.752-1.752-2.628-4.19-2.628-7.313c0-3.048,0.886-5.466,2.657-7.257c1.771-1.79,4.009-2.686,6.715-2.686 C32.604,18.558,35.441,20.101,37.156,23.187z M55.613,23.187l-4.229,2.229c-0.457-0.951-1.02-1.619-1.686-2 c-0.668-0.38-1.307-0.571-1.914-0.571c-2.857,0-4.287,1.885-4.287,5.657c0,1.714,0.363,3.084,1.086,4.113 c0.723,1.029,1.789,1.544,3.201,1.544c1.865,0,3.18-0.915,3.941-2.743l4,2c-0.875,1.563-2.057,2.791-3.541,3.686 c-1.486,0.896-3.105,1.343-4.857,1.343c-2.896,0-5.209-0.875-6.941-2.629c-1.736-1.752-2.602-4.19-2.602-7.313 c0-3.048,0.885-5.466,2.658-7.257c1.77-1.79,4.008-2.686,6.713-2.686C51.117,18.558,53.938,20.101,55.613,23.187z"/></svg>'
           '<svg class="cc-icon" viewBox="5.5 -3.5 64 64" aria-hidden="true"><path d="M37.443-3.5c8.988,0,16.57,3.085,22.742,9.257C66.393,11.967,69.5,19.548,69.5,28.5c0,8.991-3.049,16.476-9.145,22.456 C53.879,57.319,46.242,60.5,37.443,60.5c-8.649,0-16.153-3.144-22.514-9.43C8.644,44.784,5.5,37.262,5.5,28.5 c0-8.761,3.144-16.342,9.429-22.742C21.101-0.415,28.604-3.5,37.443-3.5z M37.557,2.272c-7.276,0-13.428,2.553-18.457,7.657 c-5.22,5.334-7.829,11.525-7.829,18.572c0,7.086,2.59,13.22,7.77,18.398c5.181,5.182,11.352,7.771,18.514,7.771 c7.123,0,13.334-2.607,18.629-7.828c5.029-4.838,7.543-10.952,7.543-18.343c0-7.276-2.553-13.465-7.656-18.571 C50.967,4.824,44.795,2.272,37.557,2.272z M46.129,20.557v13.085h-3.656v15.542h-9.944V33.643h-3.656V20.557 c0-0.572,0.2-1.057,0.599-1.457c0.401-0.399,0.887-0.6,1.457-0.6h13.144c0.533,0,1.01,0.2,1.428,0.6 C45.918,19.5,46.129,19.986,46.129,20.557z M33.042,12.329c0-3.008,1.485-4.514,4.458-4.514s4.457,1.504,4.457,4.514 c0,2.971-1.486,4.457-4.457,4.457S33.042,15.3,33.042,12.329z"/></svg>')
LICENCE_URL = "https://creativecommons.org/licenses/by/4.0/"
LICENCE_LINK = f'<a href="{LICENCE_URL}" rel="noopener license">{CC_MARK}CC BY 4.0</a>'

# Shown in the footer of every page.
NOTICE = f"""<div class="site-notice">
<p><strong>Licence.</strong> {CC_MARK}This wiki is open to the community under the <a href="{LICENCE_URL}" rel="noopener license">Creative Commons Attribution 4.0 International licence (CC BY 4.0)</a>. You may copy, share and adapt it for any purpose, including commercially, as long as you credit the authors.</p>
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
    line = "Author: " + html.escape(names[0])
    if len(names) > 1:
        line += " &middot; " + ("Co-authors: " if len(names) > 2 else "Co-author: ") + html.escape(", ".join(names[1:]))
    return line


def canonical(page):
    out = page["out"].replace(os.sep, "/")
    if out == "index.html" or out.endswith("/index.html"):
        out = out[:-len("index.html")]
    return f"{SITE_URL}/{out}"


def git(*args):
    return subprocess.run(["git", "-C", ROOT, "-c", "core.quotepath=off", *args],
                          capture_output=True, text=True).stdout


def last_modified():
    """Date each source page last changed: its last commit, or today if it has uncommitted edits."""
    dates, day = {}, None
    for line in git("log", "--format=@%cs", "--name-only", "--", "source").splitlines():
        if line.startswith("@"):
            day = line[1:]
        elif line:
            dates.setdefault(line, day)
    today = datetime.date.today().isoformat()
    for line in git("status", "--porcelain", "--", "source").splitlines():
        dates[line[3:].split(" -> ")[-1].strip('"')] = today
    return lambda page: dates.get("source/" + page["src"].replace(os.sep, "/"), today)


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
    if page["src"].split(os.sep)[0] in EMBLEMS or page["src"].split(os.sep)[0] in FLAGS:
        # Pages in a regional section show the section's flag or emblem before the main heading.
        content = re.sub(r"(<h1[^>]*>)", lambda m: m.group(1) + icon(page), content, count=1)
    banner = ""
    if page is home:
        content = re.sub(r"<h1[^>]*>.*?</h1>", "", content, count=1, flags=re.S)
        # The document details box that opens the page is shown above the section cards.
        details = re.match(r"\s*(<blockquote.*?</blockquote>)\s*", content, re.S)
        if details:
            content = content[details.end():]
        banner = hero(page, details.group(1) if details else "")
    doc = TEMPLATE.format(
        hue=look(page)[0], hero=banner, css_v=version("style.css"), js_v=version("site.js"),
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
    index.append({"t": title, "s": section, "u": page["out"].replace(os.sep, "/"), "c": plain(cases[0])})
    for anchor, chunk in zip(cases[1::2], cases[2::2]):
        heading = re.search(r"<h3[^>]*>(.*?)</h3>", chunk, re.S)
        body = plain(chunk.split("</table></div>", 1)[-1])
        index.append({"t": plain(heading.group(1)) if heading else anchor.upper(), "s": title,
                      "u": page["out"].replace(os.sep, "/") + "#" + anchor, "c": body[:CASE_SNIPPET]})

# Data files that pages link to (for example CSV downloads) are copied next to the generated pages.
for dirpath, dirs, files in os.walk(SRC):
    for f in files:
        if not f.endswith(".md") and not f.startswith("."):
            dest = os.path.join(ROOT, os.path.relpath(os.path.join(dirpath, f), SRC))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copyfile(os.path.join(dirpath, f), dest)

open(os.path.join(ROOT, "assets", "search-index.js"), "w", encoding="utf-8").write(
    "window.SEARCH_INDEX = " + json.dumps(index, ensure_ascii=False) + ";\n")
modified = last_modified()
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{canonical(p)}</loc><lastmod>{modified(p)}</lastmod></url>\n" for p in order) + "</urlset>\n")
print(f"Built {len(order)} pages")
