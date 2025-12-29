# pyright 使用指南

`pyright` 是由微软开发的高性能静态类型检查器。它是 VS Code 中 Pylance 语言服务器的基础，以极快的检查速度和深度编辑器集成而闻名。

## 目录

- [01_installation.py - 安装说明](01_installation.py)：介绍如何通过 npm、pip 或 uv 安装 pyright。
- [02_basic_usage.py - 基本使用](02_basic_usage.py)：介绍常用的命令行参数。
- [03_config_file.py - 配置文件](03_config_file.py)：展示 `pyrightconfig.json` 的标准配置项。
- [04_check_modes.py - 检查模式](04_check_modes.py)：介绍 `off`、`basic`、`standard` 和 `strict` 模式。
- [05_vscode_integration.py - VS Code 集成](05_vscode_integration.py)：展示如何配置 Pylance 插件。
- [06_ignore_checks.py - 忽略检查](06_ignore_checks.py)：展示如何使用 `# pyright: ignore` 处理特定行的警告。

## 核心特性

1. **极致速度**：得益于 TypeScript 编写，它在处理大型项目时比 mypy 快得多。
2. **零配置友好**：即使没有配置文件，它也能提供相当不错的检查。
3. **Pylance 支持**：在 VS Code 中可以获得实时的、内联的类型错误提示。

## 学习建议

- 如果你是 VS Code 用户，pyright 是你的不二之选。
- 在大型 Mono-repo 或具有海量代码的项目中，pyright 的性能优势会非常明显。
