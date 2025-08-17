"""Helper package for tests to import the FastAPI application."""

from pathlib import Path
import sys

_ROOT = Path(__file__).resolve().parents[2] / "app"
ROOT_PARENT = _ROOT.parents[1]
if str(ROOT_PARENT.parent) not in sys.path:  # pragma: no cover
    sys.path.insert(0, str(ROOT_PARENT.parent))
if str(_ROOT.parent) not in sys.path:
    sys.path.insert(0, str(_ROOT.parent))
__path__ = [str(_ROOT)]  # type: ignore[var-annotated]

