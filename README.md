# Python 学习项目

这是一个使用 uv 管理的 Python 学习项目，涵盖 Python 基础、数据分析等多个主题。

## 项目结构

```
python-playground/
├── 01_python_core/              # Python 语言基础
│   ├── 01_basics/               # 基础语法（21个细化模块）
│   │   ├── 01_comments.py       # 注释
│   │   ├── 02_variables.py      # 变量
│   │   ├── 03_number_systems.py # 进制系统
│   │   ├── 04_if_statements.py  # if条件语句
│   │   ├── 05_match_case.py     # match-case语句
│   │   ├── 06_while_loops.py    # while循环
│   │   ├── 07_for_loops.py      # for循环
│   │   ├── 08_loop_control.py   # 循环控制(break/continue/pass)
│   │   ├── 09_comprehensions.py # 推导式
│   │   ├── 10_data_types_basic.py    # 基础数据类型
│   │   ├── 11_type_conversion.py     # 类型转换
│   │   ├── 12_string_encoding.py     # 字符串编码
│   │   ├── 13_input_output.py        # 输入输出
│   │   ├── 14_arithmetic_operators.py    # 算术运算符
│   │   ├── 15_comparison_operators.py    # 比较运算符
│   │   ├── 16_logical_operators.py       # 逻辑运算符
│   │   ├── 17_bitwise_operators.py       # 位运算符
│   │   ├── 18_membership_operators.py    # 成员运算符
│   │   ├── 19_assignment_operators.py    # 赋值运算符
│   │   ├── 20_identity_operators.py      # 身份运算符
│   │   └── 21_operator_precedence.py     # 运算符优先级
│   ├── 02_data_structures/      # 数据结构
│   │   ├── 01_lists.py          # 列表
│   │   ├── 02_tuples.py         # 元组
│   │   ├── 03_strings.py        # 字符串
│   │   ├── 04_sets.py           # 集合
│   │   └── 05_dictionaries.py   # 字典
│   ├── 03_functions/            # 函数
│   ├── 04_file_operations/      # 文件操作
│   ├── 05_oop/                  # 面向对象编程
│   ├── 06_exceptions/           # 异常处理
│   ├── 07_modules/              # 模块和包
│   ├── 08_advanced/             # 高级特性
│   ├── 09_regex/                # 正则表达式
│   ├── 10_concurrency/          # 并发编程
│   ├── 11_networking/           # 网络编程
│   ├── docs/                    # 17个Markdown文档
│   ├── tests/                   # 测试
│   └── notebooks/               # Jupyter Notebooks
├── 02_data_analytics/           # 数据分析
│   ├── 01_numpy/                # NumPy 基础
│   ├── 02_pandas/               # Pandas 基础
│   ├── 03_visualization/        # 数据可视化
│   ├── 04_projects/             # 小项目实践
│   ├── docs/                    # 文档
│   ├── tests/                   # 测试
│   └── notebooks/               # Jupyter Notebooks
├── 03_langchain_foundation/     # LangChain 基础学习
│   ├── 01_module1/              # Module 1: 创建代理
│   │   ├── __init__.py
│   │   └── notebooks/           # 基础模型、工具、记忆、多模态
│   ├── 02_module2/              # Module 2: 高级代理
│   │   ├── __init__.py
│   │   └── notebooks/           # MCP、状态管理、多代理系统
│   ├── 03_module3/              # Module 3: 生产就绪代理
│   │   ├── __init__.py
│   │   └── notebooks/           # 中间件、HITL、动态代理
│   ├── utils/                   # LangChain 工具
│   │   ├── __init__.py
│   │   └── env_utils.py         # 环境配置工具
│   ├── tests/                   # 测试
│   ├── docs/                    # 完整中文学习文档（13 个文件，10 万+ 字）
│   │   ├── README.md            # 总索引（学习路径、环境配置、技术栈对比）
│   │   ├── 01_langchain/        # LangChain (Python) 模块
│   │   │   ├── README.md        # 模块索引
│   │   │   ├── 01_核心组件.md    # Agents、Models、Tools、Messages、Memory
│   │   │   └── 02_高级特性.md    # Middleware、Multi-agent、HITL、Guardrails
│   │   ├── 02_langgraph/        # LangGraph (Python) 模块
│   │   │   ├── README.md        # 模块索引
│   │   │   ├── 01_基础.md        # Graph API、Functional API、State
│   │   │   └── 02_高级特性.md    # Persistence、Interrupts、Memory、Streaming
│   │   ├── 03_deepagents/       # Deep Agents (Python) 模块
│   │   │   ├── README.md        # 模块索引
│   │   │   ├── 01_基础.md        # 四大核心能力、快速开始
│   │   │   └── 02_高级特性.md    # Backends、Subagents、Long-term Memory
│   │   └── 04_langsmith/        # LangSmith 模块
│   │       ├── README.md        # 模块索引
│   │       ├── 01_可观测性与评估.md  # Observability、Tracing、Evaluation
│   │       └── 02_部署.md        # Cloud Deployment、生产最佳实践
│   ├── README.md                # 项目说明（中文）
│   ├── .env.example             # 环境变量模板
│   └── example.env              # 环境变量模板（备份）
├── utils/                       # 项目共享工具
├── docs/                        # 项目级文档
│   └── uv-tutorial.md          # uv包管理器教程
└── discuss/                     # 讨论和计划文档
```

## 设计理念

- **按学习领域分类**：每个顶层目录代表一个学习领域（如 Python 语言、数据分析、大数据等）
- **数字序号排序**：使用两位数字前缀确保学习顺序清晰
- **细粒度模块化**：每个概念独立成文件，便于针对性学习和复习
- **文档驱动**：每个代码文件都对应详细的 Markdown 文档
- **易于扩展**：未来可以添加更多学习领域
- **实例丰富**：每个文件包含大量示例和实际应用

## 环境配置

### 前置要求

- Python 3.12+
- uv 包管理器

### 安装依赖

```bash
# 安装所有依赖
uv sync

# 安装开发依赖
uv sync --extra dev
```

### 已安装的主要库

- **数据分析**: numpy, pandas, matplotlib, seaborn, scipy
- **交互式开发**: jupyter, jupyterlab, ipython, ipykernel, ipywidgets
- **代码质量**: ruff
- **实用工具**: requests, python-dotenv, pydantic
- **LangChain 生态**:
  - 核心: langchain, langchain-core, langchain-community, langgraph
  - 集成: langchain-openai, langchain-anthropic, langchain-google-vertexai
  - 工具: tavily, mcp, langsmith
  - 文档处理: pypdf, langchain-text-splitters

## 使用指南

### 运行 Python 脚本

```bash
# 运行 Python 基础示例（按顺序学习）
uv run python 01_python_core/01_basics/01_comments.py
uv run python 01_python_core/01_basics/02_variables.py
uv run python 01_python_core/01_basics/04_if_statements.py

# 运行数据结构示例
uv run python 01_python_core/02_data_structures/01_lists.py

# 运行数据分析示例
uv run python 02_data_analytics/01_numpy/01_intro.py

# 运行 LangChain 示例
uv run python 03_langchain_foundation/01_module1/notebooks/1.5_personal_chef.py
```

### LangChain 环境配置

```bash
# 进入 langchain foundation 目录
cd 03_langchain_foundation

# 复制环境变量模板
cp example.env .env

# 编辑 .env 文件，添加你的 API 密钥
# 必需：OPENAI_API_KEY, TAVILY_API_KEY
# 可选：ANTHROPIC_API_KEY, GOOGLE_API_KEY, LANGSMITH_API_KEY

# 验证环境配置
uv run python utils/env_utils.py
```

### 启动 Jupyter Notebook

```bash
# 启动 Jupyter Notebook
uv run jupyter notebook

# 启动 JupyterLab
uv run jupyter lab
```

### 代码检查

```bash
# 使用 ruff 检查代码
uv run ruff check .

# 自动修复问题
uv run ruff check --fix .
```

### 运行测试

```bash
# 运行所有测试
uv run pytest

# 运行测试并查看覆盖率
uv run pytest --cov
```

## 学习路径

### 01. Python 语言基础 (`01_python_core/`)

#### 01_basics - 基础语法（细化为21个模块）
按学习顺序：
1. **基础概念** (01-03): 注释、变量、进制系统
2. **控制流** (04-09): if语句、match-case、while循环、for循环、循环控制、推导式
3. **数据类型** (10-12): 基础数据类型、类型转换、字符串编码
4. **输入输出** (13): 输入输出操作
5. **运算符** (14-21): 算术、比较、逻辑、位、成员、赋值、身份运算符及优先级

#### 02_data_structures - 数据结构
   - 列表（List）、元组（Tuple）、字符串（String）
   - 集合（Set）、字典（Dictionary）

#### 03-11 - 进阶主题
   - 函数、文件操作、面向对象编程
   - 异常处理、模块和包
   - 高级特性（装饰器、生成器、闭包等）
   - 正则表达式、并发编程、网络编程

#### docs/ - 配套文档
   - 17个Markdown文档，详细讲解每个主题
   - 参考文档: 01-python-basics.md, 02-control-flow.md, 03-data-structures.md 等

### 02. 数据分析 (`02_data_analytics/`)
   - 01_numpy - NumPy 数组操作
   - 02_pandas - Pandas 数据处理
   - 03_visualization - Matplotlib/Seaborn 可视化
   - 04_projects - 综合项目实践

### 03. LangChain 基础 (`03_langchain_foundation/`)

本模块整合自 LangChain Academy 官方课程，包含完整的中文学习文档和三个实战模块。

#### 📚 学习文档（推荐从这里开始！）

**总索引**: [docs/README.md](03_langchain_foundation/docs/README.md) ⭐ 必读
- LangChain Foundation 技术栈完整概览
- 四种学习路径（快速入门、进阶开发、生产专家、场景驱动）
- 环境配置、技术栈对比、常见问题解答

**四大核心模块文档**（13 个文件，10 万+ 字，100+ 代码示例）：

1. **[LangChain (Python)](03_langchain_foundation/docs/01_langchain/)** - 高级框架，快速构建
   - [核心组件](03_langchain_foundation/docs/01_langchain/01_核心组件.md): Agents、Models、Tools、Messages、Memory、Streaming
   - [高级特性](03_langchain_foundation/docs/01_langchain/02_高级特性.md): Middleware、Multi-agent、Context Engineering、HITL、Guardrails

2. **[LangGraph (Python)](03_langchain_foundation/docs/02_langgraph/)** - 低级编排框架，精确控制
   - [基础](03_langchain_foundation/docs/02_langgraph/01_基础.md): Graph API、Functional API、State Management
   - [高级特性](03_langchain_foundation/docs/02_langgraph/02_高级特性.md): Persistence、Interrupts、Memory、Durable Execution、Streaming

3. **[Deep Agents (Python)](03_langchain_foundation/docs/03_deepagents/)** - 处理复杂多步骤任务
   - [基础](03_langchain_foundation/docs/03_deepagents/01_基础.md): 四大核心能力、快速开始、自定义配置
   - [高级特性](03_langchain_foundation/docs/03_deepagents/02_高级特性.md): Backends、Subagents、Long-term Memory、HITL

4. **[LangSmith](03_langchain_foundation/docs/04_langsmith/)** - 可观测性、评估和部署
   - [可观测性与评估](03_langchain_foundation/docs/04_langsmith/01_可观测性与评估.md): Observability、Tracing、Evaluation
   - [部署](03_langchain_foundation/docs/04_langsmith/02_部署.md): Cloud Deployment、配置管理、生产环境最佳实践

#### 💻 实战模块（Jupyter Notebooks）

**Module 1 - 创建代理**（基础，3-5 天）
   - 1.1 基础模型和提示词（Foundational Models & Prompting）
   - 1.2 工具和 Web 搜索（Tools & Web Search）
   - 1.3 记忆系统（Memory）
   - 1.4 多模态消息（Multimodal Messages）
   - 1.5 项目：个人厨师（Personal Chef）

**Module 2 - 高级代理**（进阶，1-2 周）
   - 2.1 Model Context Protocol (MCP)
   - 2.2 状态管理和运行时上下文（State & Runtime Context）
   - 2.3 多代理系统（Multi-Agent Systems）
   - 2.4 项目：婚礼策划师（Wedding Planner）
   - 附加：RAG 系统、SQL 代理

**Module 3 - 生产就绪代理**（高级，2-3 周）
   - 3.1 中间件系统（Middleware）
   - 3.2 消息管理（Managing Long Conversations）
   - 3.3 人机协作（Human-in-the-Loop, HITL）
   - 3.4 动态代理（Dynamic Prompts/Tools/Models）
   - 3.5 项目：邮件助手（Email Assistant）

#### 🎯 推荐学习流程

1. **阅读文档**（2-3 天）：从 [docs/README.md](03_langchain_foundation/docs/README.md) 开始，系统学习四大模块文档
2. **环境配置**（1 小时）：配置 API 密钥，验证环境
3. **实战练习**（2-6 周）：按顺序完成三个模块的 notebooks 和项目
4. **进阶学习**：阅读高级特性文档，构建完整项目

### 未来扩展方向
   - `04_web_development/` - Web 开发（Flask/Django/FastAPI）
   - `05_machine_learning/` - 机器学习（scikit-learn/TensorFlow）
   - `06_big_data/` - 大数据处理（PySpark）
   - `07_automation/` - 自动化脚本

## 项目版本

- Python: 3.14.2
- uv: 0.9.18

## 许可证

本项目仅用于个人学习目的。
