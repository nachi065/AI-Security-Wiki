"""Tests for the Builder Toolkit: aiwiki_check.py, wiki_data.py, mcp_server.py,
evidence_export.py and gen_instructions.py. They use only the standard library
and run on Linux, macOS and Windows.

Run:  python -m unittest -v test_toolkit   (from this folder)
"""
import contextlib
import csv
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path

import aiwiki_check
import evidence_export
import gen_instructions
import mcp_server
from guard import AuditLog
from wiki_data import WikiData

HERE = Path(__file__).resolve().parent
RULES = aiwiki_check.load_rules()
SITE_ROOT = HERE.parents[2]  # the generated site sits next to source/ in the wiki repository


def rules_hit(text, filename):
    return sorted({f.rule for f in aiwiki_check.scan_text(text, filename, RULES)})


class Rules(unittest.TestCase):
    def test_rule_file_is_complete(self):
        ids = [r["id"] for r in RULES["rules"]]
        self.assertEqual(len(ids), len(set(ids)))
        wd = WikiData()
        for r in RULES["rules"]:
            for key in ("title", "severity", "message", "remediation", "controls", "testCases"):
                self.assertTrue(r.get(key), f"{r['id']} lacks {key}")
            for c in r["controls"]:
                self.assertIn(c, wd.controls, f"{r['id']} names unknown control {c}")
            for t in r["testCases"]:
                self.assertIn(t, wd.tests, f"{r['id']} names unknown test case {t}")
            for k in r.get("risks", []):
                self.assertIn(k, wd.risks, f"{r['id']} names unknown risk {k}")

    def test_each_line_rule_fires_and_stays_quiet(self):
        cases = {
            "AIW-001": ("app.py", "result = eval(llm_output)", "result = eval(config_value)"),
            "AIW-002": ("ui.js", "el.innerHTML = completion;", "el.textContent = completion;"),
            "AIW-003": ("db.py", 'cur.execute(f"SELECT * FROM t WHERE x = {model_output}")',
                        'cur.execute("SELECT * FROM t WHERE x = ?", (model_output,))'),
            "AIW-004": ("load.py", "m = torch.load(path)", "m = torch.load(path, weights_only=True)"),
            "AIW-005": ("load.py", 'AutoModel.from_pretrained("org/m", revision="a1b2", trust_remote_code=True)',
                        'AutoModel.from_pretrained("org/m", revision="a1b2")'),
            "AIW-006": ("load.py", 'AutoModel.from_pretrained("org/model")', 'AutoModel.from_pretrained("org/model", revision="0f1e2d")'),
            "AIW-010": ("run.sh", "claude -p 'fix it' --dangerously-skip-permissions", "claude -p 'fix it'"),
        }
        for rule, (name, bad, good) in cases.items():
            with self.subTest(rule=rule):
                self.assertIn(rule, rules_hit(bad, name))
                self.assertNotIn(rule, rules_hit(good, name))

    def test_rules_only_apply_to_their_file_types(self):
        self.assertEqual(rules_hit("eval(llm_output)", "notes.txt"), [])

    def test_suppression(self):
        self.assertEqual(rules_hit("m = torch.load(p)  # aiwiki: ignore AIW-004 (our own file)", "a.py"), [])
        self.assertEqual(rules_hit("m = torch.load(p)  # aiwiki: ignore", "a.py"), [])
        self.assertIn("AIW-004", rules_hit("m = torch.load(p)  # aiwiki: ignore AIW-001", "a.py"))

    def test_mcp_config(self):
        config = {"mcpServers": {
            "loose": {"command": "npx", "args": ["-y", "@acme/mcp-server"]},
            "latest": {"command": "npx", "args": ["-y", "@acme/other@latest"]},
            "pinned": {"command": "npx", "args": ["-y", "@acme/pinned@1.4.2"]},
            "py-loose": {"command": "uvx", "args": ["mcp-server-fetch"]},
            "py-pinned": {"command": "uvx", "args": ["mcp-server-fetch==2025.4.7"]},
            "image": {"command": "docker", "args": ["run", "-i", "--rm", "-e", "TOKEN", "ghcr.io/acme/mcp:1.0"]},
            "image-digest": {"command": "docker", "args": ["run", "-i", "ghcr.io/acme/mcp@sha256:" + "a" * 64]},
            "remote": {"url": "http://mcp.example.com/mcp"},
            "local-http": {"url": "http://127.0.0.1:8765/mcp"},
            "tls": {"url": "https://mcp.example.com/mcp"},
            "auto": {"command": "python", "args": ["server.py"], "autoApprove": ["delete_file"]},
            "trusted": {"command": "python", "args": ["server.py"], "trust": True},
        }}
        found = aiwiki_check.scan_text(json.dumps(config, indent=2), "mcp.json", RULES)
        by = {}
        for f in found:
            by.setdefault(f.rule, set()).add(re.search(r"\(server ([^:]+):", f.message).group(1))
        self.assertEqual(by["AIW-007"], {"loose", "latest", "py-loose", "image"})
        self.assertEqual(by["AIW-008"], {"remote"})
        self.assertEqual(by["AIW-009"], {"auto", "trusted"})

    def test_vscode_style_config_is_read(self):
        config = {"servers": {"x": {"type": "stdio", "command": "npx", "args": ["some-server"]}}}
        self.assertIn("AIW-007", rules_hit(json.dumps(config), "mcp.json"))

    def test_reference_code_is_clean(self):
        files = [str(p) for p in sorted(HERE.iterdir()) if p.is_file() and not p.name.startswith("test_")]
        self.assertEqual(aiwiki_check.scan_paths(files, RULES), [])

    def test_rules_file_is_not_reported_against_itself(self):
        self.assertEqual(aiwiki_check.scan_paths([str(HERE / "ai_rules.json")], RULES), [])


class CheckerCLI(unittest.TestCase):
    def run_cli(self, *args, stdin=""):
        out = io.StringIO()
        old_in, old_out = sys.stdin, sys.stdout
        sys.stdin, sys.stdout = io.StringIO(stdin), out
        try:
            code = aiwiki_check.main(list(args))
        finally:
            sys.stdin, sys.stdout = old_in, old_out
        return code, out.getvalue()

    def test_exit_codes_and_fail_on(self):
        self.assertEqual(self.run_cli("--stdin", "--filename", "a.py", stdin="x = 1\n")[0], 0)
        self.assertEqual(self.run_cli("--stdin", "--filename", "a.py", stdin="m = torch.load(p)\n")[0], 1)
        low = 'AutoModel.from_pretrained("org/model")\n'
        self.assertEqual(self.run_cli("--stdin", "--filename", "a.py", stdin=low)[0], 0)
        self.assertEqual(self.run_cli("--stdin", "--filename", "a.py", "--fail-on", "low", stdin=low)[0], 1)
        self.assertEqual(self.run_cli("--format", "nonsense")[0], 2)

    def test_sarif_shape(self):
        code, out = self.run_cli("--stdin", "--filename", "src/a.py", "--format", "sarif", stdin="\nm = torch.load(p)\n")
        sarif = json.loads(out)
        self.assertEqual(sarif["version"], "2.1.0")
        run = sarif["runs"][0]
        self.assertEqual(run["tool"]["driver"]["rules"][0]["id"], "AIW-004")
        self.assertIn("ai-ctrl-028", run["tool"]["driver"]["rules"][0]["helpUri"])
        res = run["results"][0]
        self.assertEqual(res["level"], "error")
        self.assertEqual(res["locations"][0]["physicalLocation"]["artifactLocation"]["uri"], "src/a.py")
        self.assertEqual(res["locations"][0]["physicalLocation"]["region"]["startLine"], 2)
        self.assertIn("AI-CTRL-031", res["properties"]["controls"])

    def test_folder_scan_skips_vendored_folders(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "src").mkdir()
            (Path(d) / "node_modules" / "pkg").mkdir(parents=True)
            (Path(d) / "src" / "a.py").write_text("m = torch.load(p)\n", encoding="utf-8")
            (Path(d) / "node_modules" / "pkg" / "b.py").write_text("m = torch.load(p)\n", encoding="utf-8")
            found = aiwiki_check.scan_paths([d], RULES)
        self.assertEqual([Path(f.path).name for f in found], ["a.py"])

    @unittest.skipUnless(shutil.which("git"), "git is not installed")
    def test_staged_mode_reports_only_added_lines(self):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as d:  # git marks objects read-only on Windows
            def git(*a):
                subprocess.run(["git", *a], cwd=d, check=True, capture_output=True)
            git("init", "-q")
            git("config", "user.email", "t@example.com")
            git("config", "user.name", "t")
            f = Path(d) / "a.py"
            f.write_text("old = torch.load(p)\n", encoding="utf-8")
            git("add", "a.py")
            git("commit", "-qm", "base", "--no-verify")
            f.write_text("old = torch.load(p)\nnew = pickle.loads(blob)\n", encoding="utf-8")
            git("add", "a.py")
            here = os.getcwd()
            os.chdir(d)
            try:
                found = aiwiki_check.scan_diff(["--cached"], RULES)
            finally:
                os.chdir(here)
        self.assertEqual([(f.rule, f.line) for f in found], [("AIW-004", 2)])

    def test_added_lines_parser(self):
        diff = "+++ b/x.py\n@@ -0,0 +1,2 @@\n+a\n+b\n+++ b/y.py\n@@ -5 +7 @@\n-c\n+d\n+++ /dev/null\n"
        self.assertEqual(aiwiki_check.added_lines(diff), {"x.py": {1, 2}, "y.py": {7}})


class Data(unittest.TestCase):
    wd = WikiData()

    def test_lookups(self):
        c = self.wd.control("ai-ctrl-024")
        self.assertEqual(c["name"], "Tool and MCP Server Governance")
        self.assertIn("TC-L06-008", c["testCases"])
        self.assertIn("AI-R23", c["risks"])
        r = self.wd.risk("AI-R23")
        self.assertIn("AI-CTRL-024", r["controls"])
        t = self.wd.test_case("TC-L06-008")
        self.assertEqual(t["controls"], ["AI-CTRL-024"])
        self.assertTrue(t["url"].endswith("L06-agent-orchestration-layer.html#tc-l06-008"))
        self.assertIsNone(self.wd.get("AI-CTRL-999"))

    def test_search(self):
        hits = self.wd.search("kill switch")
        self.assertEqual(hits[0]["id"], "AI-CTRL-025")
        self.assertTrue(all(h["type"] == "test" for h in self.wd.search("kill switch", kind="test")))
        self.assertEqual(self.wd.search("   "), [])

    def test_links_resolve_on_the_built_site(self):
        pages = {"control": SITE_ROOT / "03_Control_Library" / "03_AI_Security_Control_Objectives_Library.html",
                 "risk": SITE_ROOT / "02_Risk_Management" / "02B_Enterprise_AI_Risk_Register.html"}
        if not all(p.exists() for p in pages.values()):
            self.skipTest("the built site is not next to the source")
        risk_html = pages["risk"].read_text(encoding="utf-8")
        for rid in self.wd.risks:
            self.assertIn(f'id="{self.wd.risk_url(rid).split("#")[1]}"', risk_html, rid)
        control_html = pages["control"].read_text(encoding="utf-8")
        for cid in self.wd.controls:
            self.assertIn(f'id="{cid.lower()}"', control_html, cid)

    def test_missing_data_folder_is_reported(self):
        with tempfile.TemporaryDirectory() as d, self.assertRaises(FileNotFoundError):
            WikiData(d)


def rpc(server, method, params=None, mid=1):
    msg = {"jsonrpc": "2.0", "method": method}
    if mid is not None:
        msg["id"] = mid
    if params is not None:
        msg["params"] = params
    return server.handle(msg)


class MCP(unittest.TestCase):
    server = mcp_server.Server()

    def call(self, name, **args):
        res = rpc(self.server, "tools/call", {"name": name, "arguments": args})["result"]
        return res["isError"], (json.loads(res["content"][0]["text"]) if not res["isError"] else res["content"][0]["text"])

    def test_initialize_negotiates_the_version(self):
        r = rpc(self.server, "initialize", {"protocolVersion": "2025-03-26", "capabilities": {}})["result"]
        self.assertEqual(r["protocolVersion"], "2025-03-26")
        self.assertIn("tools", r["capabilities"])
        r = rpc(self.server, "initialize", {"protocolVersion": "1999-01-01"})["result"]
        self.assertEqual(r["protocolVersion"], mcp_server.PROTOCOLS[0])

    def test_notifications_get_no_reply_and_unknown_methods_an_error(self):
        self.assertIsNone(rpc(self.server, "notifications/initialized", mid=None))
        self.assertEqual(rpc(self.server, "nope")["error"]["code"], -32601)
        self.assertEqual(self.server.handle({"id": 1})["error"]["code"], -32600)

    def test_every_tool_is_listed_read_only(self):
        tools = rpc(self.server, "tools/list")["result"]["tools"]
        self.assertEqual({t["name"] for t in tools}, {"wiki_get", "wiki_search", "wiki_controls_for_risk",
                                                    "wiki_tests_for_control", "check_ai_code", "check_secrets"})
        for t in tools:
            self.assertTrue(t["annotations"]["readOnlyHint"])
            self.assertEqual(t["inputSchema"]["type"], "object")

    def test_tools(self):
        err, out = self.call("wiki_get", id="AI-CTRL-025")
        self.assertFalse(err)
        self.assertEqual(out["name"], "AI Containment and Kill Switch")
        self.assertTrue(self.call("wiki_get", id="AI-CTRL-999")[0])
        self.assertEqual(self.call("wiki_search", query="kill switch", limit=1)[1][0]["id"], "AI-CTRL-025")
        self.assertIn("AI-CTRL-024", [c["id"] for c in self.call("wiki_controls_for_risk", risk_id="AI-R23")[1]["controls"]])
        self.assertIn("TC-L06-008", [t["id"] for t in self.call("wiki_tests_for_control", control_id="AI-CTRL-024")[1]["testCases"]])
        out = self.call("check_ai_code", text="m = torch.load(p)\n", filename="a.py")[1]
        self.assertEqual(out["findings"][0]["rule"], "AIW-004")
        out = self.call("check_secrets", text="key = 'AKIA" + "ABCDEFGHIJKLMNOP'\n")[1]
        self.assertTrue(out["findings"])
        self.assertTrue(self.call("check_ai_code", text=None, filename="a.py")[0])
        self.assertTrue(self.call("nope")[0])

    def test_prompt(self):
        names = [p["name"] for p in rpc(self.server, "prompts/list")["result"]["prompts"]]
        self.assertEqual(names, ["review-agent-design"])
        msg = rpc(self.server, "prompts/get", {"name": "review-agent-design", "arguments": {"design": "A ticket bot"}})
        self.assertIn("A ticket bot", msg["result"]["messages"][0]["content"]["text"])

    def test_stdio_transport(self):
        lines = [json.dumps({"jsonrpc": "2.0", "id": 1, "method": "ping"}), "not json",
                 json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}), ""]
        out = io.StringIO()
        mcp_server.serve_stdio(self.server, io.StringIO("\n".join(lines) + "\n"), out)
        replies = [json.loads(x) for x in out.getvalue().splitlines()]
        self.assertEqual(replies[0], {"jsonrpc": "2.0", "id": 1, "result": {}})
        self.assertEqual(replies[1]["error"]["code"], -32700)
        self.assertEqual(len(replies), 2)

    def test_stdio_subprocess(self):
        req = json.dumps({"jsonrpc": "2.0", "id": 7, "method": "tools/list"}) + "\n"
        p = subprocess.run([sys.executable, str(HERE / "mcp_server.py")], input=req.encode(), capture_output=True,
                           timeout=60, cwd=HERE)
        self.assertEqual(json.loads(p.stdout.decode("utf-8").splitlines()[0])["id"], 7)
        self.assertNotIn(b"\r\n", p.stdout)

    def test_http_transport(self):
        handler = mcp_server.make_http_handler(self.server, "s3cret", {"127.0.0.1", "localhost"})
        httpd = mcp_server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        url = f"http://127.0.0.1:{httpd.server_address[1]}/mcp"

        def post(body, **headers):
            req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                         headers={"Content-Type": "application/json", **headers})
            try:
                with urllib.request.urlopen(req, timeout=10) as r:
                    return r.status, r.read()
            except urllib.error.HTTPError as e:
                return e.code, e.read()
        try:
            ping = {"jsonrpc": "2.0", "id": 1, "method": "ping"}
            self.assertEqual(post(ping)[0], 403)
            self.assertEqual(post(ping, Authorization="Bearer wrong")[0], 403)
            self.assertEqual(post(ping, Authorization="Bearer s3cret", Origin="https://evil.example")[0], 403)
            code, body = post(ping, Authorization="Bearer s3cret")
            self.assertEqual((code, json.loads(body)["id"]), (200, 1))
            note = {"jsonrpc": "2.0", "method": "notifications/initialized"}
            self.assertEqual(post(note, Authorization="Bearer s3cret")[0], 202)
        finally:
            httpd.shutdown()
            httpd.server_close()

    def test_refuses_public_bind_without_token(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(mcp_server.main(["--http", "--host", "0.0.0.0"]), 2)


class Evidence(unittest.TestCase):
    def make_log(self, d):
        path = Path(d) / "audit.jsonl"
        log = AuditLog(str(path))
        for reason in ["OK", "DENY_ARGS", "DENY_ARGS", "DENY_KILL", "DENY_DEFINITION_CHANGED"]:
            log.write(event="decision", agent="agent://a", tool="t", args={}, status="x", reason=reason, detail="")
        log.write(event="approval_requested", agent="agent://a", tool="send_email", args={}, approval_id="1")
        return path

    def test_rows_from_log_and_sarif(self):
        with tempfile.TemporaryDirectory() as d:
            log = self.make_log(d)
            sarif = Path(d) / "a.sarif"
            findings = aiwiki_check.scan_text("m = torch.load(p)\n", "a.py", RULES)
            sarif.write_text(json.dumps(aiwiki_check.to_sarif(findings, RULES)), encoding="utf-8")
            controls, tests = Path(d) / "c.csv", Path(d) / "t.csv"
            code = evidence_export.main(["--audit-log", str(log), "--sarif", str(sarif),
                                         "--controls", str(controls), "--tests", str(tests)])
            self.assertEqual(code, 0)
            with open(controls, newline="", encoding="utf-8") as f:
                rows = {r["Control ID"]: r for r in csv.DictReader(f)}
            with open(tests, newline="", encoding="utf-8") as f:
                trows = {r["Test Case ID"]: r for r in csv.DictReader(f)}
        self.assertEqual(list(next(iter(rows.values())).keys()), evidence_export.CONTROL_COLUMNS)
        self.assertIn("Hash chain verified over 6 entries", rows["AI-CTRL-008"]["Auditor Notes"])
        self.assertIn("2 decision(s) with reason DENY_ARGS", rows["AI-CTRL-022"]["Auditor Notes"])
        self.assertIn("PENDING_APPROVAL", rows["AI-CTRL-023"]["Auditor Notes"])
        self.assertIn("AIW-004", rows["AI-CTRL-028"]["Auditor Notes"])
        self.assertEqual(rows["AI-CTRL-028"]["Result"], "")
        self.assertEqual(rows["AI-CTRL-024"]["Control"], "Tool and MCP Server Governance")
        self.assertIn("TC-L06-008", trows)
        self.assertIn("TC-L12-002", trows)

    def test_tampered_log_is_flagged(self):
        with tempfile.TemporaryDirectory() as d:
            log = self.make_log(d)
            lines = log.read_text(encoding="utf-8").splitlines()
            lines[1] = lines[1].replace("DENY_ARGS", "OK")
            log.write_text("\n".join(lines) + "\n", encoding="utf-8")
            code = evidence_export.main(["--audit-log", str(log), "--controls", str(Path(d) / "c.csv")])
            text = (Path(d) / "c.csv").read_text(encoding="utf-8")
        self.assertEqual(code, 1)
        self.assertIn("BROKEN at entry 1", text)

    def test_same_verdict_as_the_guard(self):
        with tempfile.TemporaryDirectory() as d:
            log = self.make_log(d)
            entries = [json.loads(x) for x in log.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(evidence_export.verify_chain(entries), AuditLog.verify(str(log)))

    def test_every_reason_maps_to_a_known_control_and_test(self):
        wd = WikiData()
        for reason, (control, tests) in evidence_export.REASONS.items():
            self.assertIn(control, wd.controls, reason)
            for t in tests:
                self.assertIn(t, wd.tests, reason)


class Instructions(unittest.TestCase):
    def test_writes_checks_and_keeps_existing_files(self):
        with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(io.StringIO()):
            (Path(d) / "AGENTS.md").write_text("my own rules\n", encoding="utf-8")
            self.assertEqual(gen_instructions.main(["--out", d]), 0)
            self.assertEqual((Path(d) / "AGENTS.md").read_text(encoding="utf-8"), "my own rules\n")
            cursor = (Path(d) / ".cursor" / "rules" / "ai-security-wiki.mdc").read_text(encoding="utf-8")
            self.assertTrue(cursor.startswith("---\n"))
            self.assertEqual(gen_instructions.main(["--out", d, "--check"]), 1)  # AGENTS.md differs
            self.assertEqual(gen_instructions.main(["--out", d, "--force"]), 0)
            self.assertEqual(gen_instructions.main(["--out", d, "--check"]), 0)
            for name, (rel, _) in gen_instructions.TARGETS.items():
                self.assertIn("AI-CTRL-020", (Path(d) / rel).read_text(encoding="utf-8"), name)

    def test_instructions_name_only_real_ids(self):
        wd = WikiData()
        text = gen_instructions.SOURCE.read_text(encoding="utf-8")
        for i in re.findall(r"AI-CTRL-\d{3}", text):
            self.assertIn(i, wd.controls)


if __name__ == "__main__":
    unittest.main()
