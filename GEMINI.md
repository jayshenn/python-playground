# Gemini Context File

This file provides context for Gemini when working with this repository.

## Project Overview

**Name:** python-playground
**Purpose:** A structured Python learning repository covering core Python concepts, data analytics, and LangChain foundation.
**Approach:**
- **01_python_core:** Converts 17 comprehensive Markdown documents into ~450 structured, executable Python examples following a strict hierarchical naming convention.
- **03_langchain_foundation:** Focuses on modern LLM orchestration (LangChain, LangGraph, LangSmith) based on official documentation.
**Management:** Managed using `uv` for dependency resolution and environment management.

## Key Technologies

- **Language:** Python 3.12+
- **Package Manager:** `uv`
- **Core Libraries:**
    - **Data Analytics:** `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`
    - **LLM & LangChain:** `langchain`, `langgraph`, `langsmith`, `langchain-openai`, `langchain-anthropic`, `langchain-google-genai`, `langchain-google-vertexai`
    - **Tools & MCP:** `tavily`, `mcp`, `langchain-mcp-adapters`
    - **Data Validation:** `pydantic`
    - **Utilities:** `requests`, `python-dotenv`, `sounddevice`, `pypdf`
- **Development Tools:**
    - **Linting:** `ruff`
    - **Testing:** `pytest`, `pytest-cov`
    - **Interactive:** `jupyter`, `jupyterlab`, `ipython`

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
The project follows a specific convention: **numbered top-level domains -> numbered sub-topics -> numbered scripts**.

```text
python-playground/
├── 01_python_core/           # Domain: Python Language Fundamentals
│   ├── 01_basics/            # Topic: Syntax, Variables, Control Flow
│   ├── 02_data_structures/   # Topic: List, String, Tuple, Set, Dict
│   ├── 03_functions/         # Topic: Functions, Scope, Lambda
│   ├── 04_file_operations/   # Topic: File I/O, Encoding, Pathlib
│   ├── 05_oop/               # Topic: Object-Oriented Programming
│   ├── 08_advanced/          # Topic: Decorators, Generators, Iterators
│   ├── 12_type_system/       # Topic: Pydantic, Mypy, Type Annotations
│   ├── 规划说明.md           # Detailed plan for Python Core
│   └── ... (up to 12 domains)
├── 02_data_analytics/        # Domain: Data Analysis
│   ├── 01_numpy/             # Topic: NumPy
│   └── ...
├── 03_langchain_foundation/  # Domain: LangChain & LLM Application
│   ├── 01_module1/           # Topic: LangChain (Python) - Agents
│   ├── 02_module2/           # Topic: LangGraph - Orchestration
│   ├── 03_module3/           # Topic: Deep Agents - Complex Tasks
│   ├── 04_langsmith/         # Topic: LangSmith - Observability
│   └── docs/学习计划.md       # Detailed learning plan for LangChain
├── utils/                    # Shared utility functions
├── docs/                     # Global project documentation
├── pyproject.toml            # Project configuration and dependencies
└── uv.lock                   # Dependency lock file
```

### Development Conventions

1.  **Naming (01_python_core):**
    - **One-level:** `序号_主题英文名/` (e.g., `01_basics/`)
    - **Two-level:** `序号_章节英文名/` (e.g., `01_comments/`)
    - **Scripts:** `序号_小节英文名.py` (e.g., `01_what_is_comment.py`)
    - Python modules must include `__init__.py`.
2.  **Style:**
    - Follows `ruff` configuration (line length 88).
    - Docstrings and comments should be in **Chinese**.
3.  **Expansion:**
    - New domains should follow the numbered pattern (e.g., `04_web_development`).
    - Register new packages in `pyproject.toml` under `[tool.hatch.build.targets.wheel]`.
