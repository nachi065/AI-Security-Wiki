# AI Security Wiki

A vendor-neutral reference for AI security governance, risk management, engineering standards, vendor evaluation and assurance.

## Ready-to-browse site

**https://nachi065.github.io/AI-Security-Wiki/**

The full wiki is published as a website, so there is nothing to clone or install. Open the link in any browser to get:

- A sidebar with every section and page
- Full-text search across the whole wiki
- Clickable cross-references between pages
- A layout that works on phones and tablets

| Start here | Link |
|---|---|
| Wiki home, lifecycle and role navigation | https://nachi065.github.io/AI-Security-Wiki/ |
| Risk management | https://nachi065.github.io/AI-Security-Wiki/02_Risk_Management/ |
| Control library | https://nachi065.github.io/AI-Security-Wiki/03_Control_Library/ |
| Domain standards | https://nachi065.github.io/AI-Security-Wiki/04_Domain_Standards/ |
| Vendor evaluation | https://nachi065.github.io/AI-Security-Wiki/05_Vendor_Evaluation/ |
| Testing and assurance | https://nachi065.github.io/AI-Security-Wiki/06_Testing_and_Assurance/ |
| Role-based playbooks | https://nachi065.github.io/AI-Security-Wiki/07_Role_Based_Playbooks/ |

The pages are plain HTML, so the site also works offline: download the repository and open `index.html` in a browser.

## Author and contributing

Original author: **Nachiket Sathaye**

Contributions are welcome through pull requests; see [CONTRIBUTING.md](CONTRIBUTING.md). The original author credit is fixed: it appears on every page, and an automated check rejects any change that alters or removes it.

## Structure

| Path | Contents |
|---|---|
| `index.html` | Wiki home, lifecycle and role navigation |
| `01_Strategy_and_Market/` … `09_Reference/` | The HTML pages, one folder per wiki section |
| `assets/` | Stylesheet, navigation and search scripts, search index |
| `source/` | The Markdown the pages are generated from |
| `build.py` | Regenerates the HTML pages from `source/` |
| `AUTHORS`, `check_author.py` | Original author record and the check that protects it |

## Editing a page

Edit the Markdown file under `source/`, then rebuild and push:

```sh
pip install markdown
python3 build.py
git add -A && git commit -m "Update wiki" && git push
```

The live site updates a minute or two after the push.
