"""Write the risk register, controls, risk-to-control mapping, test cases and AI Risk Map crosswalk as CSV files.

build.py calls main() on every build, so the files in source/25_Templates/data/ always match the pages they are read from.
The files are for tools that join on the wiki's IDs; the pages remain the source of truth.
"""
import csv, glob, os, re

DATA = os.path.join("25_Templates", "data")


def text(cell):
    """Plain text of a Markdown table cell: links become their label, emphasis and escapes are dropped."""
    cell = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cell)
    cell = re.sub(r"\*\*|(?<!\w)\*(?!\s)|(?<!\s)\*(?!\w)|`", "", cell)
    return re.sub(r"\s+", " ", cell.replace("\\|", "|")).strip()


def cells(line):
    return [text(c) for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def table_after(body, header_start):
    """Rows of the first table whose header row starts with header_start."""
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(header_start):
            rows = []
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                rows.append(cells(row))
            return cells(line), rows
    raise ValueError(f"no table starting {header_start!r}")


def write(src, name, header, rows):
    os.makedirs(os.path.join(src, DATA), exist_ok=True)
    path = os.path.join(src, DATA, name)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def read(src, rel):
    with open(os.path.join(src, rel), encoding="utf-8") as f:
        return f.read()


def risks(src):
    body = read(src, "02_Risk_Management/02B_Enterprise_AI_Risk_Register.md")
    header, rows = table_after(body, "| Risk ID |")
    narr = {m.group(1): re.sub(r"\s+", " ", text(m.group(2))) for m in
            re.finditer(r"(?ms)^### (AI-R\d\d): [^\n]*\n(.*?)(?=^#{2,3} |\Z)", body)}
    write(src, "risk_register.csv", header + ["Narrative"], [r + [narr.get(r[0], "")] for r in rows])


def risk_control_map(src):
    body = read(src, "02_Risk_Management/02D_AI_Risk_to_Control_Mapping.md")
    header, rows = table_after(body, "| Risk ID |")
    write(src, "risk_to_control.csv", header, rows)


def controls(src):
    body = read(src, "03_Control_Library/03_AI_Security_Control_Objectives_Library.md")
    fields = ["Control Objective", "Tier", "Applies To", "Risk Mapping"]
    rows = []
    for m in re.finditer(r"(?ms)^#### (AI-CTRL-\d{3}): ([^\n]*)\n(.*?)(?=^#{2,4} |\Z)", body):
        detail = {}
        for line in m.group(3).splitlines():
            c = cells(line) if line.startswith("|") else []
            if len(c) >= 2:
                detail[c[0]] = c[1]
        rows.append([m.group(1), m.group(2).strip()] + [detail.get(f, "") for f in fields])
    rows.sort()
    write(src, "controls.csv", ["Control ID", "Name"] + fields, rows)


def test_cases(src):
    rows = []
    for path in sorted(glob.glob(os.path.join(src, "10_Test_Case_Library", "[LD][0-9][0-9]-*.md"))):
        body = open(path, encoding="utf-8").read()
        title = re.search(r'(?m)^title: "?([^"\n]*)"?$', body)
        header, cases = table_after(body, "| ID | Title |")
        for c in cases:
            c = dict(zip(header, c))
            rows.append([c["ID"], c["Title"], c["Severity"], c["Method"], c.get("Domain(s)", ""), c["Controls"],
                         os.path.basename(path)[:3], title.group(1) if title else ""])
    write(src, "test_cases.csv", ["Test Case ID", "Title", "Severity", "Method", "Domain(s)", "Controls", "Layer or Domain", "Page"], rows)


def risk_map_crosswalk(src):
    body = read(src, "23_Framework_Crosswalks/18_AI_Risk_Map_Crosswalk.md")
    header, rows = table_after(body, "| Map domain |")
    write(src, "ai_risk_map_crosswalk.csv", header, rows)


def main(src):
    risks(src)
    risk_control_map(src)
    controls(src)
    test_cases(src)
    risk_map_crosswalk(src)


if __name__ == "__main__":
    main(os.path.join(os.path.dirname(os.path.abspath(__file__)), "source"))
