# Run one agent job in a locked-down container, from Windows PowerShell or
# PowerShell 7 on any platform. The same flags as docker-sandbox.sh; see that
# file for what each one does.
#
# Not executed by this wiki's tests (they need a container runtime). Check each
# flag against your runtime's current documentation before relying on it, and
# pin the image by digest instead of by tag. With Docker Desktop on Windows the
# container is a Linux container, so the Linux flags below apply inside it.
param(
    [Parameter(Mandatory = $true)][string]$JobDir   # contains main.py
)
$ErrorActionPreference = "Stop"
$job = (Resolve-Path -LiteralPath $JobDir).Path

docker run --rm `
  --network none `
  --read-only `
  --tmpfs /tmp:rw,noexec,nosuid,size=64m `
  --cap-drop ALL `
  --security-opt no-new-privileges `
  --pids-limit 64 `
  --memory 256m --memory-swap 256m `
  --cpus 0.5 `
  --user 65534:65534 `
  -v "${job}:/job:ro" `
  python:3.13-slim `
  python -I /job/main.py
exit $LASTEXITCODE
