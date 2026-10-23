"""Tests for egress_proxy.py. Run:  python3 -m unittest -v test_egress_proxy   (from this folder)

The tests start a throwaway web server on the loopback address and a proxy in
front of it. They need no internet access."""
import http.client
import socket
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from unittest import mock

import egress_proxy
from egress_proxy import EgressPolicy, is_public, serve


class Origin(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"hello from origin"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


class Proxy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.origin = HTTPServer(("127.0.0.1", 0), Origin)
        cls.origin_port = cls.origin.server_address[1]
        threading.Thread(target=cls.origin.serve_forever, daemon=True).start()
        cls.log = []
        # allow_private only because the test origin is on loopback
        policy = EgressPolicy(["localhost", "*.docs.example.com"], ports=(cls.origin_port, 443), allow_private=True)
        cls.proxy = serve(policy, port=0, log=cls.log.append)
        cls.proxy_port = cls.proxy.server_address[1]
        # a strict policy for the checks that must not allow private ranges
        cls.strict = EgressPolicy(["localhost", "metadata.internal", "docs.example.com"], ports=(443, 80))

    @classmethod
    def tearDownClass(cls):
        cls.origin.shutdown()
        cls.proxy.shutdown()

    def get_via_proxy(self, host, port):
        conn = http.client.HTTPConnection("127.0.0.1", self.proxy_port, timeout=5)
        conn.request("GET", f"http://{host}:{port}/", headers={"Host": f"{host}:{port}"})
        r = conn.getresponse()
        return r.status, r.read()

    def test_allowed_host_and_port_is_proxied(self):
        status, body = self.get_via_proxy("localhost", self.origin_port)
        self.assertEqual((status, body), (200, b"hello from origin"))

    def test_ipv6_first_answer_falls_back_to_the_next_checked_address(self):
        # Dual-stack hosts (CI runners among them) list ::1 before 127.0.0.1 for
        # localhost; the origin listens on IPv4 only, so the proxy must try the next one.
        answers = [(10, 1, 6, "", ("::1", self.origin_port, 0, 0)), (2, 1, 6, "", ("127.0.0.1", self.origin_port))]
        real = socket.getaddrinfo
        fake = lambda host, *a, **k: answers if host == "localhost" else real(host, *a, **k)
        with mock.patch("egress_proxy.socket.getaddrinfo", side_effect=fake):
            status, body = self.get_via_proxy("localhost", self.origin_port)
        self.assertEqual((status, body), (200, b"hello from origin"))

    def test_host_not_on_list_is_denied(self):
        status, _ = self.get_via_proxy("evil.example.net", self.origin_port)
        self.assertEqual(status, 403)
        self.assertEqual(self.log[-1]["reason"], "host not on the allow-list")

    def test_port_not_on_list_is_denied(self):
        status, _ = self.get_via_proxy("localhost", self.origin_port + 1)
        self.assertEqual(status, 403)
        self.assertIn("not allowed", self.log[-1]["reason"])

    def test_ip_literal_is_denied_unless_listed(self):
        status, _ = self.get_via_proxy("127.0.0.1", self.origin_port)
        self.assertEqual(status, 403)

    def test_connect_to_listed_host_opens_tunnel(self):
        s = socket.create_connection(("127.0.0.1", self.proxy_port), timeout=5)
        s.sendall(f"CONNECT localhost:{self.origin_port} HTTP/1.1\r\nHost: localhost\r\n\r\n".encode())
        self.assertIn(b"200", s.recv(1024).split(b"\r\n")[0])
        s.sendall(b"GET / HTTP/1.0\r\n\r\n")
        data = b""
        while chunk := s.recv(4096):
            data += chunk
        self.assertIn(b"hello from origin", data)
        s.close()

    def test_connect_to_unlisted_host_is_denied(self):
        s = socket.create_connection(("127.0.0.1", self.proxy_port), timeout=5)
        s.sendall(b"CONNECT evil.example.net:443 HTTP/1.1\r\nHost: evil.example.net\r\n\r\n")
        self.assertIn(b"403", s.recv(1024).split(b"\r\n")[0])
        s.close()

    def test_post_is_refused(self):
        conn = http.client.HTTPConnection("127.0.0.1", self.proxy_port, timeout=5)
        conn.request("POST", f"http://localhost:{self.origin_port}/", body=b"x")
        self.assertEqual(conn.getresponse().status, 403)

    def test_metadata_address_is_refused_even_if_the_name_is_listed(self):
        with mock.patch("egress_proxy.socket.getaddrinfo", return_value=[(2, 1, 6, "", ("169.254.169.254", 80))]):
            address, why = self.strict.check("metadata.internal", 80)
        self.assertEqual((address, why), (None, "resolves to a non-public address"))

    def test_mixed_answers_are_refused(self):
        answers = [(2, 1, 6, "", ("93.184.216.34", 443)), (2, 1, 6, "", ("10.0.0.5", 443))]
        with mock.patch("egress_proxy.socket.getaddrinfo", return_value=answers):
            address, _ = self.strict.check("docs.example.com", 443)
        self.assertIsNone(address)

    def test_connects_to_the_address_it_checked(self):
        with mock.patch("egress_proxy.socket.getaddrinfo", return_value=[(2, 1, 6, "", ("93.184.216.34", 443))]):
            address, why = self.strict.check("docs.example.com", 443)
        self.assertEqual((address, why), ("93.184.216.34", "ok"))

    def test_address_classes(self):
        for private in ("127.0.0.1", "10.1.2.3", "172.16.0.9", "192.168.1.1", "169.254.169.254", "::1", "fe80::1", "0.0.0.0"):
            self.assertFalse(is_public(private), private)
        self.assertTrue(is_public("93.184.216.34"))


if __name__ == "__main__":
    unittest.main()
