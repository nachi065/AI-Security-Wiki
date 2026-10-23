"""Tests for pipeline_checks.py. Run:  python3 -m unittest -v test_pipeline_checks   (from this folder)"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from pipeline_checks import (added_lines, check_trailer, personal_fields, scan_diff, scan_log_lines,
                             scan_secrets)

HERE = Path(__file__).parent
FIELDS = personal_fields(HERE / "privacy_map.json")
# Built from parts so that this file does not itself contain a secret-shaped string.
PEM = "-----BEGIN " + "RSA PRIVATE KEY-----"
AWS = "AKIA" + "ABCDEFGHIJKLMNOP"
GH = "ghp_" + "a" * 36


class SecretTests(unittest.TestCase):
    def test_finds_common_formats(self):
        for text in (PEM, f'key = "{AWS}"', f"token: {GH}", 'db_password = "Zq8vY2mL0pXr7TkW3nBs"'):
            self.assertTrue(scan_secrets(text), text)

    def test_private_key_pattern_starting_with_dashes(self):
        # A shell `grep -P "$p"` reads a pattern that starts with dashes as an option and
        # silently matches nothing. Python's re has no such failure; keep it tested.
        self.assertEqual(scan_secrets(PEM)[0].detail, "private key block")

    def test_ignores_placeholders_and_plain_code(self):
        for text in ('api_key = "your_api_key_goes_here_123"', 'password = "${DB_PASSWORD_FROM_VAULT}"',
                     "def get_token(user): return issuer.mint(user)"):
            self.assertEqual(scan_secrets(text), [], text)


class LogTests(unittest.TestCase):
    def test_flags_personal_field_in_log_call(self):
        self.assertTrue(scan_log_lines("logger.info('lookup', email)", FIELDS))
        self.assertTrue(scan_log_lines("console.log(user.phone)", FIELDS))

    def test_ignores_non_personal_and_non_log(self):
        self.assertEqual(scan_log_lines("logger.info('done', request_id)", FIELDS), [])
        self.assertEqual(scan_log_lines("send_mail(email)", FIELDS), [])


class TrailerTests(unittest.TestCase):
    def test_requires_trailer(self):
        self.assertTrue(check_trailer("Fix login bug\n"))
        for value in ("none", "suggestions", "agent"):
            self.assertEqual(check_trailer(f"Fix login bug\n\nAI-Assistance: {value}\n"), [])

    def test_comment_lines_do_not_count(self):
        self.assertTrue(check_trailer("Fix\n# AI-Assistance: agent\n"))


class DiffTests(unittest.TestCase):
    DIFF = (
        "diff --git a/app.py b/app.py\n--- a/app.py\n+++ b/app.py\n@@ -1 +1,2 @@\n"
        "-old = 1\n+print(email)\n+x = 1\n"
        "diff --git a/package-lock.json b/package-lock.json\n--- a/package-lock.json\n"
        f"+++ b/package-lock.json\n@@ -1 +1 @@\n+\"integrity\": \"{AWS}\"\n"
    )

    def test_only_added_lines_and_skips_lockfiles(self):
        self.assertEqual(added_lines(self.DIFF)["app.py"], "print(email)\nx = 1")
        findings = scan_diff(self.DIFF, FIELDS)
        self.assertEqual([f.check for f in findings], ["personal-data-in-log"])
        self.assertTrue(findings[0].where.startswith("app.py:"))


@unittest.skipUnless(shutil.which("git"), "git is not installed")
class GitHookTests(unittest.TestCase):
    """The checks wired in as real git hooks in a throwaway repository."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        env = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.com",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.com"}
        self.env = {**os.environ, **env}
        self.git("init", "-q")
        hooks = self.repo / ".git" / "hooks"
        script = HERE / "pipeline_checks.py"
        for hook, args in (("pre-commit", "pre-commit"), ("commit-msg", 'commit-msg "$1"')):
            (hooks / hook).write_text(f'#!/bin/sh\nexec "{sys.executable}" "{script}" {args}\n')
            (hooks / hook).chmod(0o755)

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args, check=True):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env, capture_output=True, text=True,
                              check=check)

    def commit(self, name, content, message):
        (self.repo / name).write_text(content)
        self.git("add", name)
        return self.git("commit", "-q", "-m", message, check=False)

    def test_secret_blocks_commit(self):
        r = self.commit("a.py", f'k = "{AWS}"\n', "Add\n\nAI-Assistance: none")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("AWS access key ID", r.stderr)

    def test_missing_trailer_blocks_commit(self):
        r = self.commit("a.py", "x = 1\n", "Add")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("AI-Assistance", r.stderr)

    def test_clean_change_commits(self):
        r = self.commit("a.py", "x = 1\n", "Add\n\nAI-Assistance: agent")
        self.assertEqual(r.returncode, 0, r.stderr)


if __name__ == "__main__":
    unittest.main()
