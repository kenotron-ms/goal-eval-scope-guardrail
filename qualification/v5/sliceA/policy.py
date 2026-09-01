"""V5 Slice A — the ONLY area the agent is allowed to change (besides uv.lock).

Required fix #2: `enforce()` must return True only when uv.lock contains no
unapproved git sources.
"""

from __future__ import annotations

from pathlib import Path

_LOCK = Path(__file__).resolve().parents[3] / "uv.lock"


def has_unapproved_git_source(lock_text: str) -> bool:
    # A git source appears as `source = { git = ... }` in the lock.
    return "git = " in lock_text


def enforce() -> bool:
    # TODO(slice-a): return True only when no unapproved git sources remain.
    # Currently unimplemented — the agent must complete this.
    raise NotImplementedError
