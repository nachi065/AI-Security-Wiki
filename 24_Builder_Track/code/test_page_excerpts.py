"""Checks that every code excerpt on the Builder Track pages appears word for word
in the file it names, so the pages cannot drift away from the code.

Run:  python3 -m unittest -v test_page_excerpts   (from this folder)

An excerpt on the page looks like this:

    <!-- excerpt: guard.py -->
    ```python
    ...lines copied from guard.py...
    ```
"""
import re
import unittest
from pathlib import Path

HERE = Path(__file__).parent
PAGE = HERE.parent / "01_Secure_Your_First_Agent.md"
PAGES = sorted(HERE.parent.glob("0*.md"))
PATTERN = re.compile(r"<!-- excerpt: (?P<file>[\w.\-]+) -->\n```\w*\n(?P<body>.*?)\n```", re.S)


class PageExcerpts(unittest.TestCase):
    def test_excerpts_match_the_files(self):
        self.assertGreater(len(PATTERN.findall(PAGE.read_text())), 10, "the page should contain its code excerpts")
        for page in PAGES:
            for m in PATTERN.finditer(page.read_text()):
                source = (HERE / m["file"]).read_text()
                self.assertIn(m["body"], source,
                              f"{page.name}: excerpt from {m['file']} no longer matches:\n{m['body'][:200]}")


if __name__ == "__main__":
    unittest.main()
