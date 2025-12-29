# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个个人 Python 学习项目，使用 uv 进行包管理，采用模块化设计，按学习领域组织代码。

## 开发环境

- Python 版本：3.14.2
- 包管理器：uv 0.9.18
- 依赖管理：pyproject.toml

## 常用命令

### 依赖管理
```bash
# 安装所有依赖
uv sync

# 安装包括开发依赖
uv sync --extra dev
```

### 运行代码
```bash
# 运行 Python 脚本
uv run python <script_path>

# 示例：
uv run python 02_data_analytics/01_numpy/01_intro.py
```

### Jupyter Notebook
```bash
# 启动 Jupyter Notebook
uv run jupyter notebook

# 启动 JupyterLab
uv run jupyter lab
```

### 代码质量
```bash
# 使用 ruff 检查代码
uv run ruff check .

# 自动修复问题
uv run ruff check --fix .
```

### 测试
```bash
# 运行所有测试
uv run pytest

# 运行测试并查看覆盖率
uv run pytest --cov
```

## 项目架构

### 目录结构原则

项目采用**按学习领域分类 + 每个领域自包含 + 统一使用数字序号**的组织方式：

1. **顶层目录 = 学习领域**：每个顶层目录（如 `01_python_core/`、`02_data_analytics/`）代表一个独立的学习领域
2. **统一数字序号**：所有有学习顺序的目录都使用两位数字前缀（01、02、03...）
3. **自包含设计**：每个学习领域包含自己的 tests/、docs/、notebooks/ 目录
4. **模块化设计**：每个主题都是独立的 Python 包，包含 `__init__.py`
5. **易于扩展**：未来可以添加新的学习领域（如 `03_web_development/`、`04_machine_learning/` 等）

### 关键目录

- **`01_python_core/`**: Python 语言基础
  - `01_basics/`: 基础语法（变量、流程控制、函数、面向对象、模块）
  - `02_advanced/`: 高级特性（装饰器、生成器、异步编程）
  - `tests/`: 该领域的测试代码
  - `docs/`: 该领域的文档
  - `notebooks/`: 该领域的 Jupyter notebooks

- **`02_data_analytics/`**: 数据分析
  - `01_numpy/`: NumPy 数组操作
  - `02_pandas/`: Pandas 数据处理
  - `03_visualization/`: Matplotlib/Seaborn 可视化
  - `04_projects/`: 综合项目实践
  - `tests/`: 该领域的测试代码
  - `docs/`: 该领域的文档
  - `notebooks/`: 该领域的 Jupyter notebooks

- **`03_langchain_foundation/`**: LangChain 基础学习（整合自 langchain-ai/lca-lc-foundations）
  - `01_module1/`: 模块 1 - 创建代理（基础模型、工具、记忆、多模态）
  - `02_module2/`: 模块 2 - 高级代理（MCP、状态管理、多代理系统）
  - `03_module3/`: 模块 3 - 生产就绪代理（中间件、HITL、动态代理）
  - `utils/`: LangChain 相关工具（环境配置等）
  - `tests/`: 该领域的测试代码
  - `docs/`: 完整的中文学习文档（13 个文件，10 万+ 字）
    - `README.md`: 总索引，包含学习路径、环境配置、技术栈对比
    - `01_langchain/`: LangChain (Python) 模块文档（高级框架）
      - `01_核心组件.md`: Agents、Models、Tools、Messages、Memory、Streaming
      - `02_高级特性.md`: Middleware、Multi-agent、Context Engineering、HITL、Guardrails
    - `02_langgraph/`: LangGraph (Python) 模块文档（低级编排框架）
      - `01_基础.md`: Graph API、Functional API、State Management
      - `02_高级特性.md`: Persistence、Interrupts、Memory、Durable Execution、Streaming
    - `03_deepagents/`: Deep Agents (Python) 模块文档（复杂任务处理）
      - `01_基础.md`: 四大核心能力、快速开始、自定义配置
      - `02_高级特性.md`: Backends、Subagents、Long-term Memory、HITL
    - `04_langsmith/`: LangSmith 模块文档（可观测性和部署）
      - `01_可观测性与评估.md`: Observability、Tracing、Evaluation
      - `02_部署.md`: Cloud Deployment、配置管理、生产环境最佳实践

- **`utils/`**: 项目共享工具函数

- **`docs/`**: 项目级文档（如项目说明、架构文档）

- **`discuss/`**: 讨论和计划文档

### 代码组织模式

每个学习领域下的子主题都是一个 Python 包：
- 必须包含 `__init__.py` 文件
- 可以被其他模块导入
- 示例代码通常包含 `if __name__ == "__main__":` 块用于直接运行

## 代码规范

### Ruff 配置

- 行长度限制：88 字符
- 目标 Python 版本：3.12+
- 启用的检查规则：E (错误), F (pyflakes), I (import 排序), N (命名), W (警告)

### 文档语言

- 代码注释和文档字符串：使用中文
- Markdown 文档：使用中文
- 正式文档：写到 `docs/` 目录
- 讨论文档：写到 `discuss/` 目录

## 开发注意事项

### 添加新学习模块

创建新的学习主题时：
1. 使用两位数字前缀（如 `03_new_topic/`）创建顶层学习领域目录
2. 在领域内的子模块也使用两位数字前缀（如 `01_module1/`、`02_module2/`）
3. 在领域目录下创建 `tests/`、`docs/`、`notebooks/` 子目录
4. 在子主题目录下创建 `__init__.py`
5. 在 `pyproject.toml` 的 `tool.hatch.build.targets.wheel.packages` 中添加新包

### 依赖项

核心依赖：
- 数据分析：numpy, pandas, matplotlib, seaborn, scipy
- 交互式开发：jupyter, jupyterlab, ipython, ipykernel, ipywidgets
- 代码质量：ruff
- 实用工具：requests, python-dotenv, pydantic
- LangChain 生态：
  - 核心：langchain, langchain-core, langchain-community, langgraph
  - 集成：langchain-openai, langchain-anthropic, langchain-google-vertexai
  - 工具：tavily, mcp, langsmith
  - 文档处理：pypdf, langchain-text-splitters

开发依赖：
- 测试：pytest, pytest-cov

### LangChain Foundation 环境配置

使用 LangChain Foundation 模块时需要配置 API 密钥：

```bash
# 进入 langchain foundation 目录
cd 03_langchain_foundation

# 复制环境变量示例文件
cp example.env .env

# 编辑 .env 文件，添加你的 API 密钥
# 必需：OPENAI_API_KEY, TAVILY_API_KEY
# 可选：ANTHROPIC_API_KEY, GOOGLE_API_KEY, LANGSMITH_API_KEY

# 验证环境配置
uv run python utils/env_utils.py
```

详细使用说明请参阅 `03_langchain_foundation/docs/README.md`

### Git 工作流

- 数据文件（.csv, .xlsx, .db）已在 .gitignore 中排除
- 虚拟环境目录 .venv/ 已忽略
- IDE 配置文件（.idea/, .vscode/）已忽略
