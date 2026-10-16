"""Pin tool definitions: write each tool's definition hash into policy.json.

Run this after a person has reviewed tool_definitions.json, and commit the
result. At run time the guard compares the definition your framework or MCP
server presents with this pin and refuses a mismatch.

Usage: python3 pin_definitions.py [policy.json] [tool_definitions.json]
"""
import json
import sys
from pathlib import Path

from guard import definition_hash, description_findings

policy_path = Path(sys.argv[1] if len(sys.argv) > 1 else "policy.json")
defs_path = Path(sys.argv[2] if len(sys.argv) > 2 else "tool_definitions.json")
policy = json.loads(policy_path.read_text())
definitions = json.loads(defs_path.read_text())

for name, spec in policy["tools"].items():
    findings = description_findings(definitions[name])
    if findings:
        sys.exit(f"{name}: review needed before pinning: {', '.join(findings)}")
    spec["definition_sha256"] = definition_hash(definitions[name])
    print(f"pinned {name}: {spec['definition_sha256'][:16]}...")

policy_path.write_text(json.dumps(policy, indent=2) + "\n")
