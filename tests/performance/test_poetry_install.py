# tests/performance/test_poetry_install.py

import pytest
import subprocess
import time

def test_poetry_install_performance():
    start_time = time.time()
    # Run poetry install in a subprocess
    result = subprocess.run(["poetry", "install", "--no-root"], capture_output=True, text=True, cwd=".")
    end_time = time.time()
    
    # Assert that the command was successful
    assert result.returncode == 0, f"Poetry install failed: {result.stderr}"
    
    # Assert that the installation time is within the performance goal (less than 5 minutes)
    duration = end_time - start_time
    print(f"\nPoetry install took {duration:.2f} seconds.")
    assert duration < 300, f"Poetry install took {duration:.2f} seconds, which is more than 5 minutes."
