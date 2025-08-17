"""Ensure tests can import the top-level ``apps`` package."""

import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
if str(root) not in sys.path:  # pragma: no cover - environment tweak
    sys.path.insert(0, str(root))

