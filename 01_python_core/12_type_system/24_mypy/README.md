# mypy 使用指南

`mypy` 是 Python 静态类型检查的先行者和官方推荐工具。它能够帮助你捕获代码中细微的类型错误，并确保大型项目中的接口一致性。

## 目录

- [01_installation.py - 安装说明](01_installation.py)：介绍如何安装 mypy。
- [02_basic_usage.py - 基本使用](02_basic_usage.py)：介绍常用的命令行指令，如检查文件、目录和显示错误代码。
- [03_config_file.py - 配置文件](03_config_file.py)：展示如何通过 `mypy.ini` 或 `pyproject.toml` 持久化配置。
- [04_strict_mode.py - 严格模式](04_strict_mode.py)：介绍如何启用更严苛的检查选项（如禁止 Any）。
- [05_common_errors.py - 常见错误](05_common_errors.py)：分析并提供解决典型 mypy 报错的方案。
- [06_ignore_checks.py - 忽略检查](06_ignore_checks.py)：展示如何使用 `# type: ignore` 处理无法自动通过的特定代码行。
- [07_stub_files.py - Stub 文件](07_stub_files.py)：介绍如何使用 `.pyi` 文件为没有类型提示的第三方库提供定义。

## 核心特性

1. **增量检查**：只检查修改过的文件，提升二次运行速度。
2. **丰富的插件**：支持 Pydantic、SQLAlchemy、Django、Pytest 等主流框架。
3. **错误代码**：每个错误都有唯一的代码（如 `[assignment]`, `[arg-type]`），方便精准忽略。

## 学习建议

- 始终启用 `show_error_codes = True`，这能让你更清楚为什么代码没通过检查。
- 对于新项目，建议开启较严格的配置；对于老项目，可以先关闭严格检查，然后逐步修复。
