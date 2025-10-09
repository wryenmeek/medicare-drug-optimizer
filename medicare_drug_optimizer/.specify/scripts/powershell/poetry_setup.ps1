# .specify/scripts/powershell/poetry_setup.ps1
# This script installs Poetry on Windows.

Write-Host "Checking for Poetry installation..."

# Check if Poetry is already installed
try {
    poetry --version | Out-Null
    Write-Host "Poetry is already installed."
} catch {
    Write-Host "Poetry not found. Installing Poetry..."

    # Download and install Poetry
    try {
        Invoke-WebRequest -Uri https://install.python-poetry.org -OutFile install-poetry.py
        python install-poetry.py --version 1.8.2 # Specify a version for consistency
        Remove-Item install-poetry.py
        Write-Host "Poetry installed successfully."
    } catch {
        Write-Error "Failed to install Poetry: $_"
        exit 1
    }
}

# Ensure Poetry's bin directory is in the PATH
$env:PATH += ";$($HOME)\.poetry\bin"
Write-Host "Poetry bin directory added to PATH."

# Configure Poetry to create virtual environments in the project directory
poetry config virtualenvs.in-project true --local
Write-Host "Poetry configured to create virtual environments in-project."

Write-Host "Poetry setup complete."
