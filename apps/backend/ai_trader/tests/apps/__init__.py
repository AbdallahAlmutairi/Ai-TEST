"""Helper package so tests can import ``apps.backend``.

This package forwards lookups to the real project ``apps`` package one level
above the tests directory.
"""

from pathlib import Path
import sys

# Discover the actual ``apps`` directory located at the project root and ensure
# the project root itself is on ``sys.path`` so that sibling packages like
# ``ai_service`` can be imported.
_ROOT = Path(__file__).resolve().parents[4]
if str(_ROOT.parent) not in sys.path:  # pragma: no cover - path setup
    sys.path.insert(0, str(_ROOT.parent))
__path__ = [str(_ROOT)]  # type: ignore[var-annotated]

