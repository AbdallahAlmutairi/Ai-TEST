"""Ensure project root is on ``sys.path`` during tests.

Pytest may set the working directory to this package which would otherwise
prevent importing the top-level ``apps`` package.  Python automatically loads
``sitecustomize`` modules on startup, so we insert the repository root here.
"""

import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
if str(root) not in sys.path:  # pragma: no cover - simple path fix
    sys.path.insert(0, str(root))

