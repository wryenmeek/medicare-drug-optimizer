# Medicare Drug Optimizer

This project aims to help users find and optimize their Medicare Part D drug costs.

## Project Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management and virtual environment isolation.

### Prerequisites

*   Python 3.10 or 3.11 installed.
*   Poetry installed globally on your system. If not, you can install it using:
    ```bash
    curl -sSL https://install.python-poetry.org | python -
    ```
    (or refer to the [official Poetry documentation](https://python-poetry.org/docs/#installation) for your operating system).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/medicare-drug-optimizer.git
    cd medicare-drug-optimizer
    ```

2.  **Install project dependencies:**
    ```bash
    poetry install
    ```
    This will create a virtual environment (if one doesn't exist) and install all project dependencies.

3.  **Activate the virtual environment:**
    ```bash
    poetry shell
    ```

### Running the Application

#### Backend
1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Activate the Poetry shell:
    ```bash
    poetry shell
    ```
3.  Run the FastAPI application:
    ```bash
    uvicorn app.main:app --reload
    ```

#### Frontend
1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install Node.js dependencies:
    ```bash
    npm install
    ```
3.  Start the Vite development server:
    ```bash
    npm run dev
    ```

### Running Tests

#### Backend
1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Activate the Poetry shell:
    ```bash
    poetry shell
    ```
3.  Run pytest:
    ```bash
    pytest
    ```

#### Frontend
1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Run Vitest:
    ```bash
    npm run test
    ```