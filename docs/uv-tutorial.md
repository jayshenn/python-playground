# uv 完整使用教程

## 目录

1. [什么是 uv](#什么是-uv)
2. [安装和更新](#安装和更新)
3. [项目管理](#项目管理)
4. [依赖管理](#依赖管理)
5. [Python 版本管理](#python-版本管理)
6. [虚拟环境管理](#虚拟环境管理)
7. [运行代码](#运行代码)
8. [常用命令速查](#常用命令速查)
9. [最佳实践](#最佳实践)
10. [常见问题](#常见问题)

---

## 什么是 uv

**uv** 是由 Astral 开发的**极速 Python 包管理器**，用 Rust 编写。

### 核心特点

- ⚡ **极快**：比 pip 快 10-100 倍
- 🔧 **统一工具**：替代 pip、pip-tools、pipenv、poetry、pyenv 等
- 📦 **完整功能**：项目管理、依赖解析、虚拟环境、Python 版本管理
- 🎯 **简单易用**：单一命令行工具，学习成本低
- 🔒 **可靠**：锁定依赖版本，确保可重现构建

### 对比传统工具

| 功能 | pip | poetry | uv |
|------|-----|--------|-----|
| 安装速度 | 慢 | 中 | ⚡ 极快 |
| 依赖解析 | 基础 | 好 | ✅ 优秀 |
| 锁文件 | ❌ | ✅ | ✅ |
| Python 版本管理 | ❌ | ❌ | ✅ |
| 虚拟环境 | 需配合 venv | ✅ | ✅ |
| 项目初始化 | ❌ | ✅ | ✅ |

---

## 安装和更新

### 安装 uv

**macOS/Linux（推荐）：**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Homebrew：**
```bash
brew install uv
```

**pip：**
```bash
pip install uv
```

**Windows（PowerShell）：**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 验证安装

```bash
uv --version
```

### 更新 uv

**官方安装方式：**
```bash
uv self update
```

**Homebrew：**
```bash
brew upgrade uv
```

**pip：**
```bash
pip install --upgrade uv
```

---

## 项目管理

### 1. 初始化新项目

```bash
# 在当前目录初始化
uv init

# 创建新项目目录并初始化
uv init my-project
cd my-project
```

生成的文件：
- `pyproject.toml` - 项目配置文件
- `.python-version` - Python 版本固定文件（可选）
- `README.md` - 项目说明
- `src/` - 源代码目录（可选）

### 2. 查看项目信息

```bash
# 查看项目配置
cat pyproject.toml

# 查看已安装的包
uv pip list
```

### 3. pyproject.toml 文件结构

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "项目描述"
requires-python = ">=3.12"
dependencies = [
    "numpy>=2.0.0",
    "pandas>=2.2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.4.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

---

## 依赖管理

### 1. 添加依赖

```bash
# 添加单个包
uv add numpy

# 添加多个包
uv add pandas matplotlib seaborn

# 添加指定版本
uv add "numpy>=2.0.0,<3.0.0"
uv add "pandas==2.2.0"

# 添加开发依赖
uv add --dev pytest ruff

# 添加可选依赖组
uv add --optional ml scikit-learn tensorflow
```

### 2. 移除依赖

```bash
# 移除包
uv remove numpy

# 移除开发依赖
uv remove --dev pytest
```

### 3. 安装依赖

```bash
# 安装所有依赖（根据 pyproject.toml）
uv sync

# 只安装生产依赖（不包括 dev）
uv sync --no-dev

# 安装包括可选依赖
uv sync --extra dev
uv sync --all-extras
```

### 4. 更新依赖

```bash
# 更新所有依赖到最新兼容版本
uv sync --upgrade

# 更新特定包
uv sync --upgrade-package numpy

# 更新并重新解析依赖
uv lock --upgrade
```

### 5. 锁定文件

uv 会自动生成 `uv.lock` 文件，记录所有依赖的确切版本。

```bash
# 生成/更新锁文件
uv lock

# 根据锁文件安装（确保一致性）
uv sync
```

**重要**：将 `uv.lock` 提交到 Git，确保团队成员使用相同版本的依赖。

---

## Python 版本管理

### 1. 查看可用 Python 版本

```bash
# 列出所有可用版本
uv python list

# 列出已安装版本
uv python list --only-installed
```

### 2. 安装 Python 版本

```bash
# 安装特定版本
uv python install 3.12
uv python install 3.13
uv python install 3.14

# 安装多个版本
uv python install 3.12 3.13
```

### 3. 固定项目 Python 版本

```bash
# 为当前项目固定版本
uv python pin 3.12

# 固定到具体版本
uv python pin 3.12.10
```

这会创建/更新 `.python-version` 文件。

### 4. 查找 Python 可执行文件

```bash
# 查找当前项目使用的 Python
uv python find

# 查找特定版本
uv python find 3.12
```

### 5. 卸载 Python 版本

```bash
# 卸载指定版本
uv python uninstall 3.11
```

---

## 虚拟环境管理

### 1. 创建虚拟环境

```bash
# uv sync 会自动创建 .venv/
uv sync

# 手动创建虚拟环境
uv venv

# 指定 Python 版本创建
uv venv --python 3.12

# 指定虚拟环境位置
uv venv /path/to/venv
```

### 2. 激活虚拟环境

**macOS/Linux：**
```bash
source .venv/bin/activate
```

**Windows：**
```bash
.venv\Scripts\activate
```

### 3. 退出虚拟环境

```bash
deactivate
```

### 4. 直接使用虚拟环境（无需激活）

```bash
# uv run 会自动使用项目虚拟环境
uv run python script.py
uv run pytest
```

---

## 运行代码

### 1. 运行 Python 脚本

```bash
# 使用项目虚拟环境运行
uv run python script.py
uv run python -m module_name

# 传递参数
uv run python script.py --arg1 value1
```

### 2. 运行安装的命令行工具

```bash
# 运行项目依赖中的工具
uv run pytest
uv run ruff check .
uv run jupyter notebook

# 运行带参数的命令
uv run pytest tests/ -v
```

### 3. 临时运行包（不安装）

```bash
# 快速运行工具，不添加到项目依赖
uvx ruff check .
uvx black .
uvx httpie https://api.github.com

# 指定版本
uvx ruff@0.4.0 check .
```

`uvx` = uv + execute，类似 `npx`。

### 4. 启动 Python REPL

```bash
# 在项目环境中启动 Python
uv run python

# 启动 IPython
uv run ipython
```

---

## 常用命令速查

### 项目初始化

```bash
uv init                  # 初始化项目
uv init my-project      # 创建新项目
```

### 依赖管理

```bash
uv add package          # 添加依赖
uv add --dev package    # 添加开发依赖
uv remove package       # 移除依赖
uv sync                 # 同步依赖（安装）
uv sync --upgrade       # 更新依赖
uv lock                 # 更新锁文件
```

### Python 版本

```bash
uv python list          # 列出可用版本
uv python install 3.12  # 安装 Python
uv python pin 3.12      # 固定项目版本
uv python find          # 查找 Python 路径
```

### 虚拟环境

```bash
uv venv                 # 创建虚拟环境
uv venv --python 3.12   # 指定版本创建
```

### 运行代码

```bash
uv run python script.py  # 运行脚本
uv run pytest            # 运行工具
uvx tool                 # 临时运行工具
```

### 其他

```bash
uv self update          # 更新 uv 本身
uv --version            # 查看版本
uv --help               # 查看帮助
```

---

## 最佳实践

### 1. 项目结构

```
my-project/
├── .venv/              # 虚拟环境（不提交到 Git）
├── .python-version     # Python 版本固定
├── pyproject.toml      # 项目配置
├── uv.lock            # 依赖锁定（提交到 Git）
├── README.md          # 项目说明
├── src/               # 源代码
│   └── my_project/
├── tests/             # 测试代码
└── .gitignore         # Git 忽略文件
```

### 2. .gitignore 配置

```gitignore
# 虚拟环境
.venv/
venv/
ENV/

# Python
__pycache__/
*.py[cod]
*.so

# uv
.uv/
```

**重要**：
- ✅ 提交：`pyproject.toml`、`uv.lock`、`.python-version`
- ❌ 不提交：`.venv/`、`__pycache__/`

### 3. 团队协作

**新成员加入项目：**

```bash
# 1. 克隆项目
git clone repo-url
cd project

# 2. 安装 uv（如果没有）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. 同步依赖（会自动创建虚拟环境）
uv sync

# 4. 开始开发
uv run python script.py
```

### 4. 持续集成（CI）

**GitHub Actions 示例：**

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Set up Python
        run: uv python install

      - name: Install dependencies
        run: uv sync

      - name: Run tests
        run: uv run pytest
```

### 5. 依赖版本策略

```toml
[project]
dependencies = [
    # 推荐：使用兼容版本范围
    "numpy>=2.0.0,<3.0.0",    # 允许 2.x 的任何版本
    "pandas>=2.2.0",           # 2.2.0 及以上

    # 谨慎使用：固定确切版本
    "requests==2.32.0",        # 只在有特殊原因时使用

    # 避免：过于宽松的版本
    "matplotlib",              # 不推荐，没有版本限制
]
```

### 6. 开发工作流

```bash
# 1. 创建功能分支
git checkout -b feature/new-feature

# 2. 添加新依赖
uv add new-package

# 3. 开发和测试
uv run python script.py
uv run pytest

# 4. 提交更改（包括 uv.lock）
git add pyproject.toml uv.lock
git commit -m "Add new feature"

# 5. 推送并创建 PR
git push origin feature/new-feature
```

---

## 常见问题

### Q1: uv 和 pip 有什么区别？

**uv** 是 pip 的现代替代品：
- 更快（10-100倍）
- 更可靠（依赖解析更好）
- 更全面（包含虚拟环境、Python 版本管理）
- 可以完全替代 pip

### Q2: 是否可以在 uv 项目中使用 pip？

可以，但不推荐混用：

```bash
# 不推荐
uv run pip install package

# 推荐
uv add package
```

### Q3: uv.lock 文件有什么用？

`uv.lock` 确保：
- 所有团队成员使用相同的依赖版本
- CI/CD 环境可重现
- 避免"在我机器上能运行"的问题

**一定要提交到 Git！**

### Q4: 如何迁移现有项目到 uv？

```bash
# 1. 如果有 requirements.txt
uv add -r requirements.txt

# 2. 如果有 poetry
uv sync  # uv 可以读取 poetry 的 pyproject.toml

# 3. 如果有 setup.py
uv pip install -e .
```

### Q5: .venv 目录很大，是否要提交到 Git？

**不要！** 虚拟环境永远不应该提交到版本控制。

在 `.gitignore` 中添加：
```gitignore
.venv/
```

团队成员通过 `uv sync` 重建虚拟环境。

### Q6: 如何在 PyCharm 中使用 uv 虚拟环境？

1. 运行 `uv sync` 创建虚拟环境
2. 在 PyCharm 中：
   - Settings → Project → Python Interpreter
   - Add Interpreter → Existing
   - 选择 `.venv/bin/python`

### Q7: uv 支持哪些 Python 版本？

uv 支持 Python 3.8 到 3.14（包括最新版本）。

### Q8: 如何查看依赖树？

```bash
# 使用 pip tree（在 uv 环境中）
uv run pip install pipdeptree
uv run pipdeptree
```

### Q9: 如何清理缓存？

```bash
# 清理 uv 缓存
uv cache clean

# 查看缓存大小
uv cache dir
```

### Q10: uv 能否替代 conda？

部分功能可以：
- ✅ Python 版本管理
- ✅ 虚拟环境
- ✅ 包管理
- ❌ 非 Python 包（如 C 库、系统工具）

如果只做 Python 开发，uv 完全够用。需要管理系统级依赖时，conda 更适合。

---

## 更多资源

- **官方文档**: https://docs.astral.sh/uv/
- **GitHub**: https://github.com/astral-sh/uv
- **更新日志**: https://github.com/astral-sh/uv/releases

---

## 总结

uv 是现代 Python 开发的强大工具：

✅ **快速开始**：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv init my-project
cd my-project
uv add numpy pandas
uv run python script.py
```

✅ **核心命令**：
- `uv init` - 初始化项目
- `uv add` - 添加依赖
- `uv sync` - 安装依赖
- `uv run` - 运行代码
- `uvx` - 临时运行工具

✅ **最佳实践**：
- 提交 `pyproject.toml` 和 `uv.lock`
- 不提交 `.venv/`
- 使用 `uv run` 而不是激活虚拟环境
- 定期更新：`uv sync --upgrade`

掌握这些，你就能高效使用 uv 进行 Python 开发了！🚀
