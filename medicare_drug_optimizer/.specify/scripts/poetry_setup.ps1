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
    
    # Install Poetry using the official installer script
    # This is the recommended way to install Poetry
    Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing | Invoke-Expression

    # Add Poetry to PATH for the current session (and potentially permanently)
    # The installer usually handles this, but explicit addition can help
    $env:Path += ";$($HOME)\.poetry\bin"
    Write-Host "Poetry installed successfully."
}

Write-Host "Poetry setup complete."
