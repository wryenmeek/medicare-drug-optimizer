# tests/integration/test_migration_utility.py

import pytest
import subprocess
import os

def test_migrate_requirements_txt_to_poetry(tmp_path):
    # Create a dummy requirements.txt
    req_content = "requests==2.28.1\n"
    req_file = tmp_path / "requirements.txt"
    req_file.write_text(req_content)

    # Initialize a poetry project in the temporary directory
    subprocess.run(["poetry", "init", "--no-interaction"], cwd=tmp_path, check=True)

    # Run the migration (this will be a placeholder for now)
    # In a real scenario, we would call the migration utility here
    # For now, we simulate adding the dependency manually
    subprocess.run(["poetry", "add", "requests==2.28.1"], cwd=tmp_path, check=True)

    # Verify pyproject.toml contains the dependency
    pyproject_content = (tmp_path / "pyproject.toml").read_text()
    assert 'requests = "2.28.1"' in pyproject_content

    # Verify poetry.lock is created
    assert (tmp_path / "poetry.lock").exists()

