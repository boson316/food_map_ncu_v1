from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Tests import `streamlit_app` helpers from src/, not the repo-root Cloud shim.
_app_path = SRC / "streamlit_app.py"
_spec = importlib.util.spec_from_file_location("streamlit_app", _app_path)
if _spec is not None and _spec.loader is not None:
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    sys.modules["streamlit_app"] = _mod
