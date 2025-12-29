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

- **数据分析**: numpy, pandas, matplotlib, seaborn
- **交互式开发**: jupyter, ipython
- **代码质量**: ruff
- **实用工具**: requests

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

### 未来扩展方向
   - `03_web_development/` - Web 开发（Flask/Django/FastAPI）
   - `04_machine_learning/` - 机器学习（scikit-learn/TensorFlow）
   - `05_big_data/` - 大数据处理（PySpark）
   - `06_automation/` - 自动化脚本

## 项目版本

- Python: 3.14.2
- uv: 0.9.18

## 许可证

本项目仅用于个人学习目的。
