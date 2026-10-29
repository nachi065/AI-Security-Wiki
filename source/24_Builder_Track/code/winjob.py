"""A Windows Job Object that caps CPU time, memory and process count for a
child process and kills it with everything it started when closed. Used by
sandbox.py on Windows, where the Unix resource limits do not exist.

Standard library only (ctypes). Windows only.
"""
from __future__ import annotations

import ctypes
from ctypes import wintypes

JobObjectExtendedLimitInformation = 9
LIMIT_PROCESS_TIME = 0x00000002
LIMIT_ACTIVE_PROCESS = 0x00000008
LIMIT_PROCESS_MEMORY = 0x00000100
LIMIT_DIE_ON_UNHANDLED_EXCEPTION = 0x00000400
LIMIT_KILL_ON_JOB_CLOSE = 0x00002000


class _Basic(ctypes.Structure):
    _fields_ = [("PerProcessUserTimeLimit", ctypes.c_int64), ("PerJobUserTimeLimit", ctypes.c_int64),
                ("LimitFlags", wintypes.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t),
                ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", wintypes.DWORD),
                ("Affinity", ctypes.c_size_t), ("PriorityClass", wintypes.DWORD), ("SchedulingClass", wintypes.DWORD)]


class _Io(ctypes.Structure):
    _fields_ = [(n, ctypes.c_uint64) for n in ("ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
                                               "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]


class _Extended(ctypes.Structure):
    _fields_ = [("BasicLimitInformation", _Basic), ("IoInfo", _Io), ("ProcessMemoryLimit", ctypes.c_size_t),
                ("JobMemoryLimit", ctypes.c_size_t), ("PeakProcessMemoryUsed", ctypes.c_size_t),
                ("PeakJobMemoryUsed", ctypes.c_size_t)]


class Job:
    def __init__(self, cpu_seconds: int, memory_mb: int, processes: int):
        k = ctypes.WinDLL("kernel32", use_last_error=True)
        k.CreateJobObjectW.restype = wintypes.HANDLE
        k.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
        k.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
        k.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
        k.TerminateJobObject.argtypes = [wintypes.HANDLE, wintypes.UINT]
        k.CloseHandle.argtypes = [wintypes.HANDLE]
        self._k = k
        self.handle = k.CreateJobObjectW(None, None)
        if not self.handle:
            raise ctypes.WinError(ctypes.get_last_error())
        info = _Extended()
        b = info.BasicLimitInformation
        b.LimitFlags = (LIMIT_PROCESS_TIME | LIMIT_ACTIVE_PROCESS | LIMIT_PROCESS_MEMORY
                        | LIMIT_DIE_ON_UNHANDLED_EXCEPTION | LIMIT_KILL_ON_JOB_CLOSE)
        b.PerProcessUserTimeLimit = cpu_seconds * 10_000_000          # 100-nanosecond units
        b.ActiveProcessLimit = processes
        info.ProcessMemoryLimit = memory_mb << 20
        if not k.SetInformationJobObject(self.handle, JobObjectExtendedLimitInformation,
                                         ctypes.byref(info), ctypes.sizeof(info)):
            err = ctypes.get_last_error()
            self.close()
            raise ctypes.WinError(err)

    def assign(self, proc) -> None:
        """Put a subprocess.Popen child in the job; kill it if that fails."""
        if not self._k.AssignProcessToJobObject(self.handle, int(proc._handle)):
            err = ctypes.get_last_error()
            proc.kill()
            raise ctypes.WinError(err)

    def kill(self) -> None:
        self._k.TerminateJobObject(self.handle, 1)

    def close(self) -> None:
        if self.handle:
            self._k.CloseHandle(self.handle)
            self.handle = None
