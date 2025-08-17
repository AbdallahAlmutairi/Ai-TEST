"""Ensure API tests can import the local `app` package."""

import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
if str(root) not in sys.path:  # pragma: no cover
    sys.path.insert(0, str(root))

