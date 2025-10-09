# Data Model

This feature primarily defines the deployment configuration and does not introduce new backend data models. It focuses on the frontend application's build and deployment artifacts.

## Entities

### FrontendBuildArtifact
Represents the compiled and optimized assets of the Single Page Application ready for deployment.

- **build_id**: Unique identifier for a specific build.
- **version**: Version of the frontend application.
- **build_date**: Timestamp of the build.
- **asset_list**: List of generated files (HTML, CSS, JS, etc.).

### GitHubActionsWorkflow
Represents the configuration for the automated deployment process.

- **workflow_name**: Name of the GitHub Actions workflow (e.g., "Deploy Frontend to GitHub Pages").
- **trigger_events**: Git events that trigger the workflow (e.g., `push` to `main` branch).
- **steps**: Sequence of actions performed (e.g., checkout code, install dependencies, build frontend, deploy to GitHub Pages).
