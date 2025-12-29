# Gemini Context File

This file provides context for Gemini when working with this repository.

## Project Overview

**Name:** python-playground
**Purpose:** A structured Python learning repository covering core Python concepts and data analytics.
**Management:** Managed using `uv` for dependency resolution and environment management.
**Structure:** The project is organized into learning domains (top-level directories) with numbered sub-modules for structured learning.

## Key Technologies

- **Language:** Python 3.12+
- **Package Manager:** `uv`
- **Core Libraries:**
    - **Data Analytics:** `numpy`, `pandas`, `matplotlib`, `seaborn`
    - **Utilities:** `requests`
- **Development Tools:**
    - **Linting:** `ruff`
    - **Testing:** `pytest`, `pytest-cov`
    - **Interactive:** `jupyter`, `ipython`

## Building and Running

### Dependency Management
- **Install all dependencies:**
  ```bash
  uv sync
  ```
- **Install with dev dependencies (testing tools):**
  ```bash
  uv sync --extra dev
  ```

### Running Code
- **Run a specific Python script:**
  ```bash
  uv run python <script_path>
  # Example:
  uv run python 01_python_core/01_basics/01_variables/01_basic_types.py
  ```

### Interactive Development
- **Start Jupyter Notebook:**
  ```bash
  uv run jupyter notebook
  ```
- **Start JupyterLab:**
  ```bash
  uv run jupyter lab
  ```

### Testing
- **Run all tests:**
  ```bash
  uv run pytest
  ```
- **Run tests with coverage:**
  ```bash
  uv run pytest --cov
  ```

### Code Quality
- **Lint code:**
  ```bash
  uv run ruff check .
  ```
- **Lint and fix:**
  ```bash
  uv run ruff check --fix .
  ```

## Project Architecture

### Directory Structure
The project follows a specific convention: **numbered top-level domains -> numbered sub-topics**.

```text
python-playground/
├── 01_python_core/           # Domain: Python Language Fundamentals
│   ├── 01_basics/            # Topic: Syntax, Variables, Control Flow
│   ├── 02_advanced/          # Topic: Decorators, Generators, AsyncIO
│   ├── tests/                # Domain-specific tests
│   ├── docs/                 # Domain-specific documentation
│   └── notebooks/            # Domain-specific notebooks
├── 02_data_analytics/        # Domain: Data Analysis
│   ├── 01_numpy/             # Topic: NumPy
│   ├── 02_pandas/            # Topic: Pandas
│   ├── 03_visualization/     # Topic: Matplotlib/Seaborn
│   └── ...
├── utils/                    # Shared utility functions
├── docs/                     # Global project documentation
└── discuss/                  # Discussion and planning
```

### Development Conventions

1.  **Naming:**
    - Use two-digit prefixes (e.g., `01_`, `02_`) for directories to maintain learning order.
    - Python modules must be valid packages (include `__init__.py`).
2.  **Style:**
    - Follows `ruff` configuration (line length 88).
    - Docstrings and comments should be in **Chinese**.
3.  **Expansion:**
    - New domains should follow the numbered pattern (e.g., `03_web_development`).
    - Register new packages in `pyproject.toml` under `[tool.hatch.build.targets.wheel]`.
