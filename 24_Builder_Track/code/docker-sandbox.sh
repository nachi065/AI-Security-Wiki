#!/bin/sh
# Run one agent job in a locked-down container.
#
# Not executed by this wiki's tests (they need a container runtime). Check each
# flag against your runtime's current documentation before relying on it, and
# pin the image by digest instead of by tag.
#
#   --network none            no network at all; use the egress proxy pattern if the job needs some
#   --read-only               root filesystem is read-only
#   --tmpfs /tmp ...          the only writable place, in memory, no exec
#   --cap-drop ALL            no Linux capabilities
#   no-new-privileges         setuid binaries cannot raise privileges
#   --pids-limit              fork bombs stop here
#   --memory / --memory-swap  equal values mean no swap
#   --user                    unprivileged user
#   job mounted read-only     the code under test cannot rewrite itself
set -eu

JOB_DIR="${1:?usage: docker-sandbox.sh JOB_DIR}"   # contains main.py

exec docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --pids-limit 64 \
  --memory 256m --memory-swap 256m \
  --cpus 0.5 \
  --user 65534:65534 \
  -v "$JOB_DIR":/job:ro \
  python:3.13-slim \
  python -I /job/main.py
