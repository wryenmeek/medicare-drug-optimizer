# Poetry Best Practices and Troubleshooting

## Best Practices

*   **Always use `poetry add` and `poetry remove`**: Avoid manually editing `pyproject.toml` and `poetry.lock`.
*   **Commit `poetry.lock`**: This ensures reproducible builds across different environments.
*   **Use `poetry run`**: Execute scripts and commands within the Poetry-managed virtual environment.
*   **Specify Python versions**: Clearly define the supported Python versions in `pyproject.toml`.

## Troubleshooting

### Dependency Resolution Issues

*   **`poetry update`**: Try updating all dependencies to their latest compatible versions.
*   **`poetry lock --no-update`**: Re-generate the `poetry.lock` file without updating dependencies.
*   **`poetry install --sync`**: Reinstall dependencies from `poetry.lock`, removing any unlisted packages.

### Virtual Environment Issues

*   **`poetry env remove <env_name>`**: Remove a corrupted virtual environment.
*   **`poetry install`**: Recreate the virtual environment and install dependencies.
