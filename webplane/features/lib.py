from eprint.str import info
import importlib
import sys
from pathlib import Path
from appframe import verbose


def activate(content_path):
    top_imports = Path(content_path).glob("*")
    if not top_imports:
        verbose(1, "No libraries to import")
    for import_name in top_imports:
        if import_name.name.startswith("__"):   # skip the __pycache_ dir
            continue
        verbose(1, info("Loading library {}", import_name))
        spec = importlib.util.spec_from_file_location(f"webplane.app.lib.{import_name.stem}", import_name.as_posix())
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[f"webplane.app.lib.{import_name.stem}"] = module
