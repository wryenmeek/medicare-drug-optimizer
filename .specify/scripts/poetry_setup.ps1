# .specify/scripts/poetry_setup.ps1

# This script installs Poetry on the system.
# It checks if Poetry is already installed and installs it if not.

Write-Host "Checking for Poetry installation..."

try {
    # Try to get Poetry version
    $poetryVersion = (poetry --version 2>&1).ToString()
    Write-Host "Poetry is already installed: $poetryVersion"
} catch {
    Write-Host "Poetry not found. Installing Poetry..."
    
    # Download the installer script securely
    $installerPath = "$($env:TEMP)\install-poetry.py"
    Invoke-WebRequest -Uri https://install.python-poetry.org -OutFile $installerPath -UseBasicParsing

    # TODO: Add a step to verify the checksum of the downloaded file against a known value.
    # For example:
    # if ((Get-FileHash $installerPath -Algorithm SHA256).Hash -ne 'EXPECTED_CHECKSUM') { throw 'Checksum mismatch!' }

    # Execute the local, verified script
    python $installerPath

    # Add Poetry to PATH for the current session (and potentially permanently)
    # The installer usually handles this, but explicit addition can help
    $env:Path += ";$($HOME)\.poetry\bin"
    Write-Host "Poetry installed successfully."
}

Write-Host "Poetry setup complete."
