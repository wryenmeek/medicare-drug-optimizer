# tests/integration/test_dependency_management.py

import pytest
import subprocess
import toml

def test_add_dependency():
    # Add a dummy dependency
    result = subprocess.run(["poetry", "add", "requests-mock", "--group=dev"], capture_output=True, text=True, check=True)
    assert result.returncode == 0
    assert "requests-mock" in result.stdout

    # Verify it's in pyproject.toml
    with open("pyproject.toml", "r") as f:
        pyproject_data = toml.load(f)
    assert "requests-mock" in pyproject_data["tool"]["poetry"]["group"]["dev"]["dependencies"]

def test_update_dependency():
    # Update a dummy dependency (assuming it's already added)
    # For a real test, we'd add a specific version first, then update
    result = subprocess.run(["poetry", "update", "requests-mock"], capture_output=True, text=True, check=True)
    assert result.returncode == 0
    assert "Updating requests-mock" in result.stdout
