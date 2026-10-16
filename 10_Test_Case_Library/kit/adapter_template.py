"""Starting point for wrapping your own application so the runner can test it.

Copy this file, fill in `handle`, and run:

    python3 run_case.py --target python:my_adapter:handle --baseline python:my_adapter:handle_unprotected L06

The runner sends `handle` one request at a time (see ../payload-kit.md for every field)
and expects a dict back. Until you fill it in, it answers `not_applicable`, so the runner
reports "inconclusive" instead of a result that looks like a pass.

Keep the unprotected variant honest: it must be the same application with only the
protection you are testing switched off, in a lab, with mock tools.
"""
from __future__ import annotations


def handle(request: dict) -> dict:
    """Run one request through your application, protection on."""
    # 1. If request["reset"] is true, start a fresh conversation, memory and approval state.
    # 2. If "action" is present (kill, revoke_credentials, approve, reject), apply it and return {"output": "done", "tool_calls": []}.
    # 3. If "direct_call" is present, make that tool call through your normal policy layer as agent request.get("agent"),
    #    on behalf of request.get("user"), instead of asking the model.
    # 4. Otherwise send request["input"] and request["context"] to your application the way it normally receives them.
    # 5. Return {"output": <text the user would see>,
    #            "tool_calls": [{"tool": <name>, "args": <dict>, "decision": "executed" | "blocked" | "pending" | "error"}]}
    return {"not_applicable": True}


def handle_unprotected(request: dict) -> dict:
    """The same application with the protection under test turned off."""
    return {"not_applicable": True}
