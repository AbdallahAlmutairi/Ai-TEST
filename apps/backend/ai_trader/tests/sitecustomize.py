"""Test configuration to add project root to sys.path."""

import sys
from pathlib import Path

root = Path(__file__).resolve().parents[3]
if str(root) not in sys.path:  # pragma: no cover
    sys.path.insert(0, str(root))

