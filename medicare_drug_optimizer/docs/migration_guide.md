# Migration Guide: From requirements.txt to Poetry

This guide outlines the steps to migrate a Python project from using `requirements.txt` for dependency management to Poetry.

## Prerequisites
- Poetry installed on your system.

## Steps

1.  **Initialize Poetry in your project**
    Navigate to your project's root directory and run:
    ```bash
    poetry init
    ```
    Follow the prompts to set up your `pyproject.toml` file. You can accept most defaults for now.

2.  **Add existing dependencies from `requirements.txt`**
    Poetry can read your `requirements.txt` file and add the dependencies to your `pyproject.toml`.
    ```bash
    poetry add $(cat requirements.txt | xargs)
    ```
    *Note: This command assumes a simple `requirements.txt` with one package per line. For more complex files (e.g., with `--find-links` or `--extra-index-url`), manual adjustment might be needed.*

3.  **Install dependencies**
    Once dependencies are added to `pyproject.toml`, install them:
    ```bash
    poetry install
    ```
    This will create a virtual environment (if one doesn't exist) and install all dependencies, generating a `poetry.lock` file.

4.  **Remove `requirements.txt`**
    Once you've successfully migrated, you can remove the old `requirements.txt` file:
    ```bash
    rm requirements.txt
    ```

5.  **Update your workflow**
    - Instead of `pip install -r requirements.txt`, use `poetry install`.
    - Instead of `pip install <package>`, use `poetry add <package>`.
    - Instead of `pip uninstall <package>`, use `poetry remove <package>`.
    - To run commands within the Poetry environment, use `poetry run <command>` (e.g., `poetry run pytest`).
