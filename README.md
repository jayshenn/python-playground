# Python 学习项目

这是一个使用 uv 管理的 Python 学习项目，涵盖 Python 基础、数据分析等多个主题。

## 项目结构

```
python-playground/
├── 01_python_fundamentals/    # Python 语言基础
│   ├── 01_basics/            # 基础语法
│   │   ├── 01_variables/     # 变量和数据类型
│   │   ├── 02_control_flow/  # 流程控制
│   │   ├── 03_functions/     # 函数
│   │   ├── 04_oop/          # 面向对象编程
│   │   └── 05_modules/      # 模块和包
│   └── 02_advanced/          # 高级特性
│       ├── 01_decorators/   # 装饰器
│       ├── 02_generators/   # 生成器
│       └── 03_async_io/     # 异步编程
├── 02_data_analytics/        # 数据分析
│   ├── 01_numpy/            # NumPy 基础
│   ├── 02_pandas/           # Pandas 基础
│   ├── 03_visualization/    # 数据可视化
│   └── 04_projects/         # 小项目实践
├── notebooks/                # Jupyter notebooks
│   ├── 01_python_fundamentals/
│   └── 02_data_analytics/
├── tests/                    # 测试代码
├── utils/                    # 通用工具函数
├── docs/                     # 正式文档
└── discuss/                  # 讨论和计划文档
```

## 设计**理念**

- **按学习领域分类**：每个顶层目录代表一个学习领域（如 Python 语言、数据分析、大数据等）
- **数字序号排序**：使用两位数字前缀确保学习顺序清晰
- **易于扩展**：未来可以添加 `big_data/`、`web_development/`、`machine_learning/` 等领域
- **模块化设计**：每个主题都是独立的 Python 包，便于导入和测试
```

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
# 运行 Python 基础示例
uv run python 01_python_fundamentals/01_basics/01_variables/01_basic_types.py

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

### 01. Python 语言基础 (`01_python_fundamentals/`)

#### 01_basics - 基础语法
   - 01_variables - 变量和数据类型
   - 02_control_flow - 流程控制（if/for/while）
   - 03_functions - 函数定义和使用
   - 04_oop - 面向对象编程
   - 05_modules - 模块和包管理

#### 02_advanced - 高级特性
   - 01_decorators - 装饰器和元编程
   - 02_generators - 生成器和迭代器
   - 03_async_io - 异步编程

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
