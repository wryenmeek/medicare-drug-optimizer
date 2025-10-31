# tests/integration/test_poetry_installation.py

import pytest
import subprocess

def test_poetry_is_installed():
    try:
        # Run poetry --version to check if it's installed
        result = subprocess.run(["poetry", "--version"], capture_output=True, text=True, check=True)
        assert "Poetry version" in result.stdout
    except FileNotFoundError:
        pytest.fail("Poetry command not found. Is it installed and in PATH?")

def test_poetry_init_creates_pyproject_toml():
    # This test assumes a clean directory or a temporary one
    # For integration tests, we might need a more isolated setup
    # For now, we'll just check if pyproject.toml exists after init
    # (This is more of a functional test, but serves the purpose for now)
    try:
        subprocess.run(["poetry", "init", "--no-interaction"], capture_output=True, text=True, check=True)
        assert "pyproject.toml" in subprocess.run(["ls"], capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Poetry init failed: {e.stderr}")
