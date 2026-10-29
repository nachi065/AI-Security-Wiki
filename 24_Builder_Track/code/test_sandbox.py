"""Tests for sandbox.py. Run:  python3 -m unittest -v test_sandbox   (from this folder)"""
import os
import unittest

from sandbox import netns_available, run_python


class Sandbox(unittest.TestCase):
    def test_normal_code_runs(self):
        r = run_python("print(2 + 2)")
        self.assertEqual((r.ok, r.stdout.strip()), (True, "4"))

    def test_infinite_loop_is_stopped(self):
        r = run_python("while True: pass", timeout=3, cpu_seconds=1)
        self.assertFalse(r.ok)

    def test_sleep_is_stopped_by_wall_clock(self):
        r = run_python("import time; time.sleep(30)", timeout=1)
        self.assertTrue(r.timed_out)

    def test_memory_bomb_is_stopped(self):
        r = run_python("x = bytearray(2 * 1024**3)", memory_mb=128)
        self.assertFalse(r.ok)
        self.assertIn("MemoryError", r.stderr)

    @unittest.skipIf(os.name == "nt", "Windows has no per-process file-size limit; sandbox.py reports this in result.limits")
    def test_large_file_write_is_stopped(self):
        r = run_python("open('big', 'wb').write(b'x' * (5 * 1024 * 1024))", file_mb=1)
        self.assertFalse(r.ok)

    def test_environment_is_empty(self):
        os.environ["AGENT_SECRET_TOKEN"] = "do-not-leak"
        try:
            r = run_python("import os; print(sorted(os.environ))")
        finally:
            del os.environ["AGENT_SECRET_TOKEN"]
        self.assertNotIn("AGENT_SECRET_TOKEN", r.stdout)
        self.assertNotIn("do-not-leak", r.stdout)

    def test_result_says_which_limits_applied(self):
        r = run_python("print(1)")
        for limit in ("cpu", "memory", "processes", "timeout", "empty-env"):
            self.assertIn(limit, r.limits)
        self.assertEqual("file-size" in r.limits, os.name != "nt")
        self.assertEqual("no-network" in r.limits, r.network_isolated)

    def test_output_is_capped(self):
        r = run_python("print('a' * 100000)", max_output=1000)
        self.assertEqual((len(r.stdout), r.truncated), (1000, True))

    def test_working_directory_is_throwaway(self):
        r = run_python("import os; open('note.txt', 'w').write('x'); print(os.getcwd())")
        self.assertIn("sandbox-", r.stdout)
        self.assertFalse(os.path.exists(r.stdout.strip()))

    @unittest.skipUnless(netns_available(), "needs `unshare --net` (Linux, usually root or user namespaces)")
    def test_no_network_when_namespace_available(self):
        code = ("import socket\n"
                "s = socket.socket()\n"
                "s.settimeout(2)\n"
                "try:\n"
                "    s.connect(('93.184.216.34', 80)); print('CONNECTED')\n"
                "except OSError as e:\n"
                "    print('BLOCKED', type(e).__name__)\n")
        r = run_python(code)
        self.assertTrue(r.network_isolated)
        self.assertIn("BLOCKED", r.stdout)
        self.assertNotIn("CONNECTED", r.stdout)

    def test_can_require_isolation(self):
        if netns_available():
            self.skipTest("isolation is available here")
        with self.assertRaises(RuntimeError):
            run_python("print(1)", require_network_isolation=True)


if __name__ == "__main__":
    unittest.main()
