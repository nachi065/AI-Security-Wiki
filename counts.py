"""Counts that pages quote (cases, layers, controls and so on), read from the source files.

build.py replaces {{n:name}} in page text with these values; check_links.py uses the same
function to flag a page that writes one of the numbers out by hand.
"""
import glob
import os
import re


def site_counts(src):
    tests = os.path.join(src, "10_Test_Case_Library")
    cases = {"L": 0, "D": 0}
    critical = 0
    layers = 0
    levels = {"Documented": 0, "Executable": 0, "Lab-validated": 0, "Independently reproduced": 0}
    for path in sorted(glob.glob(os.path.join(tests, "[LD]*.md"))):
        kind = os.path.basename(path)[0]
        rows = re.findall(r"^\| \[TC-[LD]\d\d-\d{3}\]\(#[^)]*\) \|.*$", open(path, encoding="utf-8").read(), re.M)
        cases[kind] += len(rows)
        critical += sum(1 for r in rows if r.split(" | ")[2].strip() == "Critical")
        layers += kind == "L"
        for block in re.split(r"(?m)^(?=### TC-[LD]\d\d-\d{3}:)", open(path, encoding="utf-8").read())[1:]:
            case = block.split(":", 1)[0].replace("### ", "")
            own = re.search(r"^\| \*\*Validation Level\*\* \| \[?([A-Za-z -]+?)\]?(?:\(|:| \|)", block, re.M)
            payload = os.path.exists(os.path.join(tests, "kit", "payloads", case + ".json"))
            level = own.group(1).strip() if own else "Executable" if payload else "Documented"
            levels[level] = levels.get(level, 0) + 1  # check_links.py rejects a level that is not one of the four
    domains = len(glob.glob(os.path.join(tests, "D*.md")))
    lib = open(os.path.join(src, "03_Control_Library", "03_AI_Security_Control_Objectives_Library.md"), encoding="utf-8").read()
    controls = re.findall(r"^#### (AI-CTRL-\d{3}):", lib, re.M)
    families = {m.group(1).strip() for m in re.finditer(r"^\| \[AI-CTRL-\d{3}\]\(#[^)]*\) \| [^|]+ \| ([^|]+) \|", lib, re.M)}
    tiers = re.findall(r"^\| \*\*Tier\*\* \| (\w+) \|", lib, re.M)
    register = open(os.path.join(src, "02_Risk_Management", "02B_Enterprise_AI_Risk_Register.md"), encoding="utf-8").read()
    return {
        "tests": cases["L"] + cases["D"], "layer_tests": cases["L"], "domain_tests": cases["D"],
        "layers": layers, "domains": domains, "critical": critical,
        "controls": len(controls), "families": len(families),
        "baseline": tiers.count("Baseline"), "advanced": tiers.count("Advanced"),
        "risks": len(set(re.findall(r"^### (AI-R\d\d):", register, re.M))),
        "documented": levels["Documented"], "executable": levels["Executable"],
        "lab_validated": levels["Lab-validated"], "reproduced": levels["Independently reproduced"],
        "kit_cases": len(glob.glob(os.path.join(tests, "kit", "payloads", "TC-*.json"))),
    }


if __name__ == "__main__":
    print(site_counts(os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")))
