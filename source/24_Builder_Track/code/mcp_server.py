"""A Model Context Protocol (MCP) server that gives any MCP-capable assistant
or agent read-only access to the wiki's controls, risks and test cases, and
to the Builder Track checks. It is not tied to one vendor: any client that
speaks MCP can use it, and the same answers come from the command line tools.

Standard library only; works on Linux, macOS and Windows.

    python mcp_server.py                                # stdio, for local clients
    python mcp_server.py --http --port 8765             # http://127.0.0.1:8765/mcp
    options: --data DIR (wiki CSV folder)  --token TOKEN (or $AIWIKI_MCP_TOKEN)  --allow-host HOST

Every tool is read-only: none of them writes files, runs commands or reaches
the network. The HTTP mode listens on 127.0.0.1 only; it will not bind to any
other address unless a bearer token is set, and it rejects requests whose
Origin or Host header names an unknown host (DNS rebinding protection).
"""
from __future__ import annotations

import argparse
import hmac
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

import aiwiki_check
import pipeline_checks
from wiki_data import WikiData

NAME, VERSION = "ai-security-wiki", "1.0.0"
# Protocol revisions this server answers to, newest first. Check the current
# MCP specification before relying on a newer client revision.
PROTOCOLS = ["2025-06-18", "2025-03-26", "2024-11-05"]
MAX_TEXT = 200_000

ID_ARG = {"type": "string", "description": "A wiki ID such as AI-CTRL-024, AI-R23 or TC-L06-008"}
TOOLS = [
    {"name": "wiki_get", "title": "Look up a wiki control, risk or test case",
     "description": "Return one control (AI-CTRL-nnn), register risk (AI-R nn) or test case (TC-xnn-nnn) with its links, "
                    "related controls, risks and test cases, and the URL of the page that is authoritative.",
     "inputSchema": {"type": "object", "properties": {"id": ID_ARG}, "required": ["id"]}},
    {"name": "wiki_search", "title": "Search the wiki's controls, risks and test cases",
     "description": "Find controls, risks or test cases whose ID, name or description contains every word of the query.",
     "inputSchema": {"type": "object", "properties": {
         "query": {"type": "string"},
         "kind": {"type": "string", "enum": ["all", "control", "risk", "test"], "default": "all"},
         "limit": {"type": "integer", "minimum": 1, "maximum": 100, "default": 20}}, "required": ["query"]}},
    {"name": "wiki_controls_for_risk", "title": "Controls that treat a risk",
     "description": "List the controls the wiki maps to one register risk, with the evidence it expects.",
     "inputSchema": {"type": "object", "properties": {"risk_id": ID_ARG}, "required": ["risk_id"]}},
    {"name": "wiki_tests_for_control", "title": "Test cases that prove a control",
     "description": "List the wiki test cases that test one control.",
     "inputSchema": {"type": "object", "properties": {"control_id": ID_ARG}, "required": ["control_id"]}},
    {"name": "check_ai_code", "title": "Check code or agent configuration for AI-specific risks",
     "description": "Run the wiki's AI rules (model output reaching eval, HTML or SQL; unsafe model loading; unpinned "
                    "models and MCP servers; auto-approved tools) over text you are about to write. Returns findings "
                    "with the controls and test cases for each. A clean result is not proof of safety.",
     "inputSchema": {"type": "object", "properties": {
         "text": {"type": "string"},
         "filename": {"type": "string", "description": "Used to pick the rules, for example app.py or mcp.json"}},
         "required": ["text", "filename"]}},
    {"name": "check_secrets", "title": "Check text for secrets before it is written",
     "description": "Run the Builder Track secret patterns over text you are about to write or commit.",
     "inputSchema": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}},
]
for _t in TOOLS:
    _t["annotations"] = {"readOnlyHint": True, "destructiveHint": False, "openWorldHint": False}

PROMPTS = [
    {"name": "review-agent-design", "description": "Review an agent design against the Builder Track's ten controls.",
     "arguments": [{"name": "design", "description": "The agent's purpose, tools, data and who it acts for", "required": True}]},
]


class ToolError(Exception):
    pass


class Server:
    def __init__(self, data_dir: str | None = None):
        self.data_dir = data_dir
        self._wd = None
        self.rules = aiwiki_check.load_rules()

    @property
    def wd(self) -> WikiData:
        if self._wd is None:
            self._wd = WikiData(self.data_dir)
        return self._wd

    # ---- tools ---------------------------------------------------------------
    def call(self, name: str, args: dict) -> object:
        if name == "wiki_get":
            item = self.wd.get(str(args.get("id", "")))
            if item is None:
                raise ToolError(f"{args.get('id')} is not a wiki control, risk or test case ID")
            return item
        if name == "wiki_search":
            limit = max(1, min(int(args.get("limit", 20)), 100))
            return self.wd.search(str(args.get("query", "")), str(args.get("kind", "all")), limit)
        if name == "wiki_controls_for_risk":
            risk = self.wd.risk(str(args.get("risk_id", "")))
            if risk is None:
                raise ToolError(f"{args.get('risk_id')} is not a register risk")
            return {"risk": risk["id"], "name": risk["name"], "evidenceRequired": risk["evidenceRequired"],
                    "controls": [{"id": c, "name": self.wd.controls.get(c, {}).get("Name", ""), "url": self.wd.control_url(c)}
                                 for c in risk["controls"]]}
        if name == "wiki_tests_for_control":
            ctrl = self.wd.control(str(args.get("control_id", "")))
            if ctrl is None:
                raise ToolError(f"{args.get('control_id')} is not a control")
            return {"control": ctrl["id"], "name": ctrl["name"], "testCases": [self.wd.test_case(t) for t in ctrl["testCases"]]}
        if name == "check_ai_code":
            text = self._text(args)
            found = aiwiki_check.scan_text(text, str(args.get("filename") or "stdin"), self.rules)
            return {"findings": [f.__dict__ for f in found], "note": "Heuristic rules; review each finding."}
        if name == "check_secrets":
            found = pipeline_checks.scan_secrets(self._text(args), "text")
            return {"findings": [{"check": f.check, "where": f.where, "detail": f.detail} for f in found]}
        raise ToolError(f"unknown tool {name}")

    @staticmethod
    def _text(args: dict) -> str:
        text = args.get("text")
        if not isinstance(text, str):
            raise ToolError("text must be a string")
        if len(text) > MAX_TEXT:
            raise ToolError(f"text is longer than {MAX_TEXT} characters")
        return text

    # ---- JSON-RPC --------------------------------------------------------------
    def handle(self, msg: dict) -> dict | None:
        """Answer one JSON-RPC message. Notifications (no id) get no answer."""
        if not isinstance(msg, dict) or msg.get("jsonrpc") != "2.0" or not isinstance(msg.get("method"), str):
            return _error(msg.get("id") if isinstance(msg, dict) else None, -32600, "invalid request")
        mid, method, params = msg.get("id"), msg["method"], msg.get("params") or {}
        if "id" not in msg:
            return None
        try:
            if method == "initialize":
                asked = params.get("protocolVersion")
                return _result(mid, {
                    "protocolVersion": asked if asked in PROTOCOLS else PROTOCOLS[0],
                    "capabilities": {"tools": {"listChanged": False}, "prompts": {"listChanged": False}},
                    "serverInfo": {"name": NAME, "version": VERSION},
                    "instructions": "Read-only look-ups over the AI Security Wiki and its Builder Track checks. "
                                    "The wiki pages linked in each answer are authoritative."})
            if method == "ping":
                return _result(mid, {})
            if method == "tools/list":
                return _result(mid, {"tools": TOOLS})
            if method == "tools/call":
                try:
                    out = self.call(str(params.get("name")), params.get("arguments") or {})
                    return _result(mid, {"content": [{"type": "text", "text": json.dumps(out, indent=2, ensure_ascii=False)}],
                                         "isError": False})
                except (ToolError, ValueError, FileNotFoundError) as e:
                    return _result(mid, {"content": [{"type": "text", "text": str(e)}], "isError": True})
            if method == "prompts/list":
                return _result(mid, {"prompts": PROMPTS})
            if method == "prompts/get":
                if params.get("name") != "review-agent-design":
                    return _error(mid, -32602, "unknown prompt")
                design = str((params.get("arguments") or {}).get("design", ""))
                return _result(mid, {"description": PROMPTS[0]["description"], "messages": [{"role": "user", "content": {
                    "type": "text", "text": REVIEW_PROMPT.format(design=design)}}]})
            return _error(mid, -32601, f"method not found: {method}")
        except Exception as e:  # never let one bad request stop the server
            return _error(mid, -32603, f"internal error: {type(e).__name__}")


REVIEW_PROMPT = """Review this agent design against the AI Security Wiki Builder Track's ten controls
(B1 register and owner, B2 own identity, B3 scoped short-lived credentials, B4 allow-listed and pinned tools,
B5 argument validation outside the model, B6 approval for sensitive actions, B7 sandboxed code execution,
B8 egress allow-list, B9 limits and kill switch, B10 tamper-evident decision log).
For each control say whether the design meets it, what is missing, and which wiki test case would prove it.
Use the wiki_get and wiki_tests_for_control tools for IDs and links, and do not invent IDs.

Design:
{design}"""


def _result(mid, result: dict) -> dict:
    return {"jsonrpc": "2.0", "id": mid, "result": result}


def _error(mid, code: int, message: str) -> dict:
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": code, "message": message}}


def serve_stdio(server: Server, stdin=None, stdout=None) -> None:
    """Newline-delimited JSON-RPC over standard input and output."""
    stdin, stdout = stdin or sys.stdin, stdout or sys.stdout
    for line in stdin:
        if not line.strip():
            continue
        try:
            msg = json.loads(line)
        except ValueError:
            reply = _error(None, -32700, "parse error")
        else:
            reply = [r for r in map(server.handle, msg) if r] if isinstance(msg, list) else server.handle(msg)
        if reply:
            stdout.write(json.dumps(reply, ensure_ascii=False) + "\n")
            stdout.flush()


def make_http_handler(server: Server, token: str | None, allowed_hosts: set[str]):
    class Handler(BaseHTTPRequestHandler):
        server_version = f"{NAME}/{VERSION}"

        def log_message(self, *a):  # keep request bodies out of logs
            pass

        def _send(self, code: int, body: dict | None = None):
            data = json.dumps(body).encode() if body is not None else b""
            self.send_response(code)
            if body is not None:
                self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _allowed(self) -> bool:
            host = (self.headers.get("Host") or "").rsplit(":", 1)[0].strip("[]").lower()
            origin = self.headers.get("Origin")
            if host not in allowed_hosts:
                return False
            if origin and (urlsplit(origin).hostname or "").lower() not in allowed_hosts:
                return False
            if token:
                given = self.headers.get("Authorization", "")
                return hmac.compare_digest(given.encode(), f"Bearer {token}".encode())
            return True

        def do_POST(self):
            if urlsplit(self.path).path != "/mcp":
                return self._send(404, {"error": "not found"})
            if not self._allowed():
                return self._send(403, {"error": "forbidden"})
            length = int(self.headers.get("Content-Length") or 0)
            if length > MAX_TEXT * 2:
                return self._send(413, {"error": "request too large"})
            try:
                msg = json.loads(self.rfile.read(length) or b"null")
            except ValueError:
                return self._send(400, _error(None, -32700, "parse error"))
            reply = [r for r in map(server.handle, msg) if r] if isinstance(msg, list) else server.handle(msg)
            return self._send(200, reply) if reply else self._send(202)

        def do_GET(self):  # this server does not open a server-to-client stream
            self.send_response(405)
            self.send_header("Allow", "POST")
            self.end_headers()

        do_DELETE = do_GET

    return Handler


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="mcp_server", description="AI Security Wiki MCP server (read-only).")
    ap.add_argument("--data")
    ap.add_argument("--http", action="store_true")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--token", default=os.environ.get("AIWIKI_MCP_TOKEN"))
    ap.add_argument("--allow-host", action="append", default=[])
    a = ap.parse_args(argv)
    server = Server(a.data)
    if not a.http:
        # UTF-8 and bare newlines on every platform, including Windows consoles
        sys.stdin.reconfigure(encoding="utf-8")
        sys.stdout.reconfigure(encoding="utf-8", newline="\n")
        serve_stdio(server)
        return 0
    if a.host not in ("127.0.0.1", "localhost", "::1") and not a.token:
        print("mcp_server: refusing to listen beyond loopback without --token", file=sys.stderr)
        return 2
    hosts = {"127.0.0.1", "localhost", "::1", *(h.lower() for h in a.allow_host)}
    httpd = ThreadingHTTPServer((a.host, a.port), make_http_handler(server, a.token, hosts))
    print(f"mcp_server: listening on http://{a.host}:{a.port}/mcp", file=sys.stderr)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
