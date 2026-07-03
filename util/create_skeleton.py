#!/usr/bin/env python3
"""Convenience wrapper for the skeleton skill CLI."""

from pathlib import Path
import runpy


SCRIPT = Path(__file__).resolve().parent / "skills" / "skeleton" / "scripts" / "create_skeleton.py"
runpy.run_path(str(SCRIPT), run_name="__main__")
