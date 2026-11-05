"""Select the learner by default; CI explicitly opts into worked examples."""
import importlib.util
import os
from pathlib import Path
import pytest


@pytest.fixture
def project():
    implementation = os.environ.get("BEGINNER_IMPL", "starter")
    if implementation not in {"starter", "reference"}:
        raise ValueError("BEGINNER_IMPL must be starter or reference")

    def load(name):
        path = Path(__file__).parents[1] / name / f"{implementation}.py"
        spec = importlib.util.spec_from_file_location(f"beginner_{name}_{implementation}", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    return load
