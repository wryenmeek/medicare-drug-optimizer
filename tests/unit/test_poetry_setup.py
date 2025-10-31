# tests/unit/test_poetry_setup.py

import pytest
import subprocess
import os

def test_poetry_installation_script():
    # This is a placeholder test. A real test would involve:
    # 1. Running the poetry_setup.ps1 script.
    # 2. Verifying that poetry is installed and configured correctly.
    # 3. Cleaning up any changes made by the script.

    # For now, we'll just assert that the script exists.
    script_path = os.path.abspath(".specify/scripts/powershell/poetry_setup.ps1")
    assert os.path.exists(script_path)

    # You could also try to execute it and check for specific output
    # result = subprocess.run(["powershell.exe", "-File", script_path], capture_output=True, text=True)
    # assert "Poetry setup complete." in result.stdout
    # assert result.returncode == 0
