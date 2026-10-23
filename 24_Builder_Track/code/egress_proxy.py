"""A small allow-list forward proxy for agent egress.

Standard library only, Python 3.10 or later. Point the agent's HTTPS_PROXY
and HTTP_PROXY at it and block every other route at the network layer (see
k8s-agent-pod.yaml), so the proxy is the only way out.

For each request it checks, in order:
  1. the destination port is on the allow-list;
  2. the destination host name is on the allow-list;
  3. every address the name resolves to is public (no loopback, private,
     link-local such as the cloud metadata address, or reserved ranges);
  4. it then connects to the address it just checked, not to the name, so a
     DNS answer that changes between check and connect cannot redirect it.

It handles CONNECT tunnels (HTTPS) and plain absolute-URI GET requests. It
does not inspect the encrypted content of a tunnel; it controls where the
agent can connect, not what it sends there. Pair it with the argument
validation in guard.py and with data loss controls where content matters.
"""
from __future__ import annotations

import ipaddress
import json
import select
import socket
import socketserver
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlsplit


def host_allowed(host: str, allowed: list[str]) -> bool:
    host = host.lower().rstrip(".")
    for pattern in (p.lower() for p in allowed):
        if pattern.startswith("*."):
            if host.endswith(pattern[1:]) and host != pattern[2:]:
                return True
        elif host == pattern:
            return True
    return False


def is_public(address: str) -> bool:
    ip = ipaddress.ip_address(address)
    return not (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_multicast
                or ip.is_reserved or ip.is_unspecified)


class EgressPolicy:
    def __init__(self, hosts: list[str], ports: tuple[int, ...] = (443,), allow_private: bool = False):
        self.hosts, self.ports, self.allow_private = hosts, tuple(ports), allow_private

    def resolve(self, host: str, port: int) -> tuple[list[str], str]:
        """(checked addresses to connect to, in order; empty if denied) and the reason."""
        if port not in self.ports:
            return [], f"port {port} not allowed"
        if not host_allowed(host, self.hosts):
            return [], "host not on the allow-list"
        try:
            infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
        except socket.gaierror:
            return [], "host does not resolve"
        addresses = list(dict.fromkeys(i[4][0] for i in infos))
        if not self.allow_private and not all(is_public(a) for a in addresses):
            return [], "resolves to a non-public address"
        return addresses, "ok"

    def check(self, host: str, port: int) -> tuple[str | None, str]:
        """(first address to connect to, or None) and the reason."""
        addresses, why = self.resolve(host, port)
        return (addresses[0] if addresses else None), why


def connect_checked(addresses: list[str], port: int) -> tuple[socket.socket, str]:
    """Connect to the first checked address that answers. A dual-stack name often
    lists an IPv6 address first; trying only that one fails where the service
    listens on IPv4. Every address here was checked, so none can be a surprise."""
    error: OSError = OSError("no address")
    for address in addresses:
        try:
            return socket.create_connection((address, port), timeout=10), address
        except OSError as e:
            error = e
    raise error


def make_handler(policy: EgressPolicy, log):
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.0"

        def log_message(self, *args):  # we write our own structured log
            pass

        def _deny(self, host, port, why):
            log({"ts": round(time.time(), 3), "decision": "deny", "host": host, "port": port, "reason": why})
            self.send_error(403, "egress denied")

        def do_CONNECT(self):
            host, _, port = self.path.rpartition(":")
            try:
                port = int(port)
            except ValueError:
                return self._deny(self.path, 0, "bad target")
            addresses, why = policy.resolve(host, port)
            if not addresses:
                return self._deny(host, port, why)
            try:
                upstream, address = connect_checked(addresses, port)
            except OSError:
                return self._deny(host, port, "connect failed")
            log({"ts": round(time.time(), 3), "decision": "allow", "host": host, "port": port, "address": address})
            self.send_response(200, "Connection established")
            self.end_headers()
            self._pipe(self.connection, upstream)

        def do_GET(self):
            parts = urlsplit(self.path)
            if parts.scheme != "http" or not parts.hostname:
                return self._deny(self.path, 0, "only absolute http URLs are proxied; use CONNECT for https")
            port = parts.port or 80
            addresses, why = policy.resolve(parts.hostname, port)
            if not addresses:
                return self._deny(parts.hostname, port, why)
            try:
                upstream, address = connect_checked(addresses, port)
                target = (parts.path or "/") + (f"?{parts.query}" if parts.query else "")
                upstream.sendall(f"GET {target} HTTP/1.0\r\nHost: {parts.netloc}\r\nConnection: close\r\n\r\n".encode())
            except OSError:
                return self._deny(parts.hostname, port, "connect failed")
            log({"ts": round(time.time(), 3), "decision": "allow", "host": parts.hostname, "port": port, "address": address})
            while True:
                chunk = upstream.recv(65536)
                if not chunk:
                    break
                self.wfile.write(chunk)
            upstream.close()

        do_POST = do_PUT = do_DELETE = do_PATCH = lambda self: self._deny(self.path, 0, "method not allowed")

        @staticmethod
        def _pipe(a, b):
            sockets = [a, b]
            try:
                while True:
                    readable, _, broken = select.select(sockets, [], sockets, 30)
                    if broken or not readable:
                        break
                    for s in readable:
                        data = s.recv(65536)
                        if not data:
                            return
                        (b if s is a else a).sendall(data)
            finally:
                b.close()

    return Handler


class ThreadingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


def serve(policy: EgressPolicy, host: str = "127.0.0.1", port: int = 3128, log=None) -> ThreadingServer:
    log = log or (lambda entry: print(json.dumps(entry), file=sys.stderr, flush=True))
    server = ThreadingServer((host, port), make_handler(policy, log))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


if __name__ == "__main__":
    allowed = sys.argv[1].split(",") if len(sys.argv) > 1 else ["docs.example.com"]
    srv = serve(EgressPolicy(allowed), host="0.0.0.0", port=3128)
    print(f"egress proxy on :3128, allowing {allowed}", file=sys.stderr)
    threading.Event().wait()
