"""Run model-generated Python with hard limits.

Standard library only, Python 3.10 or later, on Linux, macOS or Windows.

What this gives you: a separate process with CPU, memory, file-size and
process-count limits, a wall-clock timeout, an empty environment, a throwaway
working directory, no stdin, capped output, and (on Linux, when the kernel
allows it) a network namespace with no network.

On Windows the limits come from a Job Object instead of resource limits:
CPU time, memory, process count and kill-on-close are enforced, but there is
no file-size limit and no network removal (SandboxResult.limits lists what
was applied). The child is assigned to the job just after it starts, so its
first instructions run before the limits; keep the container as the boundary.

What it does not give you: a security boundary. Code in this process can still
read any file the parent user can read. Treat these limits as hygiene and run
this inside a container or microVM that provides the real boundary; see
docker-sandbox.sh and k8s-agent-pod.yaml in this folder.
"""
from __future__ import annotations

import os
import shutil
import signal
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field

WINDOWS = os.name == "nt"
if WINDOWS:
    import winjob
else:
    import resource


@dataclass
class SandboxResult:
    ok: bool
    stdout: str
    stderr: str
    returncode: int | None
    timed_out: bool
    truncated: bool
    network_isolated: bool
    limits: list[str] = field(default_factory=list)   # the limits this platform actually applied


def netns_available() -> bool:
    """True if `unshare --net` works for this user."""
    if WINDOWS:
        return False
    exe = shutil.which("unshare")
    if not exe:
        return False
    try:
        return subprocess.run([exe, "--net", "true"], capture_output=True, timeout=5).returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def _limits(cpu_seconds: int, memory_mb: int, file_mb: int, processes: int):
    def apply():
        os.setsid()                                                    # own session, so we can kill the group
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
        resource.setrlimit(resource.RLIMIT_AS, (memory_mb << 20, memory_mb << 20))
        resource.setrlimit(resource.RLIMIT_FSIZE, (file_mb << 20, file_mb << 20))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
        if hasattr(resource, "RLIMIT_NPROC"):
            resource.setrlimit(resource.RLIMIT_NPROC, (processes, processes))
    return apply


def run_python(code: str, timeout: int = 5, cpu_seconds: int = 3, memory_mb: int = 256,
               file_mb: int = 1, processes: int = 32, max_output: int = 20_000,
               require_network_isolation: bool = False) -> SandboxResult:
    isolated = netns_available()
    if require_network_isolation and not isolated:
        raise RuntimeError("network isolation is not available here; run inside a container with --network none")
    workdir = tempfile.mkdtemp(prefix="sandbox-")
    command = [sys.executable, "-I", "-c", code]
    if isolated:
        command = [shutil.which("unshare"), "--net"] + command
    job = None
    try:
        if WINDOWS:
            env = {"SYSTEMROOT": os.environ.get("SYSTEMROOT", r"C:\Windows")}  # Python needs it to start
            proc = subprocess.Popen(command, cwd=workdir, env=env, stdin=subprocess.DEVNULL,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            job = winjob.Job(cpu_seconds=cpu_seconds, memory_mb=memory_mb, processes=processes)
            job.assign(proc)
            limits = ["cpu", "memory", "processes", "timeout", "empty-env", "temp-dir"]
        else:
            proc = subprocess.Popen(
                command, cwd=workdir, env={"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8"},
                stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                preexec_fn=_limits(cpu_seconds, memory_mb, file_mb, processes),
            )
            limits = ["cpu", "memory", "file-size", "processes", "open-files", "timeout", "empty-env", "temp-dir"]
            limits += ["no-network"] if isolated else []
        timed_out = False
        try:
            out, err = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            if job:
                job.kill()
            else:
                os.killpg(proc.pid, signal.SIGKILL)
            out, err = proc.communicate()
        truncated = len(out) > max_output or len(err) > max_output
        return SandboxResult(
            ok=(proc.returncode == 0 and not timed_out),
            stdout=out[:max_output].decode("utf-8", "replace"),
            stderr=err[:max_output].decode("utf-8", "replace"),
            returncode=proc.returncode, timed_out=timed_out, truncated=truncated,
            network_isolated=isolated, limits=limits,
        )
    finally:
        if job:
            job.close()
        shutil.rmtree(workdir, ignore_errors=True)
